"""在打开文档后在Scripter中开始执行，需要避免窗口被GC"""
from typing import TypedDict, override
from PyQt5.QtGui import QCloseEvent, QResizeEvent
from krita import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QEvent, QObject, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from .BaseItem import BaseItem

class KritaDockBorrowerConfig(TypedDict):
    object_name: str


class KritaDockBorrower(QWidget, BaseItem[KritaDockBorrowerConfig]):
    """
    borrow krita's docker content
    """

    @override
    @staticmethod
    def default_configuration() -> KritaDockBorrowerConfig:
        return KritaDockBorrowerConfig(object_name='KisLayerBox')

    @override
    @staticmethod
    def create(conf: KritaDockBorrowerConfig):
        ...
    
    @override
    def start_editing(self) -> KritaDockBorrowerConfig:
        ...


    def __init__(self, dock_widget: DockWidget) -> None:
        super().__init__(None)
        ...
        self.__borrowed_widget = None
        self.__dock_widget = dock_widget
        self.__placeholder = QLabel('Borrowed')
        self.__placeholder.setObjectName('BORROWED')
        self.destroyed.connect(self.return_back)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        if not self.__borrowed_widget:
            return super().resizeEvent(a0)
        self.__borrowed_widget.setGeometry(self.rect()) # rect 方法返回 (0, 0, *self.size())
        return super().resizeEvent(a0)

    def borrow(self):
        if self.__borrowed_widget:
            return
        self.__borrowed_widget = self.__dock_widget.widget()
        self.__dock_widget.setWidget(self.__placeholder)
        self.__borrowed_widget.setParent(self)
        qInfo(f'{self.__borrowed_widget.geometry()=}')
        # self.__borrowed_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__borrowed_widget.setGeometry(self.rect())
        self.__borrowed_widget.show()
        # self.adjustSize()
        self.show()

    def return_back(self):
        if not self.__borrowed_widget:
            return
        self.__dock_widget.setWidget(self.__borrowed_widget)
        self.__borrowed_widget = None
        self.hide()

    def on_show(self):
        self.borrow()

    def on_hide(self):
        self.return_back()
        
if __name__ == '__main__':
    from krita_popup.popup import Popup
    win = Popup([], under_cursor=False)
    # QApplication.instance().win = win # 避免被GC
    dock = next(i for i in Krita.instance().dockers() if i.objectName() == 'sharedtooldocker')

    container = KritaDockBorrower(dock)
    borrow_btn = QPushButton(None)
    borrow_btn.clicked.connect(container.borrow)
    borrow_btn.setText('borrow')

    return_back_btn = QPushButton(None)
    return_back_btn.clicked.connect(container.return_back)
    return_back_btn.setText('return back')

    win.add_item(container, QRect(10, 100, 600, 300))
    win.add_item(borrow_btn, QRect(10, 10, 120, 50))
    win.add_item(return_back_btn, QRect(150, 10, 120, 50))
    win.show()