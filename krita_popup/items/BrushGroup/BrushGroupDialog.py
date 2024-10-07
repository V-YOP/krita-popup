
from typing import Generator, Iterable
from krita import *
from .BrushGroupConfig import BrushGroupConfig
from krita_popup.helper.QtAll import *

class ResourceItem(QListWidgetItem):
    def __init__(self, resource: Resource) -> None:
        super().__init__(None)
        self.resource = resource
        self.setIcon(QIcon(QPixmap.fromImage(resource.image())))

class ResourceListWidget(QWidget):
    """
    A list widget for showing krita resources
    """
    def __init__(self) -> None:
        super().__init__(None)
        self.__icon_list = QListWidget(self)
        self.__icon_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.__icon_list.setWrapping(True)
        # self._icon_list.setViewMode(QListView.IconMode)
        self.__icon_list.setResizeMode(QListView.Adjust)
        self.__icon_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__icon_list.setSpacing(0)
        self.__icon_list.setIconSize(QSize(64,64))
        self.__icon_list.setTextElideMode(Qt.ElideMiddle)
        self.__icon_list.setFlow(QListView.LeftToRight)
        self.__icon_list.setUniformItemSizes(True)

        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().addWidget(self.__icon_list)

    def add_resource(self, resource: Resource) -> None:
        item = ResourceItem(resource)
        self.__icon_list.addItem(item)

    def current_selected_resource(self) -> Resource | None:
        if current := self.__icon_list.currentItem():
            return current.resource # type: ignore
        
    def remove_current_selected_resource(self) -> None:
        print(self.__icon_list.currentRow())
        print(self.__icon_list.currentItem())
        if self.__icon_list.currentRow() >= 0:
            self.__icon_list.takeItem(self.__icon_list.currentRow())    

    def get_resources(self) -> Generator[Resource, None, None]:
        for i in range(self.__icon_list.count()):
            yield self.__icon_list.item(i).resource # type: ignore

class BrushEditingWidget(QWidget):
    def __init__(self, resources: Iterable[Resource]) -> None:
        super().__init__(None)
        layout = QHBoxLayout()
        self.__chooser = PresetChooser()
        self.__resource_list_widget = ResourceListWidget()
        [self.__resource_list_widget.add_resource(i) for i in resources]

        self.__deselect_button = QPushButton()
        self.__deselect_button.setIcon(Krita.instance().icon('arrow-left'))
        self.__deselect_button.setMinimumSize(16, 64)
        self.__deselect_button.clicked.connect(self.__deselect_resource)
        self.__select_button = QPushButton()
        self.__select_button.setIcon(Krita.instance().icon('arrow-right'))
        self.__select_button.setMinimumSize(16, 64)
        self.__select_button.clicked.connect(self.__select_resource)

        layout.addWidget(self.__chooser)
        layout.addWidget(self.__deselect_button)
        layout.addWidget(self.__select_button)
        layout.addWidget(self.__resource_list_widget)
        self.setLayout(layout)
    
    def __deselect_resource(self):
        self.__resource_list_widget.remove_current_selected_resource()

    def __select_resource(self):
        if resource := self.__chooser.currentPreset():
            self.__resource_list_widget.add_resource(resource)

    def selected_resources(self) -> list[Resource]:
        return list(self.__resource_list_widget.get_resources())
    


def exec_editing_dialog(setting: BrushGroupConfig) -> BrushGroupConfig | None:
    def from_str(name: str) -> Resource | None:
        return Krita.instance().resources('preset').get(name)
    dialog = QDialog(None)
    dialog.resize(1200, 800)
    dialog.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    dialog.raise_()

    horizontal_checkbox = QCheckBox()
    horizontal_checkbox.setText('Horizontal')
    horizontal_checkbox.setChecked(setting['horizontal'])
    
    brush_editing_widget = BrushEditingWidget(filter(lambda x:x, map(from_str, setting['brushes']))) # type: ignore

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.rejected.connect(lambda: dialog.done(0))
    button_box.accepted.connect(lambda: dialog.done(1))
    dialog.setLayout(QVBoxLayout())

    dialog.layout().addWidget(horizontal_checkbox)
    dialog.layout().addWidget(brush_editing_widget)
    dialog.layout().addWidget(button_box)

    if dialog.exec() == 0:
        return None
    
    horizontal = horizontal_checkbox.isChecked()
    resources = brush_editing_widget.selected_resources()

    return BrushGroupConfig(
        brushes=[resource.name() for resource in resources],
        horizontal=horizontal
    )
    

if __name__ == '__main__':
    w = BrushEditingWidget([])
    # for i in Krita.instance().resources('preset').values():
    #     w.add_resource(i)
    print(list(w.selected_resources()))
    w.show()
    # chooser = PresetChooser()
    # Krita.instance().win = chooser  # type: ignore
    # chooser.show()
    # def new_preset(a: Resource):
    #     print(a, type(a), a.objectName(), a.name())
    # chooser.presetSelected.connect(new_preset)