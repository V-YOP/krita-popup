from dataclasses import dataclass
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from typing import Generic, Literal, Optional, Sequence, TypeVar, TypedDict, Union
import sys

def false_me():
    return False

if false_me():
    from typing import NotRequired


class InputField(TypedDict):
    type: Literal['input']
    label: str
    field: str
    """
    字段名
    """
    defaultValue: 'NotRequired[str]'
    """
    默认值
    """
    locked: 'NotRequired[bool]'


class RatioField(TypedDict):
    type: Literal['ratio']
    label: str
    field: str
    items: list[str]
    defaultValue: 'NotRequired[str]'
    locked: 'NotRequired[bool]'


class DropdownField(TypedDict):
    type: Literal['dropdown']
    label: str
    field: str
    items: list[str]
    defaultValue: 'NotRequired[str]'
    locked: 'NotRequired[bool]'


class CheckboxField(TypedDict):
    type: Literal['checkbox']
    label: str
    field: str
    items: list[str]
    defaultValue: 'NotRequired[list[str]]'
    locked: 'NotRequired[bool]'


class FileField(TypedDict):
    type: Literal['file']
    label: str
    field: str
    locked: 'NotRequired[bool]'

Field = Union[InputField, RatioField, DropdownField, CheckboxField, FileField]
            
def create_form(config: Sequence[Field]):
    # 创建一个 QWidget 用于容纳表单
    form_widget = QWidget()
    layout = QFormLayout()
    fields = {}
    
    for field in config:
        field_name = field['field']
        field_type = field['type']
        field_label = field['label']
        locked = field.get('locked', False)
        
        # 创建一个水平布局来包含字段组件
        field_layout = QHBoxLayout()
        
        if field['type'] == 'input':
            default_value: str = field.get('defaultValue', '')
            input_widget = QLineEdit()
            if locked:
                input_widget.setEnabled(False)
            input_widget.setText(default_value)
            fields[field_name] = input_widget
            field_layout.addWidget(input_widget)
            
        elif field['type'] == 'ratio':
            items = field['items']
            default_value: str = field.get('defaultValue', '')
            button_group = QButtonGroup()
            for item in items:
                radio_button = QRadioButton(item)
                if locked:
                    radio_button.setEnabled(False)
                if item == default_value:
                    radio_button.setChecked(True)
                field_layout.addWidget(radio_button)
                button_group.addButton(radio_button)
            fields[field_name] = button_group
            
        elif field['type'] == 'dropdown':
            items = field['items']
            default_value: str = field.get('defaultValue', '')
            combo_box = QComboBox()
            combo_box.addItems(items)
            combo_box.setCurrentText(default_value)
            fields[field_name] = combo_box
            field_layout.addWidget(combo_box)
            if locked:
                combo_box.setEnabled(False)
            
        elif field['type'] == 'checkbox':
            items = field['items']
            default_values = field.get('defaultValue', [])
            checkboxes = []
            for item in items:
                checkbox = QCheckBox(item)
                if default_values and item in default_values:
                    checkbox.setChecked(True)
                field_layout.addWidget(checkbox)
                checkboxes.append(checkbox)
                if locked:
                    checkbox.setEnabled(False)
            fields[field_name] = checkboxes
            
        elif field['type'] == 'file':
            file_layout = QHBoxLayout()  # 为文件选择字段创建子布局
            button = QPushButton("选择文件")
            file_path = QLineEdit()
            file_path.setReadOnly(True)
            
            def open_file_dialog():
                file_name, _ = QFileDialog.getOpenFileName()
                if file_name:
                    file_path.setText(file_name)
                    
            button.clicked.connect(open_file_dialog)
            file_layout.addWidget(file_path)
            file_layout.addWidget(button)
            
            fields[field_name] = file_path
            field_layout.addLayout(file_layout)

        else:
            raise ValueError(f"Unsupported field type: {field_type}")

        # 将字段的水平布局添加到主布局中
        layout.addRow(field_label, field_layout)

    form_widget.setLayout(layout)
    
    def get_values():
        values: dict[str, None | str | list[str]] = {}
        for field_name, widget in fields.items():
            if isinstance(widget, QLineEdit):
                values[field_name] = widget.text()
            elif isinstance(widget, QButtonGroup):
                checked_button = widget.checkedButton()
                values[field_name] = checked_button.text() if checked_button else None 
            elif isinstance(widget, QComboBox):
                values[field_name] = widget.currentText()
            elif isinstance(widget, list) and isinstance(widget[0], QCheckBox):
                checked_values = [cb.text() for cb in widget if cb.isChecked()]
                values[field_name] = checked_values
            elif isinstance(widget, QLineEdit):  # 文件路径选择字段
                values[field_name] = widget.text()
        return values

    return form_widget, get_values

def exec_form_dialog(fields: Sequence[Field], stay_on_top = False):
    form_widget, get_values = create_form(fields)
    dialog = QDialog(None)

    if stay_on_top:
        dialog.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        dialog.raise_()

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.accepted.connect(lambda: dialog.done(1))
    button_box.rejected.connect(lambda: dialog.done(0))
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(form_widget)
    dialog.layout().addWidget(button_box)
    
    if dialog.exec() == 0:
        return None
    return get_values()

# 使用示例
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication([])

    config = [
        {'label': '输入字段', 'field': 'input', 'type': 'input', 'defaultValue': '默认值'},
        {'label': '锁定输入字段', 'field': 'lock_input', 'type': 'input', 'defaultValue': '锁定值', 'locked': True},
        {'label': '单选', 'field': 'ratio', 'type': 'ratio', 'items': ['A', 'B'], 'defaultValue': 'A', 'locked': True},
        {'label': '下拉单选', 'field': 'dropdown', 'type': 'dropdown', 'items': ['A', 'B'], 'defaultValue': 'A', 'locked': True},
        {'label': '复选框', 'field': 'checkbox', 'type': 'checkbox', 'items': ['选项1', '选项2', '选项3', '选项4','选项1', '选项2', '选项3', '选项4'], 'defaultValue': ['选项1'], 'locked': True},
        {'label': '文件选择', 'field': 'file', 'type': 'file'}
    ]
    print(exec_form_dialog(config))

    # form_widget, get_values = create_form(config)
    # # 测试获取表单值
    # def print_values():
    #     values = get_values()
    #     print(values)

    # window = QMainWindow()
    # window.show()

    # dialog = QDialog(window)
    # button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    # button_box.accepted.connect(lambda: dialog.done(0))
    # button_box.rejected.connect(lambda: dialog.done(1))
    # dialog.setLayout(QVBoxLayout())
    # dialog.layout().addWidget(form_widget)
    # dialog.layout().addWidget(button_box)
    
    # print(dialog.exec_())
    # print_values()

    # # show.clicked.connect(print_values)
    # import sys
    # sys.exit(app.exec_())