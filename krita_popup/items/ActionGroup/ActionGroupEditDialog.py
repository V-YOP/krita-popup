from typing import TypedDict
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListView
from krita import *
from krita_popup.helper.QtAll import *

# from .ActionGroupConfig import ActionGroupConfig


class ActionGroupConfig(TypedDict):
    """
    actions: action object names

    horizontal: horizontal layout
    """
    actions: list[str]
    horizontal: bool

class ActionsEditWidget(QWidget):
    def __init__(self, selected_actions: list[QAction], all_actions: list[QAction]) -> None:
        super().__init__(None)

        self.__all_actions = {i.objectName(): i for i in all_actions}

        selected_actions = [i for i in selected_actions]
        
        layout = QHBoxLayout()
        
        self.__not_selected_action_filter = QLineEdit()
        self.__not_selected_action_filter.setPlaceholderText('Filter')
        self.__not_selected_action_widget = self.__create_list_widget([])
        self.__not_selected_action_filter.textChanged.connect(lambda: self.__refresh_not_selected_actions(self.__not_selected_action_filter.text()))

        self.__selected_action_widget = self.__create_list_widget(selected_actions)

        self.__deselect_button = QPushButton()
        self.__deselect_button.setIcon(Krita.instance().icon('arrow-left'))
        self.__deselect_button.setMinimumSize(16, 64)
        self.__deselect_button.clicked.connect(self.__deselect_item)
        self.__select_button = QPushButton()
        self.__select_button.setIcon(Krita.instance().icon('arrow-right'))
        self.__select_button.setMinimumSize(16, 64)
        self.__select_button.clicked.connect(self.__select_item)

        self.__not_selected_action_wrapper = QWidget()
        self.__not_selected_action_wrapper.setLayout(QVBoxLayout())
        self.__not_selected_action_wrapper.layout().setContentsMargins(0,0,0,0)
        self.__not_selected_action_wrapper.layout().addWidget(self.__not_selected_action_filter)
        self.__not_selected_action_wrapper.layout().addWidget(self.__not_selected_action_widget)

        layout.addWidget(self.__not_selected_action_wrapper)
        layout.addWidget(self.__deselect_button)
        layout.addWidget(self.__select_button)
        layout.addWidget(self.__selected_action_widget)
        self.setLayout(layout)
        self.__refresh_not_selected_actions('')

    def __refresh_not_selected_actions(self, keyword: str):
        "called when filter changed, update not selected widget"
        all_not_selected_actions = [action for action in self.__all_actions.values() if action not in self.selected_actions()]
        # filter by object_name, tool_tip
        res: list[QAction] = []
        keywords = keyword.casefold().split() if keyword != '' else ['']
        for i in all_not_selected_actions:
            for keyword in keywords:
                if keyword in i.objectName().casefold() or keyword in i.toolTip().casefold():
                    res.append(i)
                    break

        self.__not_selected_action_widget.clear()
        res.sort(key=lambda action: (action.icon().isNull(), action.objectName())) # icon first
        for action in res:
            item = QListWidgetItem(
                action.icon(),
                action.objectName()
            )
            item.setToolTip(action.toolTip())
            self.__not_selected_action_widget.addItem(item)

    def __select_item(self):
        selected = self.__not_selected_action_widget.selectedItems()
        for select in selected:
            token_item = self.__not_selected_action_widget.takeItem(self.__not_selected_action_widget.row(select))
            self.__selected_action_widget.addItem(token_item)

    def __deselect_item(self):
        selected = self.__selected_action_widget.selectedItems()
        for select in selected:
            token_item = self.__selected_action_widget.takeItem(self.__selected_action_widget.row(select))
            self.__not_selected_action_widget.addItem(token_item)
    
    def __create_list_widget(self, actions: list[QAction]):
        res = QListWidget()
        res.setSpacing(4) # 元素间距
        # res.setWrapping(True) # 自动换行
        res.setFlow(QListWidget.TopToBottom)  # 横向排列
        res.setResizeMode(QListWidget.Adjust)  # 自动调整大小
        res.setSelectionMode(QListWidget.SingleSelection)  # 单选模式
        res.setDefaultDropAction(Qt.DropAction.MoveAction) # 拖动行为指定为Move（不然它会复制）
        res.setDragDropMode(QAbstractItemView.InternalMove) # 允许内部拖拽
        res.setIconSize(QSize(32,32)) # 指定图标大小

        for action in actions:
            item = QListWidgetItem(
                action.icon(),
                action.objectName()
            )
            item.setToolTip(action.toolTip())
            res.addItem(item)

        return res

    def selected_actions(self):
        object_names = map(lambda x: x.text(), self.__selected_action_widget.findItems('', Qt.MatchFlag.MatchStartsWith))
        return [self.__all_actions[i] for i in object_names]

def exec_editing_dialog(setting: ActionGroupConfig) -> ActionGroupConfig | None:
    dialog = QDialog(None)
    dialog.resize(1200, 800)
    dialog.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    dialog.raise_()

    horizontal_checkbox = QCheckBox()
    horizontal_checkbox.setText('Horizontal')
    horizontal_checkbox.setChecked(setting['horizontal'])

    all_actions = [i for i in Krita.instance().actions() ]
    action_dict = {i.objectName(): i for i in all_actions}

    actions_widget = ActionsEditWidget([action_dict[i] for i in setting['actions']], all_actions)

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.rejected.connect(lambda: dialog.done(0))
    button_box.accepted.connect(lambda: dialog.done(1))
    dialog.setLayout(QVBoxLayout())

    dialog.layout().addWidget(horizontal_checkbox)
    dialog.layout().addWidget(actions_widget)
    dialog.layout().addWidget(button_box)

    if dialog.exec() == 0:
        return None
    
    horizontal = horizontal_checkbox.isChecked()
    actions = actions_widget.selected_actions()
    return ActionGroupConfig(
        actions=[action.objectName() for action in actions],
        horizontal=horizontal
    )

if __name__ == '__main__':
    print(exec_editing_dialog(ActionGroupConfig(
        actions=[],
        horizontal=True,
    )))