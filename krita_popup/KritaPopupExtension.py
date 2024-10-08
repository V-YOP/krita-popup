from functools import partial
from krita import *
from krita_popup.constants import TOGGLE_ACTION_ID
from krita_popup.core import PopupProvider
from krita_popup.helper.QtAll import *
from krita_popup.helper.Toolbox import ToolEnum
from krita_popup.helper.util import get_window_from_object_name
from krita_popup.popup import Popup

class KritaPopupExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        
    def setup(self):
        self.__popup_provider = PopupProvider()

    def createActions(self, window):
        menu_action = window.createAction('krita_popup_menu', 'Krita Popup', "tools")
        self.menu = QMenu('Krita Popup', window.qwindow())
        menu_action.setMenu(self.menu)

        for i in range(0, 10):
            toggle_action = window.createAction(TOGGLE_ACTION_ID + str(i), f'Toggle Popup {i}', 'tools/krita_popup_menu')
            toggle_action.triggered.connect(partial(self.toggle_popup, window.qwindow().objectName(), i))
            
        for i in range(0, 10):
            setting_action = window.createAction(f"krita_pupup_edit_popup{i}", f"Edit Popup {i}", "tools/krita_popup_menu")
            setting_action.triggered.connect(partial(self.start_editing, window.qwindow().objectName(), i))

    def start_editing(self, window_object_name: str, layout_idx: int):
        window = get_window_from_object_name(window_object_name)
        if not window.views():
            return
        self.__popup_provider.start_editing(window, layout_idx)

    def toggle_popup(self, window_object_name: str, layout_idx: int):
        window = get_window_from_object_name(window_object_name)
        print('111', window_object_name)
        if not window.views():
            return
        if self.__popup_provider.is_popup_visible(layout_idx):
            self.__popup_provider.hide_popup()
        else:
            self.__popup_provider.show_popup(window, layout_idx)


# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KritaPopupExtension(Krita.instance())) 
