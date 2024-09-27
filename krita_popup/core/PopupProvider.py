
from krita import Krita
from krita_popup.constants import TOGGLE_ACTION_ID
from .ConfigurationService import ConfigurationService
from .EditingPopupService import EditingPopupService
from krita_popup.helper import singleton
from krita_popup.popup import EditingPopup, Popup
from krita_popup.items import item_defs
from krita_popup.helper.QtAll import *

from typing import NamedTuple

class ItemInstance(NamedTuple):
    uuid: str
    widget: QWidget
    geo: QRect

@singleton
class PopupProvider:
    """
    The guy who makes his hand dirty handling everything about popup including toggle, edit, configuration r/w
    """

    def __init__(self) -> None:
        self.__editing_popup_service = EditingPopupService()
        self.__configuration_service = ConfigurationService()
        self.__popup = Popup([], under_cursor=True)

        self.__notifier = Krita.instance().notifier()
        self.__notifier.setActive(True)
        
        # make sure popup hides when application closing, otherwise it will stay on backgrond and prevent krita from starting...
        self.__notifier.imageClosed.connect(lambda: self.set_popup_visible(False))
        self.__notifier.applicationClosing.connect(lambda: self.set_popup_visible(False))
        def state_changed(state: Qt.ApplicationState):
            if state == Qt.ApplicationInactive and self.is_popup_visible():
                self.set_popup_visible(False)
        QApplication.instance().applicationStateChanged.connect(state_changed)
        

    def __create_items_from_configuration(self):
        item_def = item_defs()
        confs = self.__configuration_service.load_configurations()
        items: list[ItemInstance] = []
        for conf in confs:
            item_type, id, conf, geo = conf['item_type'], conf['id'], conf['conf'], conf['geo']
            assert item_type in item_def, f'unknown item type: {item_type}'
            items.append(ItemInstance(id, item_def[item_type].create(conf), QRect(*geo)))
        return items

    def is_popup_visible(self):
        return self.__popup.isVisible()
    
    def set_popup_visible(self, visible: bool):
        """
        toggle popup display
        """
        
        # make sure the     
        action = Krita.instance().action(TOGGLE_ACTION_ID)
        if action is not None and action not in self.__popup.actions():
            self.__popup.addAction(action)
            
        if not visible:
            self.__popup.hide()
            self.__popup.clear_items()
            return

        items = self.__create_items_from_configuration()
        for _, widget, geo in items:
            self.__popup.add_item(widget, geo)
        self.__popup.show()
        QTimer.singleShot(0, lambda: QApplication.setActiveWindow(Krita.instance().activeWindow().qwindow())) # re-focus krita window

    def start_editing(self):
        ...