from dataclasses import is_dataclass
from typing import Protocol
from PyQt5.QtWidgets import QWidget
from .BaseItem import BaseItem

_items: dict[str, type[BaseItem]] = {}

def RegistItem(name: str):
    """
    A class decorator for registering items which can be put onto popup, registed class **must inherits from BaseItem**

    # example:
    ```
    @RegistItem('some widget')
    class SomeWidget(BaseItem[...]):
        ...
    ```
    """
    if name in _items:
        raise RuntimeError(f'duplicate item name {name}')
    def go(registed_class): 
        assert issubclass(registed_class, BaseItem), f'{name} must inherits from BaseItem!'
        _items[name] = registed_class 
        return registed_class
    return go

def item_defs():
    """
    get the registed items(`name -> widget_class`)
    """
    return _items.copy()