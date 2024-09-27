from dataclasses import is_dataclass
from typing import Protocol

from .BaseItem import BaseItem

_items: dict[str, type[BaseItem]] = {}

def RegistItem(name: str):
    """
    A class decorator for registering items which can be put onto popup, configuration must be encapsulated with dataclass.

    # example:
    ```
    @dataclass
    class SomeConfig:
        a: int
        b: str

    @RegistItem('some widget', SomeConfig)
    class SomeWidget(QWidget):
        def __init__(self, config: SomeConfig):
            ...
    ```
    """
    if name in _items:
        raise RuntimeError(f'duplicate item name {name}')
    def go(registed_class): 
        _items[name] = registed_class
        return registed_class
    return go

def items():
    """
    get the registed items(`name -> widget_class`)
    """
    return _items.copy()