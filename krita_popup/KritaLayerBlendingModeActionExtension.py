
from krita import *
from krita_popup.helper.QtAll import *
from krita_popup.helper.BlendingMode import BlendingMode
from functools import partial

class KritaLayerBlendingModeActionExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        
    def setup(self):
        pass

    def createActions(self, window):
        menu_action = window.createAction('layer_blending_modes', 'Layer Blending Modes', "tools")
        self.menu = QMenu('Krita Popup', window.qwindow())
        menu_action.setMenu(self.menu)

        for bm in BlendingMode:
            # TODO HARD CODE 
            if not bm in (BlendingMode.DARKER_COLOR, BlendingMode.LIGHTER_COLOR, BlendingMode.NORMAL, BlendingMode.ERASE, BlendingMode.MULTIPLY, BlendingMode.LIGHTEN, BlendingMode.DODGE): continue
            action = window.createAction(f'layer_{bm.id}_blending_mode', f'Layer {bm.en_name} Blending Mode', 'tools/layer_blending_modes/')
            action.triggered.connect(partial(self.set_current_layer_blending_mode, bm))
    
    def set_current_layer_blending_mode(self, bm: BlendingMode):
        if not (active_document := Krita.instance().activeDocument()): return
        if not (active_node := active_document.activeNode()): return
        if active_node.locked(): return
        
        # setBlendingMode居然会记在历史记录里面，你说这扯不扯
        active_node.setBlendingMode(bm.id)

Krita.instance().addExtension(KritaLayerBlendingModeActionExtension(Krita.instance())) 
