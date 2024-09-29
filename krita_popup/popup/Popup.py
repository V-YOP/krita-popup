from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFocusEvent, QResizeEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from .PopupItem import PopupItem

class Popup(QWidget):
    """
    The Real displayed popop widget, innocent to Krita for purity, use show and hide method to toggle display.

    will check if item has method `on_show` and `on_hide`, which will be invokd without arguments if exists.

    custom mask for items is supported, just create method `custom_mask` which returns the mask
    """

    def __init__(self, 
                 items: list[tuple[QWidget, QRect]],
                 /,*,
                 under_cursor = True,
                 ) -> None:
        super().__init__(None)
        self.__items: list[tuple[PopupItem, QRect]] = []
        
        self.__under_cursor = under_cursor
        
        self.setAttribute(Qt.WA_TranslucentBackground, True) # 透明背景，必须和无边框结合使用
        self.setWindowFlag(Qt.FramelessWindowHint, True) # 无边框
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True) # 置顶

        self.__mask = QRegion()
        for i in items:
            self.add_item(*i)
        # if not screen:
        screen = QApplication.screenAt(self.pos())
        self.__geo = screen.geometry()
        print(f'{self.__geo=}')
        self.show()
        self.hide()
        self.refresh_mask()
    
    def refresh_mask(self):
        self.__mask = QRegion()
        for item, _ in self.__items:
            if hasattr(item.wrapped, 'custom_mask') and (res := item.wrapped.custom_mask()) is not NotImplemented and res is not None:
                region: QRegion = res
                region.translate(item.pos())
                self.__mask = self.__mask.united(region)
            else:
                self.__mask = self.__mask.united(item.geometry())
        self.setMask(self.__mask)

    def add_item(self, widget: QWidget, relative_geo: QRect):
        """
        Add a widget to me
        """
        wrapper = PopupItem(widget)
        wrapper.setParent(self)
        wrapper.interactive = True
        wrapper.setGeometry(self.__to_real_geo(relative_geo))
        wrapper.show()
        self.__items.append((wrapper, relative_geo))
        self.refresh_mask()

    def clear_items(self):
        for wrapper, _ in self.__items:
            wrapper.setParent(None)
            wrapper.deleteLater()
        self.__items[:] = []
        self.refresh_mask()

    def __to_real_geo(self, relative_geo: QRect):
        # if not self.__under_cursor:
        center = self.rect().center()
        # else:
        #     center = QCursor.pos()
        #     print(f'{QCursor.pos()=}')
        res = QRect(relative_geo)
        res.moveTopLeft(res.topLeft() + center)
        return res
    
    def focusOutEvent(self, a0: QFocusEvent) -> None:
        print('focusOutEvent')
        self.hide()
        return super().focusOutEvent(a0)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.setGeometry(self.__geo)
        for item, relative_geo in self.__items:
            item.unsetCursor()
            item.setGeometry(self.__to_real_geo(relative_geo))
        self.refresh_mask()
        return super().resizeEvent(a0)
    
    def show(self):
        if not self.__under_cursor:
            self.setGeometry(self.__geo)
        else:
            geo = QRect(self.__geo)
            geo.moveCenter(QCursor.pos())
            self.setGeometry(geo)
        for item, _ in self.__items:
            if hasattr(item.wrapped, 'on_show'):
                getattr(item.wrapped, 'on_show')()
        super().show()
        print(f'{self.geometry()=}')
    def hide(self):
        for item, _ in self.__items:
            if hasattr(item.wrapped, 'on_hide'):
                getattr(item.wrapped, 'on_hide')()
        super().hide()
