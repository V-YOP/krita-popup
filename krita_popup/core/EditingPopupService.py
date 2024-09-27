from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from krita_popup.helper import singleton
from krita_popup.helper.QtAll import *
from krita_popup.popup import EditingPopup
from krita_popup.items import items

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
        popup = EditingPopup([])
        
        self.__popup = popup
        self.__item_selector = self.__create_item_selector_widget()
        self.__cancel_button = self.__create_button('Cancel')
        self.__apply_button = self.__create_button('Apply')

    def __reset_widget_pos(self):
        self.__item_selector.setGeometry(0,0,400,100)

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
        # always display on left side
        item_entrys = items().items()
        for item_name, _ in item_entrys:
            item_selector.addItem(item_name)
        def on_select(idx: int):
            item_selector.setCurrentIndex(-1)
            self.__on_add_item(*item_entrys[idx][1])
        item_selector.currentIndexChanged.connect(on_select)
        item_selector.show()
        return item_selector

    def __create_button(self, text: str):
        btn = QPushButton(self.__popup)
        btn.setText(text)
        btn.show()
        return btn
        
    def __on_add_item(config_type, widget_type):
        # TODO place the widget under cursor,
        ...

    
    def __connect_once(self, signal: pyqtBoundSignal, slot):
        def go(*args):
            slot(*args)
            signal.disconnect(go)
        signal.connect(go)

    def wait_for_done(self) -> list[tuple[QWidget, QRect]] | None:
        """
        show and wait 
        """
        popup = self.__popup
        popup.show()
        self.__reset_widget_pos()

        loop = QEventLoop()
        self.__connect_once(self.__cancel_button.clicked, lambda: loop.exit(1))
        self.__connect_once(self.__apply_button.clicked, lambda: loop.exit(0))
        ret = loop.exec()
        popup.hide()

        if ret == 1:
            return None
        
        return popup.items()
