from typing import Callable
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QObject, QEvent, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QAction
from enum import Enum, auto


class KeyHoldState(Enum):
    PRESSED = auto()
    RELEASED_BEFORE_TIMEOUT = auto()
    PRESSED_TIMEOUT = auto()
    RELEASED_AFTER_TIMEOUT = auto()

class KeyHoldManager(QObject):
    """
    一个利用QAction去玩儿自己的鬼把戏的操作
    """
    def __init__(self, qwindow: QObject, action: QAction, callback: Callable[[KeyHoldState], None], timeout_ms: int):
        super().__init__(qwindow)

        self.action = action
        self.callback = callback
        self.timeout_ms = timeout_ms

        self._pressed = False
        self._timed_out = False

        self._shortcut = action.shortcut()

        self._timer = QTimer(self)
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._on_timeout)

        qwindow.installEventFilter(self)
        

    # ----------------------------
    # event filter
    # ----------------------------
    def eventFilter(self, obj, event):
        if event.type() in (QEvent.ShortcutOverride, QEvent.KeyPress):
            if event.isAutoRepeat():
                return False

            self._shortcut = self.action.shortcut() # 持续跟踪action的shortcut
            if self._match_shortcut(event) and not self._pressed:
                self._on_key_press()
                return True

        elif event.type() == QEvent.KeyRelease:
            if event.isAutoRepeat():
                return False

            if self._match_shortcut(event) and self._pressed:
                self._on_key_release()
                return True

        return False

    # ----------------------------
    # state transitions
    # ----------------------------
    def _on_key_press(self):
        self._pressed = True
        self._timed_out = False

        self._timer.start(self.timeout_ms)
        self.callback(KeyHoldState.PRESSED)

    def _on_timeout(self):
        if not self._pressed:
            return

        self._timed_out = True
        self.callback(KeyHoldState.PRESSED_TIMEOUT)

    def _on_key_release(self):
        self._timer.stop()

        if self._timed_out:
            self.callback(KeyHoldState.RELEASED_AFTER_TIMEOUT)
        else:
            self.callback(KeyHoldState.RELEASED_BEFORE_TIMEOUT)

        self._pressed = False
        self._timed_out = False

    # ----------------------------
    # shortcut matching
    # ----------------------------
    def _match_shortcut(self, event):
        seq = QKeySequence(event.modifiers() | event.key())
        return self._shortcut.matches(seq) == QKeySequence.ExactMatch
