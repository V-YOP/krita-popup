from typing import Literal, Optional
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
    def __init__(self, items: list[tuple[QWidget, QRect]]) -> None:
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
        

        self.__items: list[tuple[PopupItem, QRect]] = []

        self.__item_geometry_handler = PopupItemGeometryHandler()
        for i in items:
            self.add_item(*i)

        self.showMaximized()
        self.hide()
        
    def resizeEvent(self, a0: QResizeEvent) -> None:
        for item, relative_geo in self.__items:
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
        # 获取菜单栏中的菜单项
        menu = QMenu(self)
        def delete_me():
            self.remove_item(item.wrapped)
            self.repaint()
        menu.addAction('Delete', delete_me)
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
        center = self.geometry().center()
        res = QRect(relative_geo)
        res.moveTopLeft(res.topLeft() + center)
        print(self.geometry())
        return res
    
    def __to_relative_geo(self, real_geo: QRect):
        center = self.geometry().center()
        res = QRect(real_geo)
        res.moveTopLeft(res.topLeft() - center)
        return res
    
    def add_item(self, widget: QWidget, relative_geo: QRect):
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
        self.__items.append((wrapper, relative_geo))

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

    def wait_for_done(self) -> list[tuple[QWidget, QRect]] | None:
        """
        block until popup close, return (and move) widget and relative_geometry s
        """
        self.show()
        loop = QEventLoop()
        cancel_button = QPushButton(self)
        apply_button = QPushButton(self)
        size = self.size()

        cancel_button_geo = QRect()
        cancel_button_geo.setSize(QSize(200, 60))
        cancel_button_geo.moveBottomRight(QPoint(size.width() - 600, size.height() - 100))
        cancel_button.setGeometry(cancel_button_geo)
        cancel_button.setText('Cancel')
        cancel_button.show()

        apply_button_geo = QRect()
        apply_button_geo.setSize(QSize(200, 60))
        apply_button_geo.moveBottomRight(QPoint(size.width() - 300, size.height() - 100))
        apply_button.setGeometry(apply_button_geo)
        apply_button.setText('Apply')
        apply_button.show()

        def cancel_me():
            loop.exit(1)
            cancel_button.deleteLater()
            apply_button.deleteLater()
        def apply_me():
            loop.exit(0)
            cancel_button.deleteLater()
            apply_button.deleteLater()
        cancel_button.clicked.connect(cancel_me)
        apply_button.clicked.connect(apply_me)

        ret = loop.exec()
        self.hide()
        if ret == 1:
            return None
        res = []
        for item, _ in [*self.__items]:
            relative_geo = self.__to_relative_geo(item.geometry())
            res.append((item.wrapped, relative_geo))
            self.remove_item(item.wrapped)
        return res