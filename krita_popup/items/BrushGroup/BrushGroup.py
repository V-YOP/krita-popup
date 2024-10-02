
from typing import TypedDict

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QWidget
from krita import *
from krita_popup.helper import ViewState
from .._item_gegistry import RegistItem
from ..BaseItem import BaseItem
from .BrushGroupConfig import BrushGroupConfig
from krita_popup.helper.QtAll import *
from .BrushGroupDialog import exec_editing_dialog

TOOLBUTTON_STYLE = """
QToolButton {
    width: 32px;
    height: 32px;
    background-color: #31363b;
}
QToolButton:checked {
    background-color: #647c91;
}
""".strip()


@RegistItem('Brush Group')
class BrushGroup(BaseItem[BrushGroupConfig]):
    @staticmethod
    def default_configuration() -> BrushGroupConfig:
        return BrushGroupConfig(
            brushes=[Krita.instance().krita_i18nc('./krita/data/paintoppresets/a)_Eraser_Circle.kpp', 'a) Eraser Circle')],
            horizontal=True,
        )
    
    @staticmethod
    def create(conf: BrushGroupConfig):
        return BrushGroup(conf)  # type: ignore
    
    def start_editing(self) -> BrushGroupConfig | None:
        return exec_editing_dialog(self.__config)

    def __init__(self, config: BrushGroupConfig) -> None:
        super().__init__(None)
        self.__view_state = ViewState()
        self.__config = config
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.__button_widgets: list[QToolButton] = []
        self.__resources: list[Resource] = []

        self.__layout = QHBoxLayout() if config['horizontal'] else QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setSpacing(0) # remove item spacing
        self.__layout.setContentsMargins(0,0,0,0) # remove margin
        
        resources = Krita.instance().resources('preset')
        for resource_name in config['brushes']:
            if resource_name in resources:
                btn = self.__create_tool_button(resources[resource_name])
                self.__resources.append(resources[resource_name])
                self.__button_widgets.append(btn)
                self.__layout.addWidget(btn)
    def brush_changed(self, current_resource: Resource):
        for resource, btn in zip(self.__resources, self.__button_widgets):
            if current_resource.name() == resource.name():
                btn.setChecked(True)
            else:
                btn.setChecked(False)

    def on_show(self):
        self.__view_state.currentBrushChanged.connect(self.brush_changed)
        if current := self.__view_state.current_brush:
            self.brush_changed(current)
        return super().on_show()

    def on_hide(self):
        self.__view_state.currentBrushChanged.disconnect(self.brush_changed)
        return super().on_show()

    def set_pixmap_transparency(self, pixmap: QPixmap, alpha: float):
        image = pixmap.toImage()
        for y in range(image.height()):
            for x in range(image.width()):
                pixel = image.pixelColor(x, y)
                pixel.setAlpha(int(pixel.alpha() * alpha))
                image.setPixelColor(x, y, pixel)
        return QPixmap.fromImage(image)

    def __create_tool_button(self, resource: Resource) -> QToolButton:
        btn = QToolButton(self)
        btn.setFocusPolicy(Qt.NoFocus)
        btn.setCheckable(True)
        btn.setStyleSheet(TOOLBUTTON_STYLE)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        btn.setIcon(QIcon(QPixmap.fromImage(resource.image())))
        # when resize, set icon to my size 80%
        def set_icon_size(self, _):
            btn.setIconSize(btn.size())
        btn.setMaximumSize(2000,2000)
        btn.resizeEvent = set_icon_size.__get__(btn)
        btn.setToolTip(resource.name())

        old_paint_event = btn.paintEvent
        def new_paint_event(self, event):
            old_paint_event(event)
            if self.isChecked():
                painter = QPainter(self)
                painter.setRenderHint(QPainter.Antialiasing)
                
                # 设置遮罩颜色，带有透明度的黑色 (50%透明)
                color = QColor('#7affff')
                color.setAlpha(128)
                transparent_color = color
                painter.setBrush(transparent_color)
                painter.setPen(Qt.NoPen)
                
                # 绘制一个与按钮大小相同的半透明矩形遮罩
                painter.drawRect(self.rect())
        btn.paintEvent = new_paint_event.__get__(btn)

        def onclick(_, __):
            self.__view_state.current_brush = resource
        btn.mousePressEvent = onclick.__get__(btn)
        return btn
        
    # def on_tool_changed(self, new_tool: ToolEnum):
    #     """
    #     when tool changed, reset checked status
    #     """
    #     for tool, button in zip(self.__tools, self.__button_widgets):
    #         button.setChecked(tool == new_tool)
    