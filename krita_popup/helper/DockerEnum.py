
from enum import Enum
from functools import cache

from krita import Window

class DockerEnum(Enum):
    ANIMATION_CURVES = ('AnimationCurvesDocker', '动画曲线', 'Animation Curves')
    ARRANGE = ('ArrangeDocker', '矢量图形排列控制', 'Arrange')
    ARTISTIC_COLOR_SELECTOR = ('ArtisticColorSelector', '美术拾色器', 'Artistic Color Selector')
    CHANNELS = ('ChannelDocker', '通道', 'Channels')
    ADVANCED_COLOR_SELECTOR = ('ColorSelectorNg', '多功能拾色器', 'Advanced Color Selector')
    COMPOSITIONS = ('CompositionDocker', '图层显示方案', 'Compositions')
    DIGITAL_COLORS_MIXER = ('DigitalMixer', '过渡色调混合器', 'Digital Colors Mixer')
    GAMUT_MASKS = ('GamutMask', '色域蒙版', 'Gamut Masks')
    GRID_AND_GUIDES = ('GridDocker', '网格与参考线', 'Grid and Guides')
    HISTOGRAM = ('HistogramDocker', '直方图', 'Histogram')
    UNDO_HISTORY = ('History', '撤销历史', 'Undo History')
    LAYERS = ('KisLayerBox', '图层', 'Layers')
    LOG_VIEWER = ('LogDocker', '日志查看器', 'Log Viewer')
    LUT_MANAGEMENT = ('LutDocker', 'LUT 色彩管理', 'LUT Management')
    ONION_SKINS = ('OnionSkinsDocker', '绘图纸外观', 'Onion Skins')
    OVERVIEW = ('OverviewDocker', '导航器 = 总览图', 'Overview')
    PALETTE = ('PaletteDocker', '色板', 'Palette')
    PATTERNS = ('PatternDocker', '图案', 'Patterns')
    BRUSH_PRESETS = ('PresetDocker', '笔刷预设', 'Brush Presets')
    BRUSH_PRESET_HISTORY = ('PresetHistory', '笔刷预设历史', 'Brush Preset History')
    RECORDER = ('RecorderDocker', '录像工具', 'Recorder')
    SMALL_COLOR_SELECTOR = ('SmallColorSelector', '小型拾色器', 'Small Color Selector')
    SNAPSHOT_DOCKER = ('Snapshot', '图像版本快照', 'Snapshot Docker')
    SPECIFIC_COLOR_SELECTOR = ('SpecificColorSelector', '量化拾色器', 'Specific Color Selector')
    STORYBOARD = ('StoryboardDocker', '分镜头脚本', 'Storyboard')
    SYMBOL_LIBRARIES = ('SvgSymbolCollectionDocker', '符号图库', 'Symbol Libraries')
    TASK_SETS = ('TasksetDocker', '操作流程', 'Task Sets')
    ANIMATION_TIMELINE = ('TimelineDocker', '动画时间轴', 'Animation Timeline')
    TOOLBOX = ('ToolBox', '工具箱', 'Toolbox')
    TOUCH_DOCKER = ('TouchDocker', '触摸屏辅助按钮', 'Touch Docker')
    WIDE_GAMUT_COLOR_SELECTOR = ('WideGamutColorSelector', '宽色域拾色器', 'Wide Gamut Color Selector')
    COMICS_MANAGER = ('comics_project_manager_docker', '漫画项目管理', 'Comics Manager')
    LAST_DOCUMENTS_DOCKER = ('lastdocumentsdocker', '最近图像列表', 'Last Documents Docker')
    QUICK_SETTINGS_DOCKER = ('quick_settings_docker', '笔刷常用数值一键切换面板', 'Quick Settings Docker')
    TOOL_OPTIONS = ('sharedtooldocker', '工具选项', 'Tool Options')

    def __init__(self, object_name: str, cn_name: str, en_name: str):
        self.object_name = object_name
        self.cn_name = cn_name
        self.en_name = en_name

    @cache
    @staticmethod
    def from_object_name(object_name: str):
        for enum in DockerEnum:
            if object_name == enum.object_name:
                return enum
        return None
    
    def widget(self, window: Window):
        for docker in window.dockers():
            if docker.objectName() == self.object_name:
                return docker
        raise NotImplementedError('Impossible')