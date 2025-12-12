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
        pass

    def createActions(self, window):
        """when view_show_canvas_only is set to True, set BrushesAndStuff to True"""
        window_identifier = window.qwindow().objectName()

        # execution must be delayed because BrushAndStuff action is dynamicly added
        @partial(QTimer.singleShot, 0)
        def _():
            # the former window is destroyed at this moment
            window = next(i for i in Krita.instance().windows() if i.qwindow().objectName() == window_identifier)
            canvas_only_action, toolbar_action = None, None
            for action in window.qwindow().actions():
                if action.objectName() == 'view_show_canvas_only':
                    canvas_only_action = action
                if action.objectName() == 'BrushesAndStuff':
                    toolbar_action = action
                if canvas_only_action and toolbar_action:
                    break
            else:
                raise AssertionError('Impossible')

            @canvas_only_action.triggered.connect
            def _(checked):
                if checked and not toolbar_action.isChecked(): 
                    toolbar_action.setChecked(True)

    


# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KritaPopupExtension(Krita.instance())) 
