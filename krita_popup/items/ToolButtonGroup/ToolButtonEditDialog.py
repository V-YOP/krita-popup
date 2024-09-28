from typing import TypedDict
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListView
from krita import *
from krita_popup.helper import Toolbox, ToolEnum
from krita_popup.helper.QtAll import *

from .ToolButtonGroupConfig import ToolButtonGroupConfig

class ToolsEditWidget(QWidget):
    def __init__(self, selected_tools: list[ToolEnum]) -> None:
        super().__init__(None)

        not_selected_tools = [tool for tool in ToolEnum if tool not in selected_tools]
        layout = QHBoxLayout()
        self.__not_selected_tool_widget = self.__create_list_widget(not_selected_tools)
        self.__selected_tool_widget = self.__create_list_widget(selected_tools)

        self.__deselect_button = QPushButton()
        self.__deselect_button.setIcon(Krita.instance().icon('arrow-left'))
        self.__deselect_button.setMinimumSize(16, 64)
        self.__deselect_button.clicked.connect(self.__deselect_item)
        self.__select_button = QPushButton()
        self.__select_button.setIcon(Krita.instance().icon('arrow-right'))
        self.__select_button.setMinimumSize(16, 64)
        self.__select_button.clicked.connect(self.__select_item)

        layout.addWidget(self.__not_selected_tool_widget)
        layout.addWidget(self.__deselect_button)
        layout.addWidget(self.__select_button)
        layout.addWidget(self.__selected_tool_widget)
        self.setLayout(layout)

    def __select_item(self):
        selected = self.__not_selected_tool_widget.selectedItems()
        for select in selected:
            token_item = self.__not_selected_tool_widget.takeItem(self.__not_selected_tool_widget.row(select))
            self.__selected_tool_widget.addItem(token_item)

    def __deselect_item(self):
        selected = self.__selected_tool_widget.selectedItems()
        for select in selected:
            token_item = self.__selected_tool_widget.takeItem(self.__selected_tool_widget.row(select))
            self.__not_selected_tool_widget.addItem(token_item)
    
    def __create_list_widget(self, tools: list[ToolEnum]):
        res = QListWidget()
        res.setSpacing(4) # 元素间距
        res.setWrapping(True) # 自动换行
        res.setFlow(QListWidget.LeftToRight)  # 横向排列
        res.setResizeMode(QListWidget.Adjust)  # 自动调整大小
        res.setSelectionMode(QListWidget.SingleSelection)  # 单选模式
        res.setDefaultDropAction(Qt.DropAction.MoveAction) # 拖动行为指定为Move（不然它会复制）
        res.setDragDropMode(QAbstractItemView.InternalMove) # 允许内部拖拽
        res.setIconSize(QSize(32,32)) # 指定图标大小

        for tool in tools:
            item = QListWidgetItem(
                tool.qicon,
                tool.object_name
            )
            item.setToolTip(f'cn: {tool.cn_tooltip}\nen: {tool.tooltip}')
            res.addItem(item)

        return res

    def selected_tools(self):
        object_names = map(lambda x: x.text(), self.__selected_tool_widget.findItems('', Qt.MatchFlag.MatchStartsWith))
        return [ToolEnum.from_object_name(i) for i in object_names]

def exec_editing_dialog(setting: ToolButtonGroupConfig) -> ToolButtonGroupConfig | None:
    dialog = QDialog(None)
    dialog.resize(600, 800)
    dialog.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    dialog.raise_()

    horizontal_checkbox = QCheckBox()
    horizontal_checkbox.setText('Horizontal')
    horizontal_checkbox.setChecked(setting['horizontal'])
    
    tools_widget = ToolsEditWidget([ToolEnum.from_object_name(i) for i in setting['tools']])

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.accepted.connect(lambda: dialog.done(0))
    button_box.rejected.connect(lambda: dialog.done(1))
    dialog.setLayout(QVBoxLayout())

    dialog.layout().addWidget(horizontal_checkbox)
    dialog.layout().addWidget(tools_widget)
    dialog.layout().addWidget(button_box)

    if dialog.exec_() == 1:
        return None
    
    horizontal = horizontal_checkbox.isChecked()
    tools = tools_widget.selected_tools()
    return ToolButtonGroupConfig(
        tools=[tool.object_name for tool in tools],
        horizontal=horizontal
    )


if __name__ == '__main__':
    # tool = ToolsEditWidget([ToolEnum.KRITA_SHAPE_KIS_TOOL_BRUSH])
    # tool.resize(1000, 1000)
    # tool.raise_()
    # tool.show()
    print(exec_editing_dialog(ToolButtonGroupConfig(
        tools=['KisToolSelectOutline', 'KisToolSelectSimilar', 'KisToolSelectRectangular'],
        horizontal=True,
    )))