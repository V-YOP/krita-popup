

import json
from typing import Any, TypedDict
from krita_popup.helper import singleton
from krita_popup.helper import ToolEnum
from krita import *

class ItemConfig(TypedDict):
    id: str
    item_type: str
    conf: dict
    geo: tuple[int,int,int,int]

DEBUG = True
DEBUG_CONFIG: list[ItemConfig] = [
    ItemConfig(id='horizontal_test', item_type='Tool Button Group', geo=(-200,-150,400,100), conf=dict(
        tools=[i.object_name for i in [
            ToolEnum.KIS_TOOL_SELECT_OUTLINE,
            ToolEnum.KIS_TOOL_SELECT_ELLIPTICAL,
            ToolEnum.KIS_TOOL_SELECT_RECTANGULAR,
            ToolEnum.KIS_TOOL_SELECT_POLYGONAL,
        ]],
        horizontal=True,
    )),
    ItemConfig(id='vertical_test', item_type='Tool Button Group', geo=(200,-200,100,400), conf=dict(
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

    def load_configurations(self) -> list[ItemConfig]:
        """
        return item_id -> (item_type_name, item_configuration)
        """
        if DEBUG:
            return DEBUG_CONFIG
        setting = Krita.instance().readSetting('krita_popup', 'layout0', '[]')
        return json.loads(setting)
    
    def save_configurations(self, setting: ItemConfig):
        Krita.instance().writeSetting('krita_popup', 'layout0', json.dumps(setting))