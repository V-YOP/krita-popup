

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

    def __init__(self) -> None:
        super().__init__()
        self.__last_preset: None | Resource = None
    
        self.notifier = Krita.instance().notifier()
        self.notifier.setActive(True)
        
        self.__stop_loop = False
        def stop_me():
            self.__stop_loop = True
        self.notifier.applicationClosing.connect(stop_me)
        self.__loop_me()

    def __main_loop(self):
        current = self.current_brush
        if current is None:
            return
        if self.__last_preset is None or self.__last_preset.name() != current.name():
            self.currentBrushChanged.emit(current)
            self.__last_preset = current
            print('brush changed: ', current.name())

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

ViewState()