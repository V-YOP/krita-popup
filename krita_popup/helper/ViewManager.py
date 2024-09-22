from typing import NamedTuple, List
from PyQt5.QtCore import QObject
from .PerWindowCachedState import window_cache
from .Logger import Logger
from .singleton import singleton
from .QtAll import *
from krita import *

logger = Logger()

Opinion = NamedTuple('Opinion', [('view_id', int), ('qview', QMdiSubWindow), ('view', View)])

@singleton
class ViewManager(QObject):
    viewlistChanged = pyqtSignal(name="viewlistChanged")
    def __init__(self) -> None:
        super().__init__()
        self.notifier = Krita.instance().notifier()
        self.notifier.setActive(True)
        
        def refresh_view_cache():
            ViewManager.__all_view.clear()
            self.viewlistChanged.emit()

        self.notifier.windowCreated.connect(refresh_view_cache)
        self.notifier.viewClosed.connect(refresh_view_cache)
        self.notifier.viewCreated.connect(refresh_view_cache)
        self.notifier.imageCreated.connect(refresh_view_cache)

    @window_cache
    @staticmethod
    def __all_view(window: Window) -> List[Opinion]:
        views = window.views()
        if views is None:
            return []
        qviews: list[QMdiSubWindow] = window.qwindow().findChild(QMdiArea).findChildren(QMdiSubWindow)
        def get_view_id(subwin: QMdiSubWindow) -> int:
            view_widget = next((i for i in subwin.findChildren(QWidget) if i.metaObject().className() == 'KisView'), None)
            view_name = view_widget.objectName()
            return int(view_name.replace('view_', ''))
        qviews.sort(key=get_view_id)

        res = []
        for qview, view in zip(qviews, views):
            view_id = get_view_id(qview)
            res.append(Opinion(view_id, qview, view))
        return res
    
    def views(self, window: Window):
        return ViewManager.__all_view(window)
    