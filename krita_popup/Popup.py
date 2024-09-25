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

def get_screen_size(widget: QWidget):
    return QApplication.screenAt(widget.pos()).size()

class Popup(QWidget):
    """
    The Real displayed popop widget, innocent to Krita for purity, use show and hide method to toggle display
    """

    def __init__(self, 
                 items: list[tuple[QWidget, QRect]],
                 /,*,
                 screen: QScreen = None,
                 under_cursor = True,
                 ) -> None:
        super().__init__(None)
        self.__items: list[tuple[QWidget, QRect]] = []
        
        self.__under_cursor = under_cursor
        self.setAttribute(Qt.WA_TranslucentBackground, True) # 透明背景，必须和无边框结合使用
        self.setWindowFlag(Qt.FramelessWindowHint, True) # 无边框
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True) # 置顶
        
        self.__mask = QRegion()
        for i in items:
            self.add_item(*i)
        if not screen:
            screen = QApplication.screenAt(self.pos())
        self.__geo = screen.geometry()
        self.show()
        self.hide()
        # TODO mask
    
    def refresh_mask(self):
        for item, _ in self.__items:
            self.__mask.intersected(item.geometry())
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

    def __to_real_geo(self, relative_geo: QRect):
        # if not self.__under_cursor:
        center = self.geometry().center()
        # else:
        #     center = QCursor.pos()
        #     print(f'{QCursor.pos()=}')
        res = QRect(relative_geo)
        res.moveTopLeft(res.topLeft() + center)
        return res
    
    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.setGeometry(self.__geo)
        for item, relative_geo in self.__items:
            item.unsetCursor()
            item.setGeometry(self.__to_real_geo(relative_geo))
        self.refresh_mask()
        return super().resizeEvent(a0)
    
    def show(self):
        # TODO setup mask
        print('show')
        if not self.__under_cursor:
            self.setGeometry(self.__geo)
        else:
            geo = QRect(self.__geo)
            geo.moveCenter(QCursor.pos())
            self.setGeometry(geo)
            
        super().show()
    def hide(self):
        print('hide')
        # TODO unset mask
        super().hide()

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



if __name__ == '__main__':
    if QApplication.instance() is None:
        app = QApplication([])
    else:
        app = None

    top = QPushButton()
    top.setText('top')
    top.clicked.connect(lambda: print('top'))
    
    bottom = QPushButton()
    bottom.setText('bottom')
    

    popup = Popup([
        (top, QRect(0,-100, 100,50)),
        (bottom, QRect(0,100, 100,50))
    ], under_cursor=True)

    manager_widget = QWidget()
    manager_widget.setWindowFlag(Qt.WindowStaysOnTopHint, True) # 置顶
    layout = QVBoxLayout(manager_widget)

    toggle_show_btn = QPushButton()
    toggle_show_btn.setText('toggle')
    def go():
        if popup.isVisible():
            popup.hide()
        else:
            popup.show()
    toggle_show_btn.clicked.connect(go)
    layout.addWidget(toggle_show_btn)
    manager_widget.show()

    

    
    # left = QPushButton()
    # left.setText('left')
    # popup.add_item(left, QRect(-200,0, 100,50))

    
    # right = QPushButton()
    # right.setText('right')
    # popup.add_item(right, QRect(200,0, 100,50))

    # popup.showMaximized()
    # print(popup.wait_for_done())
    if app is not None:
        app.exec()