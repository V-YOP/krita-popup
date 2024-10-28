
from krita import *
from krita_popup.constants import TOGGLE_ACTION_ID
from krita_popup.helper.util import get_window_from_object_name
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
        self.__current_layout_idx: int | None = None

        self.__notifier = Krita.instance().notifier()
        self.__notifier.setActive(True)

        # make sure popup hides when application closing, otherwise it will stay on backgrond and prevent krita from starting...
        # self.__notifier.imageClosed.connect(lambda: self.hide_popup())
        # self.__notifier.applicationClosing.connect(lambda: self.hide_popup())
        # def state_changed(state: Qt.ApplicationState):
        #     if state == Qt.ApplicationInactive and self.is_popup_visible():
        #         self.hide_popup()
        # QApplication.instance().applicationStateChanged.connect(state_changed) # type: ignore
        # self.__last_window: str = ''
        

    def __create_items_from_configuration(self, window: Window, layout_idx: int):
        item_def = item_defs()
        confs = self.__configuration_service.load_item_configs(layout_idx)
        items: list[ItemInstance] = []
        for conf in confs:
            item_type, id, geo = conf['item_type'], conf['id'], conf['geo']
            assert item_type in item_def, f'unknown item type: {item_type}'
            items.append(ItemInstance(id, conf, item_def[item_type].create(conf['conf'], window, False), QRect(*geo)))
        return items

    def is_popup_visible(self, layout_idx: int | None = None):
        visible = self.__under_cursor_popup.isVisible()
        if layout_idx is not None:
            return visible and layout_idx == self.__current_layout_idx
        return visible

    def __init_actions(self, window: Window):
        """
        let the popup can listen shortcut
        """
        # if window.qwindow().objectName() == self.__last_window:
        #     return
        # # when window changed, reset actions
        # for action in self.__under_cursor_popup.actions():
        #     self.__under_cursor_popup.removeAction(action)
        #     self.__fixed_popup.removeAction(action)

        # for action in window.qwindow().actions():
        #     self.__under_cursor_popup.addAction(action)
        #     self.__fixed_popup.addAction(action)
            
        # self.__last_window = window.qwindow().objectName()

    def show_popup(self, window: Window, layout_idx: int):
        self.__init_actions(window)
        self.__fixed_popup.setParent(window.qwindow())
        self.__under_cursor_popup.setParent(window.qwindow())

        self.__under_cursor_popup.hide()
        self.__under_cursor_popup.clear_items()
        self.__fixed_popup.hide()
        self.__fixed_popup.clear_items()
        self.__current_layout_idx = layout_idx
        items = self.__create_items_from_configuration(window, layout_idx)
        for item in items:
            if item.config.get('fixed', False):
                self.__fixed_popup.add_item(item.widget, item.geo)
            else:
                self.__under_cursor_popup.add_item(item.widget, item.geo)

        self.__under_cursor_popup.show() # fiexd popup should beyonds to under cursor popup 
        self.__fixed_popup.show()
        self.__under_cursor_popup.raise_()
        self.__fixed_popup.raise_()
        # window_object_name = window.qwindow().objectName()
        # QTimer.singleShot(0, lambda: QApplication.setActiveWindow(get_window_from_object_name(window_object_name).qwindow())) # re-focus krita window

    def hide_popup(self):
        self.__under_cursor_popup.hide()
        self.__under_cursor_popup.clear_items()
        self.__fixed_popup.hide()
        self.__fixed_popup.clear_items()
        self.__current_layout_idx = None

    def start_editing(self, window: Window, layout_idx: int):
        """
        Fetch current items, showing editing popup, wait for 
        """
        self.hide_popup() # hide popup first
        
        items = self.__create_items_from_configuration(window, layout_idx)
        new_items = self.__editing_popup_service.wait_for_done(items)
        if new_items is None:
            return # user click cancel, don't do anything
        
        self.__configuration_service.save_item_configs(layout_idx, new_items)