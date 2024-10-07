
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from krita_popup.helper.QtAll import *
from .BaseItem import BaseItem
from krita import *


class LayerModeWidget(BaseItem[None]):
    @staticmethod
    def create(configuration: None, editing_mode: bool) -> 'LayerModeWidget':
        return LayerModeWidget(configuration)
    
    @staticmethod
    def default_configuration() -> None:
        return None
    
    def start_editing(self) -> None:
        return None
    
    def __init__(self, config: None) -> None:
        super().__init__()
        favo_blending_modes = Krita.instance().readSetting('', 'favoriteCompositeOps', '').split(',')
        Krita.instance().activeDocument().activeNode().blendingMode
        