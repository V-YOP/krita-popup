from enum import Enum
from functools import cache, partial
from typing import List, Optional
from krita import *
from . import singleton
from . import window_cache
from .QtAll import *
from . import Logger

logger = Logger()

class ToolEnum(Enum):
    INTERACTION_TOOL = ('InteractionTool', 'select', 'Select Shapes Tool', '形状选择工具')
    KARBON_CALLIGRAPHY_TOOL = ('KarbonCalligraphyTool', 'calligraphy', 'Calligraphy', '西文书法工具')
    PATH_TOOL = ('PathTool', 'shape_handling', 'Edit Shapes Tool', '锚点编辑工具：对矢量图形的锚点进行操作')
    SVG_TEXT_TOOL = ('SvgTextTool', 'draw-text', 'Text Tool', '文字工具')
    KRITA_SHAPE_KIS_TOOL_SMART_PATCH = ('KritaShape/KisToolSmartPatch', 'krita_tool_smart_patch', 'Smart Patch Tool', '智能补丁工具/仿制图章/修复画笔')
    KIS_TOOL_ENCLOSE_AND_FILL = ('KisToolEncloseAndFill', 'krita_tool_enclose_and_fill', 'Enclose and Fill Tool', '闭合填充工具/圈涂')
    KRITA_SELECTED_KIS_TOOL_COLOR_SAMPLER = ('KritaSelected/KisToolColorSampler', 'krita_tool_color_sampler', 'Sample a color from the image or current layer', '拾色器/滴管：拾取图像或当前图层颜色')
    KRITA_FILL_KIS_TOOL_FILL = ('KritaFill/KisToolFill', 'krita_tool_color_fill', 'Fill a contiguous area of color with a color, or fill a selection.', '填充工具/油漆桶：用一种颜色填充一片相连的颜色或一个选区。')
    KRITA_SHAPE_KIS_TOOL_LAZY_BRUSH = ('KritaShape/KisToolLazyBrush', 'krita_tool_lazybrush', 'Colorize Mask Tool', '智能填色蒙版工具')
    KRITA_FILL_KIS_TOOL_GRADIENT = ('KritaFill/KisToolGradient', 'krita_tool_gradient', 'Draw a gradient.', '渐变工具：拉出渐变')
    KIS_TOOL_SELECT_MAGNETIC = ('KisToolSelectMagnetic', 'tool_magnetic_selection', 'Magnetic Curve Selection Tool', '磁性曲线选区工具')
    KIS_TOOL_SELECT_CONTIGUOUS = ('KisToolSelectContiguous', 'tool_contiguous_selection', 'Contiguous Selection Tool', '相连颜色选区工具/魔棒')
    KIS_TOOL_SELECT_POLYGONAL = ('KisToolSelectPolygonal', 'tool_polygonal_selection', 'Polygonal Selection Tool', '多边形选区工具/多边形套索')
    KIS_TOOL_SELECT_ELLIPTICAL = ('KisToolSelectElliptical', 'tool_elliptical_selection', 'Elliptical Selection Tool', '椭圆选区工具')
    KIS_TOOL_SELECT_OUTLINE = ('KisToolSelectOutline', 'tool_outline_selection', 'Freehand Selection Tool', '手绘轮廓选区工具/套索')
    KIS_TOOL_SELECT_SIMILAR = ('KisToolSelectSimilar', 'tool_similar_selection', 'Similar Color Selection Tool', '相似颜色选区工具')
    KIS_TOOL_SELECT_RECTANGULAR = ('KisToolSelectRectangular', 'tool_rect_selection', 'Rectangular Selection Tool', '矩形选区工具')
    KIS_TOOL_SELECT_PATH = ('KisToolSelectPath', 'tool_path_selection', 'Bezier Curve Selection Tool', '曲线选区工具')
    KRITA_SHAPE_KIS_TOOL_RECTANGLE = ('KritaShape/KisToolRectangle', 'krita_tool_rectangle', 'Rectangle Tool', '矩形工具：可圆角')
    KIS_TOOL_POLYGON = ('KisToolPolygon', 'krita_tool_polygon', 'Polygon Tool. Shift-mouseclick ends the polygon.', '多边形工具：单击画布开始绘制，Shift+单击结束绘制。')
    KIS_TOOL_POLYLINE = ('KisToolPolyline', 'polyline', 'Polyline Tool. Shift-mouseclick ends the polyline.', '折线工具：单击画布开始绘制，Shift+单击结束绘制。')
    KRITA_SHAPE_KIS_TOOL_LINE = ('KritaShape/KisToolLine', 'krita_tool_line', 'Line Tool', '直线工具')
    KIS_TOOL_PENCIL = ('KisToolPencil', 'krita_tool_freehandvector', 'Freehand Path Tool', '手绘路径工具/自由钢笔')
    KRITA_SHAPE_KIS_TOOL_ELLIPSE = ('KritaShape/KisToolEllipse', 'krita_tool_ellipse', 'Ellipse Tool', '椭圆工具')
    KRITA_SHAPE_KIS_TOOL_DYNA = ('KritaShape/KisToolDyna', 'krita_tool_dyna', 'Dynamic Brush Tool', '力学笔刷工具')
    KRITA_SHAPE_KIS_TOOL_MULTI_BRUSH = ('KritaShape/KisToolMultiBrush', 'krita_tool_multihand', 'Multibrush Tool', '多路笔刷工具')
    KRITA_SHAPE_KIS_TOOL_BRUSH = ('KritaShape/KisToolBrush', 'krita_tool_freehand', 'Freehand Brush Tool', '手绘笔刷工具')
    KIS_TOOL_PATH = ('KisToolPath', 'krita_draw_path', 'Bezier Curve Tool. Shift-mouseclick or double-click ends the curve.', '曲线工具/钢笔：单击画布开始绘制，双击或Shift+双击结束绘制。')
    KIS_ASSISTANT_TOOL = ('KisAssistantTool', 'krita_tool_assistant', 'Assistant Tool', '辅助尺工具')
    KRITA_SHAPE_KIS_TOOL_MEASURE = ('KritaShape/KisToolMeasure', 'krita_tool_measure', 'Measure the distance between two points', '测量工具：测量两点间距离')
    TOOL_REFERENCE_IMAGES = ('ToolReferenceImages', 'krita_tool_reference_images', 'Reference Images Tool', '参考图像工具')
    ZOOM_TOOL = ('ZoomTool', 'tool_zoom', 'Zoom Tool', '缩放工具')
    PAN_TOOL = ('PanTool', 'tool_pan', 'Pan Tool', '视图平移工具/抓手')
    KIS_TOOL_CROP = ('KisToolCrop', 'tool_crop', 'Crop the image to an area', '裁剪工具：将图像裁剪至指定大小')
    KRITA_TRANSFORM_KIS_TOOL_MOVE = ('KritaTransform/KisToolMove', 'krita_tool_move', 'Move a layer', '移动图层')
    KIS_TOOL_TRANSFORM = ('KisToolTransform', 'krita_tool_transform', 'Transform a layer or a selection', '变形工具：对图层或选区进行变形')

    def __init__(self, object_name: str, icon: str, tooltip: str, cn_tooltip: str):
        self.object_name = object_name
        self.icon = icon
        self.tooltip = tooltip
        self.cn_tooltip = cn_tooltip

    @cache
    @staticmethod
    def from_object_name(object_name: str) -> 'ToolEnum':
        for enum in ToolEnum:
            if object_name == enum.object_name:
                return enum
        raise RuntimeError(f'Illegal objectName {object_name}')
    @property
    def qicon(self):
        return Krita.instance().icon(self.icon)
    
@singleton
class Toolbox(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.__notifier = Krita.instance().notifier()
        self.__notifier.setActive(True)
        self.__notifier.windowIsBeingCreated.connect(self.__add_toolbutton_click_listener)

    currentToolChanged = pyqtSignal(ToolEnum, name='currentToolChanged')
    """
    emit when current tool changed.
    parameter: ToolEnum
    """

    @window_cache
    @staticmethod
    def __get_tool_buttons(window: Window) -> List[QToolButton]:
        toolbox_docker = next((i for i in window.dockers() if i.objectName() == 'ToolBox'), None)
        if toolbox_docker is None:
            raise RuntimeError("Impossible")
        tools_obj = next((i for i in toolbox_docker.findChildren(QObject) if i.metaObject().className() == "KoToolBox"), None)
        if tools_obj is None:
            raise RuntimeError("Impossible")
        
        tool_buttons = tools_obj.findChildren(QToolButton)
        return tool_buttons
    
    def __add_toolbutton_click_listener(self, window: Window):
        name = window.qwindow().objectName()
        def go():
            window = next((i for i in Krita.instance().windows() if i.qwindow().objectName() == name), None)
            if window is None:
                raise RuntimeError("Impossible")
            
            btns = Toolbox.__get_tool_buttons(window)
            for btn in btns:
                def set_current_tool(btn: QToolButton):
                    if not btn.isChecked():
                        return
                    new_tool = ToolEnum.from_object_name(btn.objectName())
                    self.currentToolChanged.emit(new_tool)

                btn.toggled.connect(partial(set_current_tool, btn))

            # only run me once
            self.__notifier.windowIsBeingCreated.disconnect(self.__add_toolbutton_click_listener)

        QTimer.singleShot(0, go) # must wait the window created fully

    @property
    def current_tool(self) -> ToolEnum | None:
        win = Krita.instance().activeWindow()
        if win is None:
            return None
        for i in Toolbox.__get_tool_buttons(win):
            if i.isChecked():
                return ToolEnum.from_object_name(i.objectName())
        return None

    @current_tool.setter
    def current_tool(self, new_tool: ToolEnum):
        win = Krita.instance().activeWindow()
        if win is None:
            return
        tool = self.current_tool
        if tool is new_tool:
            return
        for i in Toolbox.__get_tool_buttons(win):
            if i.objectName() == new_tool.object_name:
                self.currentToolChanged.emit(new_tool)
                i.click()
                return
    
Toolbox() # 饿汉