

from krita_popup.helper.BlendingMode import BlendingMode
from . import singleton
from krita import *
from krita_popup.helper.QtAll import *

CHECK_INTERVAL = 100

@singleton
class ViewState(QObject):
    """
    provide method and signal about state of views, like Brush Preset, Brush Size, Brush Flow...
    """
    currentBrushChanged = pyqtSignal(Resource, name='currentBrushChanged')
    currentLayerBlendingModeChanged = pyqtSignal(BlendingMode, name='currentLayerBlendingModeChanged')
    """
    argument: current Brush Preset `Resource`
    """

    def __init__(self) -> None:
        super().__init__()
        self.__last_brush: None | Resource = None
        self.__last_layer_blending_mode: None | BlendingMode = None
    
        self.notifier = Krita.instance().notifier()
        self.notifier.setActive(True)
        
        self.__stop_loop = False
        def stop_me():
            self.__stop_loop = True
        self.notifier.applicationClosing.connect(stop_me)
        self.__loop_me()

    def __main_loop(self):
        if current_brush := self.current_brush:
            if self.__last_brush is None or self.__last_brush.name() != current_brush.name():
                self.currentBrushChanged.emit(current_brush)
                self.__last_brush = current_brush
        
        if current_layer_blending_mode := self.current_layer_blending_mode:
            if self.__last_layer_blending_mode is None or self.__last_layer_blending_mode != current_layer_blending_mode:
                self.currentLayerBlendingModeChanged.emit(current_layer_blending_mode)
                self.__last_layer_blending_mode = current_layer_blending_mode

    def __loop_me(self):
        if self.__stop_loop:
            return
        self.__main_loop()
        QTimer.singleShot(CHECK_INTERVAL, self.__loop_me)
    
    @property
    def current_brush(self):
        if not (win := Krita.instance().activeWindow()) or \
           not (view := win.activeView()):
            return None
        return view.currentBrushPreset()
    
    @current_brush.setter
    def current_brush(self, new_brush: Resource):
        if not (win := Krita.instance().activeWindow()) or \
           not (view := win.activeView()):
            return
        assert new_brush.type() == 'preset', f'{new_brush.name()} is not a brush preset!'
        view.setCurrentBrushPreset(new_brush)

    @property
    def current_layer_blending_mode(self):
        if not (document := Krita.instance().activeDocument()):
            return None
        return BlendingMode.by_id(document.activeNode().blendingMode())

    @current_layer_blending_mode.setter
    def current_layer_blending_mode(self, new_blending_mode: BlendingMode):
        if not (document := Krita.instance().activeDocument()):
            return None
        document.activeNode().setBlendingMode(new_blending_mode.id)

ViewState()