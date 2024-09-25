from dataclasses import is_dataclass

_items: dict[str, tuple[type, type]] = {}

def RegistItem(name: str, config_class: type):
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
    
    assert isinstance(config_class, type) and is_dataclass(config_class), f'{config_class} must be a dataclass'
    def go(registed_class): 
        _items[name] = (config_class, registed_class)
        return registed_class
    return go

def items():
    """
    get the registed items(`name -> (config_class, widget_class)`)
    """
    return _items.copy()