from typing import Literal, Optional
from PyQt5.QtCore import *
from PyQt5.QtCore import QChildEvent, Qt
from PyQt5.QtGui import QPaintEvent, QResizeEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget

class CrossOverlay(QWidget):
    """
    A crossline widget for indicating
    """
    def __init__(self, parent=None, radius=20):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # 让鼠标事件穿透该组件
        self.setAttribute(Qt.WA_NoSystemBackground)  # 禁止系统背景绘制
        self.setStyleSheet("background: transparent;")  # 设置背景透明
        self.raise_()  # 将这个覆盖层放到顶层
        self.__radius = radius

    def paintEvent(self, event):
        # 绘制十字在顶层组件上
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(Qt.black, 6)
        painter.setPen(pen)

        rect = self.rect()
        center = rect.center()

        # 绘制水平线
        painter.drawLine(QPoint(center.x() - self.__radius, center.y()), QPoint(center.x() + self.__radius, center.y()))
        # 绘制垂直线
        painter.drawLine(QPoint(center.x(), center.y() - self.__radius), QPoint(center.x(), center.y() + self.__radius))

        pen = QPen(Qt.white, 2)
        painter.setPen(pen)

        rect = self.rect()
        center = rect.center()

        # 绘制水平线
        painter.drawLine(QPoint(center.x() - self.__radius, center.y()), QPoint(center.x() + self.__radius, center.y()))

        # 绘制垂直线
        painter.drawLine(QPoint(center.x(), center.y() - self.__radius), QPoint(center.x(), center.y() + self.__radius))


        painter.end()
