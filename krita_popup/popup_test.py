from typing import Literal, Optional
from PyQt5.QtCore import *
from PyQt5.QtCore import QChildEvent, Qt
from PyQt5.QtGui import QPaintEvent, QResizeEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from popup import Popup


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