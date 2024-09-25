from dataclasses import dataclass
from krita_popup.helper.QtAll import *
from krita_popup.helper import Toolbox, ToolEnum
from krita import *
from ._item_gegistry import RegistItem

TOOLBUTTON_STYLE = """
QToolButton {
    width: 32px;
    height: 32px;
    border: None;
}
QToolButton:checked {
    background-color: #647c91;
}
""".strip()

@dataclass
class ToolButtonGroupConfig:
    tools: list[str]
    """
    tools' objectNames
    """
    horizontal: bool = True

@RegistItem('Tool Button Group', ToolButtonGroupConfig)
class ToolButtonGroup(QWidget):
    def __init__(self, config: ToolButtonGroupConfig) -> None:
        super().__init__()
        self.__toolbox = Toolbox()
        self.__tools = [ToolEnum.from_object_name(i) for i in config.tools]
        self.__button_widgets: list[QToolButton] = []
        self.__toolbox.currentToolChanged.connect(self.on_tool_changed)

        self.__layout = QHBoxLayout() if config.horizontal else QVBoxLayout()
        self.setLayout(self.__layout)

        for tool in self.__tools:
            # each tool a button
            btn_widget = self.__create_tool_button(tool)
            self.__button_widgets.append(btn_widget)
            self.__layout.addWidget(btn_widget)

    def __create_tool_button(self, tool_enum: ToolEnum) -> QToolButton:
        btn = QToolButton(self)
        btn.setObjectName(tool_enum.object_name)
        btn.setCheckable(True)
        btn.setStyleSheet(TOOLBUTTON_STYLE)
        btn.setIcon(Krita.instance().icon(tool_enum.icon))
        btn.setToolTip(tool_enum.tooltip)
        def onclick():
            self.__toolbox.current_tool = tool_enum
        btn.clicked.connect(onclick)
        return btn
            
    def on_tool_changed(self, new_tool: ToolEnum):
        """
        when tool changed, reset checked status
        """
        for tool, button in zip(self.__tools, self.__button_widgets):
            button.setChecked(tool == new_tool)
    
