"""
contains widgets that can be configured placed on popup
"""

from ._item_gegistry import items


# import all modules on this directory
from pathlib import Path
import importlib
assert __package__, 'No parent package, WTF? me executed directly?'

for file in Path(__file__).parent.iterdir():
    if file.name.startswith('_'):
        continue
    module_name = file.with_suffix('').name
    importlib.import_module(module_name, __package__)

