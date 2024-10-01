from typing import TypedDict
from krita import *
from PyQt5.QtWidgets import QWidget
from krita_popup.helper import DockerEnum, form
from krita_popup.helper.QtAll import *

from ._item_gegistry import RegistItem
from .BaseItem import BaseItem

class KritaDockBorrowerConfig(TypedDict):
    object_name: str
    transparent_background: bool

@RegistItem('Docker Borrower')
class KritaDockBorrower(QWidget, BaseItem[KritaDockBorrowerConfig]):
    """
    borrow krita's docker content
    """

    @staticmethod
    def default_configuration() -> KritaDockBorrowerConfig:
        return KritaDockBorrowerConfig(object_name='KisLayerBox', transparent_background=False)

    @staticmethod
    def create(conf: KritaDockBorrowerConfig):
        return KritaDockBorrower(conf)  # type: ignore
    
    def __get_docker_defs(self):
        """
        return list[(description, object_name)]
        """
        dockers = Krita.instance().dockers()
        res: list[tuple[str, str]] = []
        for docker in dockers:
            if enum := DockerEnum.from_object_name(docker.objectName()):
                # is krita internal dockers
                res.append((f'{enum.cn_name}/{enum.en_name}', enum.object_name))
            else:
                res.append((docker.windowTitle(), docker.objectName()))
        return res

    def start_editing(self) -> KritaDockBorrowerConfig | None:
        docker_defs = self.__get_docker_defs()
        current_docker_desc = next(i[0] for i in docker_defs if i[1] == self.__object_name)
        config = [
            form.DropdownField(
                type = 'dropdown',
                field='desc',
                label='Docker',
                items=[i[0] for i in docker_defs],
                defaultValue=current_docker_desc
            ),
            form.CheckboxField(
                type='checkbox',
                field='transparent_background',
                label='',
                defaultValue=['Transparent Background'] if self.__transparent_background else [],
                items=['Transparent Background']
            )
        ]
        result = form.exec_form_dialog(config, True)
        if not result:
            return None
        print(result)
        desc: str = result['desc'] # type: ignore
        transparent_background = bool(result['transparent_background'])

        return KritaDockBorrowerConfig(
            object_name=next(i[1] for i in docker_defs if i[0] == desc),
            transparent_background=transparent_background,
        )

    def __init__(self, conf: KritaDockBorrowerConfig) -> None:
        super().__init__(None)
        self.__object_name = conf['object_name']
        self.__transparent_background = conf['transparent_background']

        self.__dock_widget: QDockWidget | None = None
        self.__borrowed_widget: QWidget | None = None

        self.__placeholder = QLabel('Borrowed')
        self.__placeholder.setObjectName('BORROWED')
        self.destroyed.connect(self.return_back)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        if not self.__borrowed_widget:
            return super().resizeEvent(a0)
        self.__borrowed_widget.setGeometry(self.rect()) # rect 方法返回 (0, 0, *self.size())
        return super().resizeEvent(a0)

    def __get_dock_widget(self):
        return next(i for i in Krita.instance().dockers() if i.objectName() == self.__object_name)

    def borrow(self):
        if self.__borrowed_widget:
            return
        
        # do not store dock_widget for possible multiple window
        self.__dock_widget = self.__get_dock_widget()
        self.__borrowed_widget = self.__dock_widget.widget()

        if not self.__transparent_background:
            self.setAutoFillBackground(True)
            self.setPalette(Krita.instance().activeWindow().qwindow().palette())

        self.__dock_widget.setWidget(self.__placeholder)
        self.__borrowed_widget.setParent(self)
        qInfo(f'{self.__borrowed_widget.geometry()=}')
        self.__borrowed_widget.setGeometry(self.rect())
        self.__borrowed_widget.show()
        self.show()

    def return_back(self):
        if not self.__borrowed_widget or not self.__dock_widget:
            return
        self.__dock_widget.setWidget(self.__borrowed_widget)
        self.__borrowed_widget = None
        self.__dock_widget = None
        self.hide()

    def on_show(self):
        print('borrow me!')
        self.borrow()

    def on_hide(self):
        print('return me!')
        self.return_back()
        
if __name__ == '__main__':
    pass
    # from krita_popup.popup import Popup
    # win = Popup([], under_cursor=False)
    # # QApplication.instance().win = win # 避免被GC
    # dock = next(i for i in Krita.instance().dockers() if i.objectName() == 'sharedtooldocker')

    # container = KritaDockBorrower(dock)
    # borrow_btn = QPushButton(None)
    # borrow_btn.clicked.connect(container.borrow)
    # borrow_btn.setText('borrow')

    # return_back_btn = QPushButton(None)
    # return_back_btn.clicked.connect(container.return_back)
    # return_back_btn.setText('Return Back')

    # win.add_item(container, QRect(10, 100, 600, 300))
    # win.add_item(borrow_btn, QRect(10, 10, 120, 50))
    # win.add_item(return_back_btn, QRect(150, 10, 120, 50))
    # win.show()