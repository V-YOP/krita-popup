from typing import Literal, Optional
from PyQt5.QtCore import *
from PyQt5.QtCore import QChildEvent, Qt
from PyQt5.QtGui import QPaintEvent, QResizeEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget

class PopupItem(QWidget):
    """
    A wrapper for widgets added onto Popup, the wrapped widget's parent will be the wrapper, used for controlling interactivity and providing helpful methods.
    """
    def __init__(self, wrapped: QWidget) -> None:
        """
        identifier: should be unique
        """
        super().__init__(wrapped.parentWidget())
        self.__wrapped = wrapped
        self.__wrapped.setParent(self)
        self.__mask = QLabel(self)
        self.__mask.setMouseTracking(True)
        self.__mask.setStyleSheet("background-color: rgba(0,0,0,0);")  # 设置透明背景
        self.__mask.setGeometry(self.rect())
        self.__mask.raise_()
        self.__mask.show()

        self.__interactive = False

        # add a resizeEventFilter to synchronize size
        self.__resize_event_filter = type('', (QObject,), {})()
        def eventFilter(_, a0: QObject, a1: QEvent) -> bool:
            if a1.type() in (QEvent.Resize, QEvent.Move):
                self.__wrapped.setGeometry(self.rect())
                self.interactive = self.interactive
            return False
        self.__resize_event_filter.eventFilter = eventFilter.__get__(self.__resize_event_filter)
        self.installEventFilter(self.__resize_event_filter)

    @property
    def wrapped(self):
        return self.__wrapped
    
    @property
    def interactive(self):
        return self.__interactive
    
    @interactive.setter
    def interactive(self, v: bool):
        self.__interactive = v
        if v:
            self.__mask.setGeometry(0, 0, 0, 0)
        else:
            self.__mask.setGeometry(self.rect())
