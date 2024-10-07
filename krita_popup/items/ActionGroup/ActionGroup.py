from krita_popup.helper.QtAll import *
from krita import *
from .ActionGroupConfig import ActionGroupConfig
from .ActionGroupEditDialog import exec_editing_dialog
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



@RegistItem('Action Group')
class ActionGroup(BaseItem[ActionGroupConfig]):
    @staticmethod
    def default_configuration() -> ActionGroupConfig:
        return ActionGroupConfig(
            actions=['erase_action'],
            horizontal=True,
        )
    
    @staticmethod
    def create(conf: ActionGroupConfig, editing_mode: bool):
        return ActionGroup(conf)  # type: ignore
    
    def __init__(self, config: ActionGroupConfig) -> None:
        super().__init__()
        self.__config = config
        
        # TODO: multiple window support: get actions at `on_show` method to get current window's action
        self.__actions = [Krita.instance().action(i) for i in config['actions']]
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__button_widgets: list[QToolButton] = []
        
        self.__layout = QHBoxLayout() if config['horizontal'] else QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setSpacing(0) # remove item spacing
        self.__layout.setContentsMargins(0,0,0,0) # remove margin
        
        for action in self.__actions:
            # each tool a button
            btn_widget = self.__create_tool_button(action)
            self.__button_widgets.append(btn_widget)
            self.__layout.addWidget(btn_widget)

    def start_editing(self) -> ActionGroupConfig | None:
        return exec_editing_dialog(self.__config)

    def __create_tool_button(self, action: QAction) -> QToolButton:
        btn = QToolButton(self)
        btn.setFocusPolicy(Qt.NoFocus)
        btn.setObjectName(action.objectName())
        if action.isCheckable():
            btn.setCheckable(True)
            btn.setChecked(action.isChecked())
            action.toggled.connect(btn.setChecked) # TODO 是否需要在自己销毁时移除该连接？
            btn.toggled.connect(action.setChecked)
        else:
            btn.clicked.connect(action.trigger)
        
        btn.setStyleSheet(TOOLBUTTON_STYLE)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        btn.setToolTip(action.toolTip())
        if action.icon().isNull():
            btn.setText(action.objectName())
        else:
            btn.setIcon(action.icon())
            # when resize, set icon to my size 80%
            def set_icon_size(self, _):
                btn.setIconSize(btn.size() * 0.6)
            btn.resizeEvent = set_icon_size.__get__(btn)

        return btn
        
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
