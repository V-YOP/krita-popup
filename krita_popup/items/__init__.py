"""
contains widgets that can be configured placed on popup
"""

from ._item_gegistry import item_defs
from .BaseItem import BaseItem

# import all modules on this directory
from pathlib import Path
import importlib
assert __package__, 'No parent package, WTF? me executed directly?'

for file in Path(__file__).parent.iterdir():
    if file.name.startswith('_'):
        continue
    module_name = file.with_suffix('').name
    print('import', module_name, __package__)
    importlib.import_module(f'{__package__}.{module_name}')

