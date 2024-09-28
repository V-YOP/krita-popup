from typing import Iterable, Literal, Optional
from PyQt5.QtCore import *
from PyQt5.QtCore import QChildEvent, Qt
from PyQt5.QtGui import QPaintEvent, QResizeEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from .CrossOverlay import CrossOverlay
from .PopupItem import PopupItem
from .PopupItemGeometryHandler import PopupItemGeometryHandler

class EditingPopup(QWidget):
    """
    The editing popup
    """
    def __init__(self, items: list[tuple[QWidget, QRect, list[tuple[str, QAction]]]]) -> None:
        super().__init__(None)
        self.setAttribute(Qt.WA_TranslucentBackground, True) # 透明背景，必须和无边框结合使用
        self.setWindowFlag(Qt.FramelessWindowHint, True) # 无边框
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True) # 置顶

        # delegate item's event to me
        self.__delegate_event_filter = type('', (QObject,), {})(self)
        def delegate_event_filter_fn(_, widget, event):
            self.__on_item_event(widget, event)
            return False
        self.__delegate_event_filter.eventFilter = delegate_event_filter_fn.__get__(self.__delegate_event_filter)

        # resize cross_line when my size changed
        self.__cross_line = CrossOverlay(self)
        self.__resize_cross_line_event_filter = type('', (QObject,), {})(self)
        def resize_event_filter_fn(_, widget, event):
            self.__cross_line.setGeometry(self.rect())
            return False
        self.__cross_line.setVisible(True) 
        
        self.__resize_cross_line_event_filter.eventFilter = resize_event_filter_fn.__get__(self.__resize_cross_line_event_filter)
        self.installEventFilter(self.__resize_cross_line_event_filter)
        

        self.__items: list[tuple[PopupItem, QRect, list[QAction]]] = []

        self.__item_geometry_handler = PopupItemGeometryHandler()
        for i in items:
            self.add_item(*i)

        self.showMaximized()
        self.hide()
        
    def resizeEvent(self, a0: QResizeEvent) -> None:
        for item, relative_geo, _ in self.__items:
            item.unsetCursor()
            item.setGeometry(self.__to_real_geo(relative_geo))
        return super().resizeEvent(a0)
        
    def paintEvent(self, a0: QPaintEvent) -> None:
        """
        paint a half transparent background for editing mode
        """
        p = QPainter(self)
        p.setPen(QColor(0,0,0,0))
        p.setBrush(QColor(33, 33, 33, 150))
        p.drawRect(self.rect())
        p.end()

    def __popup_item_menu(self, item: PopupItem):
        _, _, actions = next(i for i in self.__items if i[0] is item)
        # 获取菜单栏中的菜单项
        menu = QMenu(self)
        for action in actions:
            menu.addAction(action)
        menu.exec_(item.mapToGlobal(item.rect().topRight()))

    def __on_item_event(self, item: PopupItem, event: QEvent):
        # 如果是右键按下，唤起上下文菜单
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.RightButton:
            self.__popup_item_menu(item)
            return
        
        # 无视鼠标左键以外的键按下和抬起
        if not (event.type() in (QEvent.MouseButtonPress, QEvent.MouseButtonRelease) and event.button() != Qt.LeftButton):
            self.__item_geometry_handler.handle(item, event)
            return
        
    def __to_real_geo(self, relative_geo: QRect):
        center = self.rect().center()
        res = QRect(relative_geo)
        res.moveTopLeft(res.topLeft() + center)
        print(self.geometry())
        return res
    
    def relative_geometry(self, widget: QWidget):
        """
        Get a widget's relative geometry to screen center
        """
        for wrapper, *_ in self.__items:
            if wrapper.wrapped is widget:
                return self.__to_relative_geo(wrapper.geometry())
        raise RuntimeError('widget not in popup')

    def __to_relative_geo(self, real_geo: QRect):
        center = self.rect().center()
        res = QRect(real_geo)
        res.moveTopLeft(res.topLeft() - center)
        return res
    
    def add_item(self, widget: QWidget, relative_geo: QRect, actions: Iterable[QAction] = ()):
        """
        Add a widget to me
        """
        wrapper = PopupItem(widget)
        wrapper.setMouseTracking(True)
        wrapper.setParent(self)
        self.__cross_line.raise_()
        wrapper.installEventFilter(self.__delegate_event_filter)
        wrapper.interactive = False
        wrapper.setGeometry(self.__to_real_geo(relative_geo))
        wrapper.show()
        self.__items.append((wrapper, relative_geo, list(actions)))

    def remove_item(self, widget: QWidget):
        """
        Remove a widget from me
        """
        wrapper = next((i for i in self.__items if i[0].wrapped is widget), None)
        if wrapper:
            self.__items.remove(wrapper)
            wrapper[0].removeEventFilter(self.__delegate_event_filter)
            wrapper[0].setParent(None)
            wrapper[0].deleteLater()
            return wrapper[0].wrapped
        
    def clear_items(self):
        for wrapper, _, _ in self.__items:
            wrapper.removeEventFilter(self.__delegate_event_filter)
            wrapper.setParent(None)
            wrapper.deleteLater()
        self.__items[:] = []

    def items(self):
        """
        return widget and real relative_geo pairs
        """
        return [(i.wrapped, self.__to_relative_geo(i.geometry())) for i, _ in self.__items]
    
    def show(self):
        for item, *_ in self.__items:
            if hasattr(item.wrapped, 'on_show'):
                getattr(item.wrapped, 'on_show')()
        super().show()
    def hide(self):
        for item, *_ in self.__items:
            if hasattr(item.wrapped, 'on_hide'):
                getattr(item.wrapped, 'on_hide')()
        super().hide()