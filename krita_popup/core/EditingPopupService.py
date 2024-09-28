import uuid
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .ConfigurationService import ConfigurationService
from krita_popup.helper import singleton
from krita_popup.helper.QtAll import *
from krita_popup.popup import EditingPopup
from .ConfigurationService import ItemConfig, ItemInstance
from krita_popup.items import BaseItem, item_defs

@singleton
class EditingPopupService:
    """
    Wraps Editing Popup, provide methods about adding, deleting items and editing items' geometry and configuration

    A QCombobox on top left would be used to add items, that's how it should works:
    1. User click it, select an item
    2. Open a dialog about the widget's configuration
    3. user fill fields on it and click 'Ok'
    4. Ask user to click anywhere to put the widget on it

    that's how it really works:
    1. User click it, select an item
    2. Place corresponding widget on center! configuration? no configuration!
    """

    def __init__(self) -> None:
        # TODO add a method about 
        self.__popup = EditingPopup([])
        self.__configuration_service = ConfigurationService()
        self.__item_selector = self.__create_item_selector_widget()
        self.__cancel_button = self.__create_button('Cancel')
        self.__apply_button = self.__create_button('Apply')

        self.__items: list[ItemInstance] = []

    def __reset_widget_pos(self):
        self.__item_selector.setGeometry(0,0,400,50)

        size = self.__popup.size()

        cancel_button_geo = QRect()
        cancel_button_geo.setSize(QSize(200, 60))
        cancel_button_geo.moveBottomRight(QPoint(size.width() - 600, size.height() - 100))
        self.__cancel_button.setGeometry(cancel_button_geo)

        apply_button_geo = QRect()
        apply_button_geo.setSize(QSize(200, 60))
        apply_button_geo.moveBottomRight(QPoint(size.width() - 300, size.height() - 100))
        self.__apply_button.setGeometry(apply_button_geo)

    def __create_item_selector_widget(self):
        item_selector = QComboBox(self.__popup)
        item_selector.addItem('--- add item ---')
        item_selector.setCurrentIndex(0)
        # always display on left side
        item_entrys = list(item_defs().items())
        for item_name, _ in item_entrys:
            item_selector.addItem(item_name)
        def on_select(idx: int):
            if idx == 0:
                return
            item_selector.setCurrentIndex(0)
            self.__add_item(*item_entrys[idx - 1])
        item_selector.currentIndexChanged.connect(on_select)
        item_selector.show()
        return item_selector

    def __create_button(self, text: str):
        btn = QPushButton(self.__popup)
        btn.setText(text)
        btn.show()
        return btn
        
    def __add_item(self, item_type_name: str, item_type: type[BaseItem], item_config: ItemConfig | None = None):
        # TODO place the widget under cursor,
        if item_config is None:
            id = uuid.uuid4().hex
            config = item_type.default_configuration()
            geo = (-100, -100, 200, 200)
        else: 
            id = item_config['id']
            config = item_config['conf']
            geo = item_config['geo']

        instance: QWidget = item_type.create(config)
        item_instance = ItemInstance(
            uuid=id,
            config=ItemConfig(
                id=id,
                item_type=item_type_name,
                conf=config,
                geo=geo,
            ),
            widget=instance,
            geo=QRect(*geo)
        )
        self.__items.append(item_instance)
        self.__popup.add_item(instance, QRect(*geo), self.__item_actions(item_instance))

    def __connect_once(self, signal: pyqtBoundSignal, slot):
        def go():
            slot()
            signal.disconnect(go)
        signal.connect(go)

    def __item_actions(self, instance: ItemInstance) -> list[QAction]:
        delete_action = QAction()
        delete_action.setText('Delete')
        def delete_item():
            self.__items.remove(instance)
            self.__popup.remove_item(instance.widget)
        delete_action.triggered.connect(delete_item)

        edit_action = QAction()
        edit_action.setText('Edit')
        def edit_item():
            item: BaseItem = instance.widget
            current_geo = self.__popup.relative_geometry(instance.widget)
            
            new_config = item.start_editing()
            if not new_config:
                return
            
            instance.config['conf'] = new_config
            instance.config['geo'] = [current_geo.x(),current_geo.y(),current_geo.width(),current_geo.height()]
            delete_item()
            self.__add_item(instance.config['item_type'], item_defs()[instance.config['item_type']], instance.config)
            

        edit_action.triggered.connect(edit_item)
        return [
            edit_action,
            delete_action,
        ]

    def wait_for_done(self, items: list[ItemInstance]) -> list[ItemConfig] | None:
        """
        show and wait. 

        items: item instances, **will be cleaned after invoke**
        """
        # move items to me 
        self.__items = items[:]
        items[:] = []
        del items
        self.__popup.clear_items()

        # TODO
        for item in self.__items:
            self.__popup.add_item(item.widget, item.geo, self.__item_actions(item))
        
        self.__reset_widget_pos()
        self.__popup.show()
        loop = QEventLoop()
        self.__connect_once(self.__cancel_button.clicked, lambda: loop.exit(0))
        self.__connect_once(self.__apply_button.clicked, lambda: loop.exit(1))
        ret = loop.exec()
        self.__popup.hide()

        if ret == 0:
            self.__items = []
            return None
        
        result = []
        for item in self.__items:
            geo = self.__popup.relative_geometry(item.widget)
            print(f'{item.widget.geometry()=}')
            print(f'relative {geo=}')
            print(f'{self.__popup.geometry()=}')
            print(f'{self.__popup.geometry().center()=}')
            result.append(ItemConfig(
                id = item.uuid,
                item_type = item.config['item_type'],
                conf = item.config['conf'],
                geo = [geo.x(), geo.y(), geo.width(), geo.height()]
            ))
        self.__items = []

        print(result)
        return result
        # return self.__popup.items()
