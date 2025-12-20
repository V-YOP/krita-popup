from functools import partial
from krita import *
from krita_popup.constants import TOGGLE_ACTION_ID
from krita_popup.core import PopupProvider
from krita_popup.helper.QtAll import *
from krita_popup.helper.Toolbox import ToolEnum
from krita_popup.helper.util import get_window_from_object_name
from krita_popup.popup import Popup
from krita_popup.helper.KeyHoldManager import KeyHoldManager, KeyHoldState
from krita_popup.constants import POPUP_NUM, HOLD_THRESHOLD_MS

class KritaPopupExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        
    def setup(self):
        self.__popup_provider = PopupProvider()
        self.key_hold_managers = []

    def createActions(self, window):
        menu_action = window.createAction('krita_popup_menu', 'Krita Popup', "tools")
        self.menu = QMenu('Krita Popup', window.qwindow())
        menu_action.setMenu(self.menu)

        
        for i in range(0, POPUP_NUM):
            toggle_action = window.createAction(TOGGLE_ACTION_ID + str(i), f'Toggle Popup {i}', 'tools/krita_popup_menu')
            self.key_hold_managers.append(KeyHoldManager(window.qwindow(), toggle_action, partial(self.on_toggle_popup, window.qwindow().objectName(), i), HOLD_THRESHOLD_MS))
            
        for i in range(0, POPUP_NUM):
            setting_action = window.createAction(f"krita_pupup_edit_popup{i}", f"Edit Popup {i}", "tools/krita_popup_menu")
            setting_action.triggered.connect(partial(self.__start_editing, window.qwindow().objectName(), i))

    def on_toggle_popup(self, window_object_name: str, layout_idx: int, key_hold_state: KeyHoldState):
        window = get_window_from_object_name(window_object_name)
        if not window.views():
            return
        
        if key_hold_state == KeyHoldState.PRESSED:
            # 按下则toggle
            if self.__popup_provider.is_popup_visible(layout_idx):
                self.__popup_provider.hide_popup()
            else:
                self.__popup_provider.show_popup(window, layout_idx)
        elif key_hold_state == KeyHoldState.PRESSED_TIMEOUT:
            # 超时，什么都不做
            pass
        elif key_hold_state == KeyHoldState.RELEASED_BEFORE_TIMEOUT:
            # 说明是短按，什么都不做
            pass
        elif key_hold_state == KeyHoldState.RELEASED_AFTER_TIMEOUT:
            # 说明是长按，hide它
            self.__popup_provider.hide_popup()

    def __start_editing(self, window_object_name: str, layout_idx: int):
        window = get_window_from_object_name(window_object_name)
        if not window.views():
            return
        self.__popup_provider.start_editing(window, layout_idx)

    def __toggle_popup(self, window_object_name: str, layout_idx: int):
        window = get_window_from_object_name(window_object_name)
        if not window.views():
            return
        if self.__popup_provider.is_popup_visible(layout_idx):
            self.__popup_provider.hide_popup()
        else:
            self.__popup_provider.show_popup(window, layout_idx)

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KritaPopupExtension(Krita.instance())) 
