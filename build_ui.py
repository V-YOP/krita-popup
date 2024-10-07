import os
from subprocess import check_call
from shutil import which
from pathlib import Path
assert which('pyuic5'), 'must install `pyqt5` at global environment, try run `pip install pyqt5`'

os.chdir(Path(__file__).parent/'krita_popup')

for ui_file in [i.absolute() for i in Path('').glob('**/*.ui')]:
    os.chdir(ui_file.parent)
    check_call(['pyuic5', '-x', ui_file.name, '-o', ui_file.with_suffix('.py').name])
