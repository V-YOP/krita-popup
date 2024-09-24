from krita import *
from krita_popup.helper.QtAll import *

class KritaPopupExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        # TODO create actual handler for this window, window will be identified by objectName 
        menu_action = window.createAction('krita_popup_menu', 'Krita Popup', "tools")
        self.menu = QMenu('Krita Popup', window.qwindow())
        menu_action.setMenu(self.menu)

        toggle_display_action = window.createAction("krita_pupup_display_toggle", "Toggle Display Popup", "tools/krita_popup_menu")
        toggle_display_action.setChecked(True)
        toggle_display_action.triggered.connect(lambda: ...)

        setting_action = window.createAction("krita_pupup_settings", "Settings", "tools/krita_popup_menu")
        setting_action.triggered.connect(lambda: ...)

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KritaPopupExtension(Krita.instance())) 
