
from typing import TypedDict

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from krita import *

from ._item_gegistry import RegistItem
from .BaseItem import BaseItem
from krita_popup.helper.QtAll import *
from krita_popup.helper.util import get_window_from_object_name

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

class MainMenuButtonConfig(TypedDict):
    pass

@RegistItem('Krita Menu Button')
class KritaMenuButton(BaseItem[MainMenuButtonConfig]):
    @staticmethod
    def default_configuration() -> MainMenuButtonConfig:
        return MainMenuButtonConfig()
    
    @staticmethod
    def create(conf: MainMenuButtonConfig, window: Window, editing_mode: bool):
        return KritaMenuButton(window)
    
    def start_editing(self) -> MainMenuButtonConfig | None:
        # no editing
        return None
    
    def __init__(self, window: Window) -> None:
        super().__init__(None)
        self.__window_object_name = window.objectName()

        self.setLayout(QHBoxLayout())
        self.__button = QPushButton()
        self.layout().addWidget(self.__button)

        self.__button.setFocusPolicy(Qt.NoFocus)
        self.__button.setCheckable(True)
        self.__button.setStyleSheet(TOOLBUTTON_STYLE)
        self.__button.setIcon(Krita.instance().icon('properties'))
        self.__button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        def set_icon_size(__, _):
            self.__button.setIconSize(self.__button.size() * 0.8)
        self.__button.resizeEvent = set_icon_size.__get__(self.__button)
        self.__button.clicked.connect(self.show_menu_on_click)

    def show_menu_on_click(self):
        # 获取菜单栏中的菜单项
        menu = QMenu(self)
        # 获取顶级菜单栏中的菜单
        for action in get_window_from_object_name(self.__window_object_name).qwindow().menuBar().actions():
            submenu = action.menu()
            if submenu:
                # 将顶级菜单栏的菜单添加到按钮点击菜单
                menu.addMenu(submenu)
        self.__button.setChecked(True)
        # 显示菜单，位置在按钮的右上角
        menu.exec_(self.__button.mapToGlobal(self.__button.rect().topRight()))
        self.__button.setChecked(False)
