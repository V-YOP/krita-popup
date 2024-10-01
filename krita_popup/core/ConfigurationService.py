

import json
from typing import Any, NamedTuple, Protocol, TypedDict
from krita_popup.helper import singleton
from krita_popup.helper import ToolEnum
from krita import *
from krita_popup.helper.QtAll import *

class ItemConfig(TypedDict):
    id: str
    item_type: str
    conf: dict
    fixed: bool
    geo: tuple[int,int,int,int]

class ItemInstance(NamedTuple):
    uuid: str
    config: ItemConfig
    widget: QWidget
    geo: QRect

DEBUG = False
DEBUG_CONFIG: list[ItemConfig] = [
    ItemConfig(id='horizontal_test', item_type='Tool Button Group', fixed=False, geo=(-200,-150,400,100), conf=dict(
        tools=[i.object_name for i in [
            ToolEnum.KIS_TOOL_SELECT_OUTLINE,
            ToolEnum.KIS_TOOL_SELECT_ELLIPTICAL,
            ToolEnum.KIS_TOOL_SELECT_RECTANGULAR,
            ToolEnum.KIS_TOOL_SELECT_POLYGONAL,
        ]],
        horizontal=True,
    )),
    ItemConfig(id='vertical_test', item_type='Tool Button Group', fixed=False, geo=(200,-200,100,400), conf=dict(
        tools=[i.object_name for i in [
            ToolEnum.KIS_TOOL_SELECT_OUTLINE,
            ToolEnum.KIS_TOOL_SELECT_ELLIPTICAL,
            ToolEnum.KIS_TOOL_SELECT_RECTANGULAR,
            ToolEnum.KIS_TOOL_SELECT_POLYGONAL,
        ]],
        horizontal=False,
    ))
]

@singleton
class ConfigurationService:
    """
    Responsible for load and dump item configurations
    """

    def load_configurations(self, layout_idx: int) -> list[ItemConfig]:
        """
        return item_id -> (item_type_name, item_configuration)
        """
        if DEBUG:
            return DEBUG_CONFIG
        
        # TODO validate, filter all invalid settings
        setting = Krita.instance().readSetting('krita_popup', f'layout{layout_idx}', '[]')
        print(f'{layout_idx=}, {setting=}')
        return json.loads(setting)
    
    def save_configurations(self, layout_idx: int, settings: list[ItemConfig]):
        """
        save settings, items whose size is empty will be removed
        """
        # TODO validate, filter all invalid settings
        filtered_settings = []
        for setting in settings:
            _, _, w, h = setting['geo']
            if w * h != 0:
                filtered_settings.append(setting)
        Krita.instance().writeSetting('krita_popup', f'layout{layout_idx}', json.dumps(filtered_settings))