from functools import partial
from krita import *
from krita_popup.constants import TOGGLE_ACTION_ID
from krita_popup.core import PopupProvider
from krita_popup.helper.QtAll import *
from krita_popup.helper.Toolbox import ToolEnum
from krita_popup.popup import Popup

class KritaPopupExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        
    def setup(self):
        self.__popup_provider = PopupProvider()

    def createActions(self, window):
        # TODO create actual handler for this window, window will be identified by objectName 
        menu_action = window.createAction('krita_popup_menu', 'Krita Popup', "tools")
        self.menu = QMenu('Krita Popup', window.qwindow())
        menu_action.setMenu(self.menu)

        for i in range(0, 10):
            setting_action = window.createAction(f"krita_pupup_edit_popup{i}", f"Edit Popup {i}", "tools/krita_popup_menu")
            setting_action.triggered.connect(partial(self.start_editing, i))

            toggle_action = window.createAction(TOGGLE_ACTION_ID + str(i), f'Toggle Popup {i}', 'tools/krita_popup_menu')
            toggle_action.triggered.connect(partial(self.toggle_popup, i))
    
    def start_editing(self, layout_idx: int):
        if not Krita.instance().documents():
            return
        self.__popup_provider.start_editing(layout_idx)
    def toggle_popup(self, layout_idx: int):
        if not Krita.instance().documents():
            return
        if self.__popup_provider.is_popup_visible(layout_idx):
            self.__popup_provider.hide_popup()
        else:
            self.__popup_provider.show_popup(layout_idx)


# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KritaPopupExtension(Krita.instance())) 
