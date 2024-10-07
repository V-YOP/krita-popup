

from collections.abc import Iterator
from enum import Enum
from operator import attrgetter


class BlendingMode(Enum):
    PLUS                            = ('plus', 'Arithmetic', '数学运算', 'Addition', '相加 = 线性减淡 = 添加')
    DIVIDE                          = ('divide', 'Arithmetic', '数学运算', 'Divide', '划分 = 除去')
    INVERSE_SUBTRACT                = ('inverse_subtract', 'Arithmetic', '数学运算', 'Inverse Subtract', '减去反相值')
    MULTIPLY                        = ('multiply', 'Arithmetic', '数学运算', 'Multiply', '正片叠底 = 相乘')
    SUBTRACT                        = ('subtract', 'Arithmetic', '数学运算', 'Subtract', '减去')

    XOR                             = ('xor', 'Binary', '二元逻辑', 'XOR', 'XOR - 异或')
    OR                              = ('or', 'Binary', '二元逻辑', 'OR', 'OR - 或')
    AND                             = ('and', 'Binary', '二元逻辑', 'AND', 'AND - 与')
    NAND                            = ('nand', 'Binary', '二元逻辑', 'NAND', 'NAND - 与非')
    NOR                             = ('nor', 'Binary', '二元逻辑', 'NOR', 'NOR - 或非')
    XNOR                            = ('xnor', 'Binary', '二元逻辑', 'XNOR', 'XNOR - 双条件')
    IMPLICATION                     = ('implication', 'Binary', '二元逻辑', 'IMPLICATION', 'IMPLICATION - 蕴含')
    NOT_IMPLICATION                 = ('not_implication', 'Binary', '二元逻辑', 'NOT IMPLICATION', 'NOT IMPLICATION - 非蕴含')
    CONVERSE                        = ('converse', 'Binary', '二元逻辑', 'CONVERSE', 'CONVERSE - 反蕴含')
    NOT_CONVERSE                    = ('not_converse', 'Binary', '二元逻辑', 'NOT CONVERSE', 'NOT CONVERSE - 反非蕴含')

    BURN                            = ('burn', 'Darken', '变暗', 'Burn', '颜色加深 = 加深')
    LINEAR_BURN                     = ('linear_burn', 'Darken', '变暗', 'Linear Burn', '线性加深')
    DARKEN                          = ('darken', 'Darken', '变暗', 'Darken', '变暗')
    GAMMA_DARK                      = ('gamma_dark', 'Darken', '变暗', 'Gamma Dark', '伽玛值变暗')
    DARKER_COLOR                    = ('darker color', 'Darken', '变暗', 'Darker Color', '深色 = 取较深色')
    SHADE_IFS_ILLUSIONS             = ('shade_ifs_illusions', 'Darken', '变暗', 'Shade (IFS Illusions)', '阴影 (IFS Illusions)')
    FOG_DARKEN_IFS_ILLUSIONS        = ('fog_darken_ifs_illusions', 'Darken', '变暗', 'Fog Darken (IFS Illusions)', '雾状变暗 (IFS Illusions)')
    EASY_BURN                       = ('easy burn', 'Darken', '变暗', 'Easy Burn', '平缓加深')

    DODGE                           = ('dodge', 'Lighten', '变亮', 'Color Dodge', '颜色减淡')
    ADD                             = ('add', 'Lighten', '变亮', 'Linear Dodge', '线性减淡 = 添加 = 相加')
    LIGHTEN                         = ('lighten', 'Lighten', '变亮', 'Lighten', '变亮')
    LINEAR_LIGHT                    = ('linear light', 'Lighten', '变亮', 'Linear Light', '线性光 = 图章')
    SCREEN                          = ('screen', 'Lighten', '变亮', 'Screen', '滤色')
    PIN_LIGHT                       = ('pin_light', 'Lighten', '变亮', 'Pin Light', '点光')
    VIVID_LIGHT                     = ('vivid_light', 'Lighten', '变亮', 'Vivid Light', '亮光')
    FLAT_LIGHT                      = ('flat_light', 'Lighten', '变亮', 'Flat Light', '平光')
    HARD_LIGHT                      = ('hard_light', 'Lighten', '变亮', 'Hard Light', '强光')
    SOFT_LIGHT_IFS_ILLUSIONS        = ('soft_light_ifs_illusions', 'Lighten', '变亮', 'Soft Light (IFS Illusions)', '柔光 (IFS Illusions)')
    SOFT_LIGHT_PEGTOP_DELPHI        = ('soft_light_pegtop_delphi', 'Lighten', '变亮', 'Soft Light (Pegtop-Delphi)', '柔光 (Pegtop-Delphi) = 模糊光')
    SOFT_LIGHT                      = ('soft_light', 'Lighten', '变亮', 'Soft Light (Photoshop)', '柔光 (Photoshop)')
    SOFT_LIGHT_SVG                  = ('soft_light_svg', 'Lighten', '变亮', 'Soft Light (SVG)', '柔光 (SVG)')
    GAMMA_LIGHT                     = ('gamma_light', 'Lighten', '变亮', 'Gamma Light', '伽玛值变亮')
    GAMMA_ILLUMINATION              = ('gamma_illumination', 'Lighten', '变亮', 'Gamma Illumination', '伽玛值照明')
    LIGHTER_COLOR                   = ('lighter color', 'Lighten', '变亮', 'Lighter Color', '浅色 = 取较浅色')
    PNORM_A                         = ('pnorm_a', 'Lighten', '变亮', 'P-Norm A', 'P-范数 A')
    PNORM_B                         = ('pnorm_b', 'Lighten', '变亮', 'P-Norm B', 'P-范数 B')
    SUPER_LIGHT                     = ('super_light', 'Lighten', '变亮', 'Super Light', '超强光')
    TINT_IFS_ILLUSIONS              = ('tint_ifs_illusions', 'Lighten', '变亮', 'Tint (IFS Illusions)', '高光 (IFS Illusions)')
    FOG_LIGHTEN_IFS_ILLUSIONS       = ('fog_lighten_ifs_illusions', 'Lighten', '变亮', 'Fog Lighten (IFS Illusions)', '雾状变亮 (IFS Illusions)')
    EASY_DODGE                      = ('easy dodge', 'Lighten', '变亮', 'Easy Dodge', '平缓减淡')
    LUMINOSITY_SAI                  = ('luminosity_sai', 'Lighten', '变亮', 'Luminosity/Shine (SAI)', '发光 (SAI)')

    MODULO                          = ('modulo', 'Modulo', '取模运算', 'Modulo', '取模运算')
    MODULO_CONTINUOUS               = ('modulo_continuous', 'Modulo', '取模运算', 'Modulo - Continuous', '取模运算 - 连续')
    DIVISIVE_MODULO                 = ('divisive_modulo', 'Modulo', '取模运算', 'Divisive Modulo', '取余运算')
    DIVISIVE_MODULO_CONTINUOUS      = ('divisive_modulo_continuous', 'Modulo', '取模运算', 'Divisive Modulo - Continuous', '取余运算 - 连续')
    MODULO_SHIFT                    = ('modulo_shift', 'Modulo', '取模运算', 'Modulo Shift', '取模运算偏移')
    MODULO_SHIFT_CONTINUOUS         = ('modulo_shift_continuous', 'Modulo', '取模运算', 'Modulo Shift - Continuous', '取模运算偏移 - 连续')

    DIFF                            = ('diff', 'Negative', '负片', 'Difference', '差值')
    EQUIVALENCE                     = ('equivalence', 'Negative', '负片', 'Equivalence', '等效值')
    ADDITIVE_SUBTRACTIVE            = ('additive_subtractive', 'Negative', '负片', 'Additive Subtractive', '减去平方根')
    EXCLUSION                       = ('exclusion', 'Negative', '负片', 'Exclusion', '排除')
    ARC_TANGENT                     = ('arc_tangent', 'Negative', '负片', 'Arcus Tangent', '反正切值')
    NEGATION                        = ('negation', 'Negative', '负片', 'Negation', '取反')

    NORMAL                          = ('normal', 'Mix', '颜色混合', 'Normal', '正常')
    BEHIND                          = ('behind', 'Mix', '颜色混合', 'Behind', '背后')
    GREATER                         = ('greater', 'Mix', '颜色混合', 'Greater', '覆盖较不透明色')
    OVERLAY                         = ('overlay', 'Mix', '颜色混合', 'Overlay', '叠加')
    LAMBERT_LIGHTING                = ('lambert_lighting', 'Mix', '颜色混合', 'Lambert Lighting (Linear)', 'Lambert 光照 (线性)')
    LAMBERT_LIGHTING_GAMMA2_2       = ('lambert_lighting_gamma2.2', 'Mix', '颜色混合', 'Lambert Lighting (Gamma 2.2)', 'Lambert 光照 (伽玛值 2.2)')
    ERASE                           = ('erase', 'Mix', '颜色混合', 'Erase', '擦除')
    ALPHADARKEN                     = ('alphadarken', 'Mix', '颜色混合', 'Alpha Darken', '透明度变暗')
    HARD_MIX                        = ('hard mix', 'Mix', '颜色混合', 'Hard Mix', '实色混合')
    HARD_MIX_PHOTOSHOP              = ('hard_mix_photoshop', 'Mix', '颜色混合', 'Hard Mix (Photoshop)', '实色混合 (Photoshop)')
    HARD_MIX_SOFTER_PHOTOSHOP       = ('hard_mix_softer_photoshop', 'Mix', '颜色混合', 'Hard Mix Softer (Photoshop)', '实色混合柔和 (Photoshop)')
    GRAIN_MERGE                     = ('grain_merge', 'Mix', '颜色混合', 'Grain Merge', '颗粒合并 (相加变深)')
    GRAIN_EXTRACT                   = ('grain_extract', 'Mix', '颜色混合', 'Grain Extract', '颗粒抽取 (减去变浅)')
    PARALLEL                        = ('parallel', 'Mix', '颜色混合', 'Parallel', '平行')
    ALLANON                         = ('allanon', 'Mix', '颜色混合', 'Allanon', '相加减半')
    GEOMETRIC_MEAN                  = ('geometric_mean', 'Mix', '颜色混合', 'Geometric Mean', '几何平均')
    DESTINATION_ATOP                = ('destination-atop', 'Mix', '颜色混合', 'Destination Atop', '目标顶部')
    DESTINATION_IN                  = ('destination-in', 'Mix', '颜色混合', 'Destination In', '目标内部')
    HARD_OVERLAY                    = ('hard overlay', 'Mix', '颜色混合', 'Hard Overlay', '强光叠加')
    INTERPOLATION                   = ('interpolation', 'Mix', '颜色混合', 'Interpolation', '插值')
    INTERPOLATION_2X                = ('interpolation 2x', 'Mix', '颜色混合', 'Interpolation - 2X', '插值 - 二次')
    PENUMBRA_A                      = ('penumbra a', 'Mix', '颜色混合', 'Penumbra A', '半影 A = 柔和减淡')
    PENUMBRA_B                      = ('penumbra b', 'Mix', '颜色混合', 'Penumbra B', '半影 B = 柔和加深')
    PENUMBRA_C                      = ('penumbra c', 'Mix', '颜色混合', 'Penumbra C', '半影 C')
    PENUMBRA_D                      = ('penumbra d', 'Mix', '颜色混合', 'Penumbra D', '半影 D')

    BUMPMAP                         = ('bumpmap', 'Misc', '其他', 'Bumpmap', '凹凸贴图')
    COMBINE_NORMAL                  = ('combine_normal', 'Misc', '其他', 'Combine Normal Map', '合并法线贴图')
    DISSOLVE                        = ('dissolve', 'Misc', '其他', 'Dissolve', '溶解')
    COPY_RED                        = ('copy_red', 'Misc', '其他', 'Copy Red', '复制红通道')
    COPY_GREEN                      = ('copy_green', 'Misc', '其他', 'Copy Green', '复制绿通道')
    COPY_BLUE                       = ('copy_blue', 'Misc', '其他', 'Copy Blue', '复制蓝通道')
    COPY                            = ('copy', 'Misc', '其他', 'Copy', '复制')
    TANGENT_NORMALMAP               = ('tangent_normalmap', 'Misc', '其他', 'Tangent Normalmap', '切线空间法线贴图')

    COLOR                           = ('color', 'HSY', 'HSY 颜色调整', 'Color', '颜色')
    HUE                             = ('hue', 'HSY', 'HSY 颜色调整', 'Hue', '色相')
    SATURATION                      = ('saturation', 'HSY', 'HSY 颜色调整', 'Saturation', '饱和度')
    LUMINOSITY                      = ('luminosity', 'HSY', 'HSY 颜色调整', 'Luminosity', '明度')
    DEC_SATURATION                  = ('dec_saturation', 'HSY', 'HSY 颜色调整', 'Decrease Saturation', '降低饱和度')
    INC_SATURATION                  = ('inc_saturation', 'HSY', 'HSY 颜色调整', 'Increase Saturation', '提高饱和度')
    DEC_LUMINOSITY                  = ('dec_luminosity', 'HSY', 'HSY 颜色调整', 'Decrease Luminosity', '降低明度')
    INC_LUMINOSITY                  = ('inc_luminosity', 'HSY', 'HSY 颜色调整', 'Increase Luminosity', '提高明度')

    COLOR_HSI                       = ('color_hsi', 'HSI', 'HSI 颜色调整', 'Color HSI', '颜色 (HSI)')
    HUE_HSI                         = ('hue_hsi', 'HSI', 'HSI 颜色调整', 'Hue HSI', '色相 (HSI)')
    SATURATION_HSI                  = ('saturation_hsi', 'HSI', 'HSI 颜色调整', 'Saturation HSI', '饱和度 (HSI)')
    INTENSITY                       = ('intensity', 'HSI', 'HSI 颜色调整', 'Intensity', '亮度 (HSI)')
    DEC_SATURATION_HSI              = ('dec_saturation_hsi', 'HSI', 'HSI 颜色调整', 'Decrease Saturation HSI', '降低饱和度 (HSI)')
    INC_SATURATION_HSI              = ('inc_saturation_hsi', 'HSI', 'HSI 颜色调整', 'Increase Saturation HSI', '提高饱和度 (HSI)')
    DEC_INTENSITY                   = ('dec_intensity', 'HSI', 'HSI 颜色调整', 'Decrease Intensity', '降低亮度 (HSI)')
    INC_INTENSITY                   = ('inc_intensity', 'HSI', 'HSI 颜色调整', 'Increase Intensity', '提高亮度 (HSI)')

    COLOR_HSL                       = ('color_hsl', 'HSL', 'HSL 颜色调整', 'Color HSL', '颜色 (HSL)')
    HUE_HSL                         = ('hue_hsl', 'HSL', 'HSL 颜色调整', 'Hue HSL', '色相 (HSL)')
    SATURATION_HSL                  = ('saturation_hsl', 'HSL', 'HSL 颜色调整', 'Saturation HSL', '饱和度 (HSL)')
    LIGHTNESS                       = ('lightness', 'HSL', 'HSL 颜色调整', 'Lightness', '亮度')
    DEC_SATURATION_HSL              = ('dec_saturation_hsl', 'HSL', 'HSL 颜色调整', 'Decrease Saturation HSL', '降低饱和度 (HSL)')
    INC_SATURATION_HSL              = ('inc_saturation_hsl', 'HSL', 'HSL 颜色调整', 'Increase Saturation HSL', '提高饱和度 (HSL)')
    DEC_LIGHTNESS                   = ('dec_lightness', 'HSL', 'HSL 颜色调整', 'Decrease Lightness', '降低亮度 (HSL)')
    INC_LIGHTNESS                   = ('inc_lightness', 'HSL', 'HSL 颜色调整', 'Increase Lightness', '提高亮度 (HSL)')

    COLOR_HSV                       = ('color_hsv', 'HSV', 'HSV 颜色调整', 'Color HSV', '颜色 (HSV)')
    HUE_HSV                         = ('hue_hsv', 'HSV', 'HSV 颜色调整', 'Hue HSV', '色相 (HSV)')
    SATURATION_HSV                  = ('saturation_hsv', 'HSV', 'HSV 颜色调整', 'Saturation HSV', '饱和度 (HSV)')
    VALUE                           = ('value', 'HSV', 'HSV 颜色调整', 'Value', '明度 (HSV)')
    DEC_SATURATION_HSV              = ('dec_saturation_hsv', 'HSV', 'HSV 颜色调整', 'Decrease Saturation HSV', '降低饱和度 (HSV)')
    INC_SATURATION_HSV              = ('inc_saturation_hsv', 'HSV', 'HSV 颜色调整', 'Increase Saturation HSV', '提高饱和度 (HSV)')
    DEC_VALUE                       = ('dec_value', 'HSV', 'HSV 颜色调整', 'Decrease Value', '降低明度 (HSV)')
    INC_VALUE                       = ('inc_value', 'HSV', 'HSV 颜色调整', 'Increase Value', '提高明度 (HSV)')

    REFLECT                         = ('reflect', 'Quadratic', '二次方', 'Reflect', '反射')
    GLOW                            = ('glow', 'Quadratic', '二次方', 'Glow', '发光')
    FREEZE                          = ('freeze', 'Quadratic', '二次方', 'Freeze', '冷却')
    HEAT                            = ('heat', 'Quadratic', '二次方', 'Heat', '加热')
    GLOW_HEAT                       = ('glow_heat', 'Quadratic', '二次方', 'Glow-Heat', '发光-加热')
    HEAT_GLOW                       = ('heat_glow', 'Quadratic', '二次方', 'Heat-Glow', '加热-发光')
    REFLECT_FREEZE                  = ('reflect_freeze', 'Quadratic', '二次方', 'Reflect-Freeze', '反射-冷却')
    FREEZE_REFLECT                  = ('freeze_reflect', 'Quadratic', '二次方', 'Freeze-Reflect', '冷却-反射')
    HEAT_GLOW_FREEZE_REFLECT_HYBRID = ('heat_glow_freeze_reflect_hybrid', 'Quadratic', '二次方', 'Heat-Glow & Freeze-Reflect Hybrid', '加热-发光与冷却-反射结合')


    def __init__(self, id: str, en_category: str, cn_category: str, en_name: str, cn_name: str) -> None:
        super().__init__()
        self.id = id
        self.en_category = en_category
        self.cn_category = cn_category
        self.en_name = en_name
        self.cn_name = cn_name
        
    @classmethod
    def categories(cls):
        from itertools import groupby
        return groupby(cls, lambda i: i.en_category)
    

    @classmethod
    def by_id(cls, id: str):
        res = next((i for i in cls if i.id == id), None)
        if not res:
            raise KeyError(f'Unknown blending mode id: {id}')
        return res
    
