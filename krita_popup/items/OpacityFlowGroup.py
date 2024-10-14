from typing import Callable, Literal, TypedDict

from krita_popup.helper.QtAll import *
from krita import *
from krita import Window
from itertools import zip_longest
from .BaseItem import BaseItem
from ._item_gegistry import RegistItem

TOOLBUTTON_STYLE = """
QToolButton {
    width: 32px;
    height: 32px;
    background-color: #31363b;
}
QToolButton:checked {
    background-color: #647c91;
}
""".strip()

class OpacityFlowGroupConfig(TypedDict):
    """
    horizontal: horizontal layout
    """
    value_type: Literal['opacity', 'flow']
    level: int # 有多少个按钮
    curve: Literal['linear', 'quadratic', 'cubic']
    horizontal: bool
    invert: bool

@RegistItem('Opacity Flow Group')
class OpacityFlowGroup(BaseItem[OpacityFlowGroupConfig]):
    @staticmethod
    def default_configuration() -> OpacityFlowGroupConfig:
        return OpacityFlowGroupConfig(
            value_type='opacity',
            level=7,
            curve='quadratic',
            horizontal=False,
            invert=True,
        )

    @staticmethod
    def create(configuration: OpacityFlowGroupConfig, window: Window, editing_mode: bool) -> 'OpacityFlowGroup':
        return OpacityFlowGroup(configuration)
    
    def start_editing(self) -> OpacityFlowGroupConfig | None:
        # TODO 
        return None

    def __init__(self, conf: OpacityFlowGroupConfig) -> None:
        super().__init__()
        self.__config = conf
        self.setLayout(QHBoxLayout() if self.__config['horizontal'] else QVBoxLayout())
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0,0,0,0)

        self.__value_change_cbs = []

        end_value_iter = self.__level_start_values()
        next(end_value_iter)
        ranges = list(zip_longest(self.__level_start_values(), end_value_iter))
        if self.__config['invert']:
            ranges = reversed(ranges)
        for start_value, end_value in ranges:
            btn, cb = self.__create_level_button(f'{start_value:2.2%}', start_value, end_value)
            self.__value_change_cbs.append(cb)
            self.layout().addWidget(btn)
    
    # def loop_me(self):


    def __level_start_values(self):
        def remap_value(value: float):
            match self.__config['curve']:
                case 'linear':
                    scale = 1
                case 'quadratic':
                    scale = 2
                case 'cubic':
                    scale = 3
            return value ** scale

        level = self.__config['level']
        level -= 1
        step = 1 / level  # 使用浮点除法以保持精度
        i = 0
        for _ in range(level):
            yield remap_value(i) 
            i += step
        yield remap_value(1.0)  # 最后一个数确保是100


    def __create_level_button(self, text: str, value_start_inclusive: float, value_end_exclusive: float | None) -> tuple[QToolButton, Callable[[float], None]]:
        "return btn instance and a 'refresher' which accept current value"
        btn = QToolButton()
        btn.setCheckable(True)
        btn.setFocusPolicy(Qt.NoFocus)
        btn.setStyleSheet(TOOLBUTTON_STYLE)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn.setText(text)
        def refresh_me(current_value: float):
            if current_value >= value_start_inclusive and (value_end_exclusive is None or current_value < value_end_exclusive):
                btn.setChecked(True)
            else:
                btn.setChecked(False)
        def onclick():
            self.__set_current_value(value_start_inclusive)
            for refresh in self.__value_change_cbs:
                refresh(value_start_inclusive)
        btn.clicked.connect(onclick)

        if current_value := self.__get_current_value():
            refresh_me(current_value)
        
        return btn, refresh_me


    def __get_current_value(self) -> float | None:
        if (win := Krita.instance().activeWindow()) and (view := win.activeView()):
            if self.__config['value_type'] == 'opacity':
                return view.paintingOpacity()
            return view.paintingFlow() 
        
    def __set_current_value(self, value: float):
        if (win := Krita.instance().activeWindow()) and (view := win.activeView()):
            if self.__config['value_type'] == 'opacity':
                view.setPaintingOpacity(value)
                return
            view.setPaintingFlow(value)
