from typing import TypedDict

from PyQt5.QtGui import QKeyEvent, QRegion
from krita_popup.helper.QtAll import *
from krita_popup.helper import Toolbox, ToolEnum
from krita import *
from .ToolButtonGroupConfig import ToolButtonGroupConfig
from .ToolButtonEditDialog import exec_editing_dialog
from ..BaseItem import BaseItem
from .._item_gegistry import RegistItem

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



@RegistItem('Tool Button Group')
class ToolButtonGroup(QWidget, BaseItem[ToolButtonGroupConfig]):
    @staticmethod
    def default_configuration() -> ToolButtonGroupConfig:
        return ToolButtonGroupConfig(
            tools=[ToolEnum.KRITA_SHAPE_KIS_TOOL_BRUSH.object_name],
            horizontal=True,
        )
    
    @staticmethod
    def create(conf: ToolButtonGroupConfig):
        return ToolButtonGroup(conf)  # type: ignore
    
    def __init__(self, config: ToolButtonGroupConfig) -> None:
        super().__init__()
        self.__config = config
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__toolbox = Toolbox()
        self.__tools = [ToolEnum.from_object_name(i) for i in config['tools']]
        self.__button_widgets: list[QToolButton] = []
        self.__toolbox.currentToolChanged.connect(self.on_tool_changed)

        self.__layout = QHBoxLayout() if config['horizontal'] else QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setSpacing(0) # remove item spacing
        self.__layout.setContentsMargins(0,0,0,0) # remove margin
        
        for tool in self.__tools:
            # each tool a button
            btn_widget = self.__create_tool_button(tool)
            self.__button_widgets.append(btn_widget)
            self.__layout.addWidget(btn_widget)

    def start_editing(self) -> ToolButtonGroupConfig | None:
        return exec_editing_dialog(self.__config)

    def __create_tool_button(self, tool_enum: ToolEnum) -> QToolButton:
        btn = QToolButton(self)
        btn.setFocusPolicy(Qt.NoFocus)
        btn.setObjectName(tool_enum.object_name)
        btn.setCheckable(True)
        if self.__toolbox.current_tool == tool_enum:
            btn.setChecked(True)
        btn.setStyleSheet(TOOLBUTTON_STYLE)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn.setIcon(tool_enum.qicon)
        # when resize, set icon to my size 80%
        def set_icon_size(self, _):
            btn.setIconSize(btn.size() * 0.6)
        btn.resizeEvent = set_icon_size.__get__(btn)
        btn.setToolTip(tool_enum.tooltip)
        def onclick(_, __):
            if not btn.isChecked():
                btn.setChecked(True)
            self.__toolbox.current_tool = tool_enum
        btn.mousePressEvent = onclick.__get__(btn)
        return btn
        
    def on_tool_changed(self, new_tool: ToolEnum):
        """
        when tool changed, reset checked status
        """
        for tool, button in zip(self.__tools, self.__button_widgets):
            button.setChecked(tool == new_tool)
    
    def on_show(self):
        print('me show')
        return super().on_show()
    def on_hide(self):
        print('me hide')
        return super().on_hide()
    # def custom_mask(self) -> QRegion:
    #     region = QRegion()
    #     region = region.united(QRect(0,0,30,30))
    #     return region
