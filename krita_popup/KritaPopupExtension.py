from krita import *
from krita_popup.constants import TOGGLE_ACTION_ID
from krita_popup.helper.QtAll import *
from krita_popup.helper.Toolbox import ToolEnum
from krita_popup.popup import Popup

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

        self.toggle_action = window.createAction(TOGGLE_ACTION_ID, 'Toggle Popup', 'tools/krita_popup_menu')
        self.toggle_action.setCheckable(True)
        self.toggle_action.triggered.connect(self.toggle_popup)

    def toggle_popup(self):
        import importlib
        if not hasattr(self, 'popup'):
            from krita_popup.items.ToolButtonGroup import ToolButtonGroup, ToolButtonGroupConfig
            from krita_popup.items.KritaDockBorrower import KritaDockBorrower
            
            tools = ToolButtonGroup(ToolButtonGroupConfig(
                [ToolEnum.KRITA_SHAPE_KIS_TOOL_BRUSH.object_name, ToolEnum.KIS_TOOL_CROP.object_name]
            ))
            tools_rect = QRect(0, 0, 200, 100)
            tools_rect.moveCenter(QPoint(0, -150))

            tool_option_docker = KritaDockBorrower(next(i for i in Krita.instance().dockers() if i.objectName() == 'sharedtooldocker'))
            tool_option_rect = QRect(0,0,400, 800)
            tool_option_rect.moveCenter(QPoint(300, 0))
            print(tool_option_rect)
            self.popup = Popup([
                (tools, tools_rect),
                (tool_option_docker, tool_option_rect)
            ], under_cursor=True)
            self.popup.addAction(self.toggle_action) # make sure popup can listen shortcut
            def state_changed(state: Qt.ApplicationState):
                if state == Qt.ApplicationInactive:
                    self.popup.hide()
                    self.toggle_action.setChecked(False)
            QApplication.instance().applicationStateChanged.connect(state_changed)
        
        if self.toggle_action.isChecked():
            self.popup.show()
            QTimer.singleShot(0, lambda: QApplication.setActiveWindow(Krita.instance().activeWindow().qwindow())) # re-focus krita window
        else:
            self.popup.hide()

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KritaPopupExtension(Krita.instance())) 
