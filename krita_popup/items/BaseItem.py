from typing import Generic, TypeVar
from PyQt5.QtGui import QKeyEvent, QRegion
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

from krita import Krita

def false_me() -> None:
    return False # type: ignore

if false_me():
    from typing import Self

T = TypeVar('T')

class BaseItem(Generic[T], QWidget):
    """
    Item interface, **must be inherited**, listen popup show, hide and editing me. subclasses must implement `default_conguration`, `create` and `start_editing` method, and can implement `on_show`, `on_hide`, `custom_mask` method if necessary. 
    
    T: Configuration Class, **must be Json serializable and deserializable**
    """
    @staticmethod
    def default_configuration() -> T:
        """
        A default configuration
        """
        raise NotImplementedError()

    @staticmethod
    def create(configuration: T, editing_mode: bool) -> 'Self': # type: ignore
        """
        Create instance by configuration. the client has no need to store the config_id because it's only used for identify configuration and will be given when store config
        
        configuration: A configuration class
        """
        raise NotImplementedError()

    def start_editing(self) -> T | None:
        """
        return edited configuration, return None if no editing. 

        If you need to show a dialog, make sure the dialog has no parents and is stay on top, eg:

        ```
        dialog = QDialog(None) # parent must be None, don't leave it empty
        dialog.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        dialog.raise_()
        ``` 

        subclass **has no need** to update itself with new configuration, it will be deleted (on_hide method will be invoked) and then recreated. 
        """
        raise NotImplementedError()

    def on_show(self): 
        """
        Invoked when popup added onto editing popup and editing popup showed.

        **It might be invoked even if it's already visible!**
        """
        pass

    def on_hide(self): 
        """
        Invoked when popup hides and deleted from editing popup

        **It might be invoked even if it's already non-visible!**
        """
        pass
    
    def custom_mask(self) -> QRegion:
        """
        return a QRegion as mask, override it if the widget is not showed like a rectangle
        """
        return NotImplemented