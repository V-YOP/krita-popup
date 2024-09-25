from typing import Literal, Optional
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from .PopupItem import PopupItem

class PopupItemGeometryHandler:
    def __init__(self) -> None:
        self.__editing_widget = None
        self.__editing_widget_original_geo: Optional[QRect] = None
        self.__editing_global_pos_start: Optional[QPoint] = None
        self.__editing_anchor: Literal['B', 'T', 'R', 'L', 'LT', 'RT', 'LB', 'RB', 'INNER', None] = None

    def handle(self, item: PopupItem, event: QEvent):    
        if event.type() in (QEvent.FocusAboutToChange,):
            item.unsetCursor()
            self.stop_editing()
            return False
        
        if event.type() in (QEvent.MouseMove, QEvent.Leave, QEvent.MouseButtonPress, QEvent.MouseButtonRelease):
            self.__handle_mouse_event(item, event)
        
    def get_editing_ahchor(self, wh: QSize, offset: QPoint, border_threshold = 15) -> Literal['B', 'T', 'R', 'L', 'LT', 'RT', 'LB', 'RB', 'INNER']:
        border_threshold = min(wh.width() // 4, wh.height() // 4, border_threshold)

        close_to_vertical_border = offset.x() <= border_threshold or abs(wh.width() - offset.x()) <= border_threshold
        close_to_horizontal_border = offset.y() <= border_threshold or abs(wh.height() - offset.y()) <= border_threshold
        
        if not close_to_horizontal_border and not close_to_vertical_border:
            return 'INNER'

        horizontal_label = 'L' if offset.x() * 2 < wh.width() else 'R'
        vertical_label = 'T' if offset.y() * 2 < wh.height() else 'B'

        if close_to_horizontal_border and not close_to_vertical_border:
            return vertical_label
        if close_to_vertical_border and not close_to_horizontal_border:
            return horizontal_label
        return f'{horizontal_label}{vertical_label}'

    def __setting_cursor(self, child_widget: QWidget, event: QMouseEvent):
        # 鼠标移动出组件时，重设光标
        if event.type() == QEvent.Leave:
            child_widget.unsetCursor()
            return 
        # 否则，设置光标
        match self.get_editing_ahchor(child_widget.size(), event.pos()):
            case 'INNER':
                cursor = Qt.ClosedHandCursor # 抓手
            case 'L' | 'R':
                cursor = Qt.SizeHorCursor # 横向调整大小
            case 'T' | 'B':
                cursor = Qt.SizeVerCursor # 纵向调整大小
            case 'LT' | 'RB':
                cursor = Qt.SizeFDiagCursor # 左上到右下对角线
            case 'RT' | 'LB':
                cursor = Qt.SizeBDiagCursor # 左上到右下对角线
            case _: raise NotImplementedError("Impossible")
        child_widget.setCursor(QCursor(cursor))

    def stop_editing(self):
        if self.__editing_widget:
            self.__editing_widget.unsetCursor()
        self.__editing_widget = None
        self.__editing_widget_original_geo = None
        self.__editing_global_pos_start = None
        self.__editing_anchor = None

    def __handle_mouse_event(self, item: PopupItem, event: QEvent):
        # 不在编辑状态时，设置光标
        if not self.__editing_widget and event.type() in (QEvent.Leave, QEvent.MouseMove):
            self.__setting_cursor(item, event)
            return
        # 无视离开事件
        if event.type() == QEvent.Leave:
            return
        
        # self.__editing_widget只是个标识，不使用，目标是为了避免编辑到其它的 widget
        if self.__editing_widget is not None and self.__editing_widget is not item:
            return

        # 如果是鼠标左键按下，设置状态，设置光标
        if event.type() == QEvent.MouseButtonPress:
            self.stop_editing()
            self.__setting_cursor(item, event)
            self.__editing_anchor = self.get_editing_ahchor(item.size(),event.pos())
            self.__editing_widget = item
            self.__editing_widget_original_geo = item.geometry()
            self.__editing_global_pos_start = event.globalPos()
            return

        if event.type() == QEvent.MouseButtonRelease:
            # 如果是鼠标抬起，重设状态，重设光标    
            item.unsetCursor()
            self.stop_editing()
            return

        offset = event.globalPos() - self.__editing_global_pos_start
        geo = QRect(self.__editing_widget_original_geo)
        # 鼠标移动事件，狠角色要来了
        # 如果是编辑位置，问题容易一些——获取当前鼠标位置相对于原位置的偏移量，并据此设置geometry
        # 编辑大小时，虽然让人感觉很虚，但是QRect里有很多方法让我不需要自己实现任何多余计算逻辑
        match self.__editing_anchor:
            case 'INNER':
                geo.moveTo(geo.x() + offset.x(), geo.y() + offset.y())
            case 'L':
                geo.setLeft(geo.left() + offset.x())
            case 'R':
                geo.setRight(geo.right() + offset.x())
            case 'T': 
                geo.setTop(geo.top() + offset.y())
            case 'B': 
                geo.setBottom(geo.bottom() + offset.y())
            case 'LT':
                geo.setTopLeft(geo.topLeft() + offset)
            case 'RT':
                geo.setTopRight(geo.topRight() + offset)
            case 'LB':
                geo.setBottomLeft(geo.bottomLeft() + offset)
            case 'RB':
                geo.setBottomRight(geo.bottomRight() + offset)
        
        item.setGeometry(geo)
