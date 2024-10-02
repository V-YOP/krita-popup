
from krita import *
from krita_popup.constants import TOGGLE_ACTION_ID
from .ConfigurationService import ConfigurationService, ItemInstance
from .EditingPopupService import EditingPopupService
from krita_popup.helper import singleton
from krita_popup.popup import EditingPopup, Popup
from krita_popup.items import item_defs
from krita_popup.helper.QtAll import *

@singleton
class PopupProvider:
    """
    The guy who makes his hand dirty handling everything about popup including toggle, edit, configuration r/w.

    Actually, there's two popup displaying, one is always fixed to screen, one is always under control.
    """

    def __init__(self) -> None:
        self.__editing_popup_service = EditingPopupService()
        self.__configuration_service = ConfigurationService()

        self.__under_cursor_popup = Popup([], under_cursor=True)
        self.__fixed_popup = Popup([], under_cursor=False)

        self.__notifier = Krita.instance().notifier()
        self.__notifier.setActive(True)
        self.__current_layout_idx: int | None = None

        # make sure popup hides when application closing, otherwise it will stay on backgrond and prevent krita from starting...
        self.__notifier.imageClosed.connect(lambda: self.hide_popup())
        self.__notifier.applicationClosing.connect(lambda: self.hide_popup())
        def state_changed(state: Qt.ApplicationState):
            if state == Qt.ApplicationInactive and self.is_popup_visible():
                self.hide_popup()
        QApplication.instance().applicationStateChanged.connect(state_changed) # type: ignore
        

    def __create_items_from_configuration(self, layout_idx: int):
        item_def = item_defs()
        confs = self.__configuration_service.load_configurations(layout_idx)
        items: list[ItemInstance] = []
        for conf in confs:
            item_type, id, geo = conf['item_type'], conf['id'], conf['geo']
            assert item_type in item_def, f'unknown item type: {item_type}'
            items.append(ItemInstance(id, conf, item_def[item_type].create(conf['conf']), QRect(*geo)))
        return items

    def is_popup_visible(self, layout_idx: int | None = None):
        visible = self.__under_cursor_popup.isVisible()
        if layout_idx is not None:
            return visible and layout_idx == self.__current_layout_idx
        return visible

    def __init_actions(self):
        """
        let the popup can listen shortcut
        """
        action = Krita.instance().action(TOGGLE_ACTION_ID + str(0))
        if action is None or action in self.__under_cursor_popup.actions():
            return
        for action in Krita.instance().actions():
            self.__under_cursor_popup.addAction(action)
            self.__fixed_popup.addAction(action)

    def show_popup(self, layout_idx: int):
        self.__init_actions()
        
        self.__under_cursor_popup.hide()
        self.__under_cursor_popup.clear_items()
        self.__fixed_popup.hide()
        self.__fixed_popup.clear_items()
        self.__current_layout_idx = layout_idx
        items = self.__create_items_from_configuration(layout_idx)
        for item in items:
            if item.config.get('fixed', False):
                self.__fixed_popup.add_item(item.widget, item.geo)
            else:
                self.__under_cursor_popup.add_item(item.widget, item.geo)

        self.__fixed_popup.show()
        self.__under_cursor_popup.show() # under cursor popup should be beyond fiexd popup
        QTimer.singleShot(0, lambda: QApplication.setActiveWindow(Krita.instance().activeWindow().qwindow())) # re-focus krita window

    def hide_popup(self):
        self.__under_cursor_popup.hide()
        self.__under_cursor_popup.clear_items()
        self.__fixed_popup.hide()
        self.__fixed_popup.clear_items()
        self.__current_layout_idx = None

    def start_editing(self, layout_idx: int):
        """
        Fetch current items, showing editing popup, wait for 
        """
        self.hide_popup() # hide popup first
        
        items = self.__create_items_from_configuration(layout_idx)
        new_items = self.__editing_popup_service.wait_for_done(items)
        if new_items is None:
            return # user click cancel, don't do anything
        
        self.__configuration_service.save_configurations(layout_idx, new_items)