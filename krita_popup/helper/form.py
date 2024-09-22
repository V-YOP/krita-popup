from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def create_form(config):
    # 创建一个 QWidget 用于容纳表单
    form_widget = QWidget()
    layout = QVBoxLayout()
    fields = {}
    
    for field in config:
        field_name = field['field']
        field_type = field['type']
        default_value = field.get('defaultValue', '')
        locked = field.get('locked', False)
        items = field.get('items', [])
        
        # 创建一个水平布局来包含标签和字段组件
        field_layout = QHBoxLayout()
        
        # 创建并添加字段的标签
        label = QLabel(field_name)
        field_layout.addWidget(label)
        
        if field_type == 'input':
            input_widget = QLineEdit()
            if locked:
                input_widget.setEnabled(False)
            input_widget.setText(default_value)
            fields[field_name] = input_widget
            field_layout.addWidget(input_widget)
            
        elif field_type == 'ratio':
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
            
        elif field_type == 'dropdown':
            combo_box = QComboBox()
            combo_box.addItems(items)
            combo_box.setCurrentText(default_value)
            fields[field_name] = combo_box
            field_layout.addWidget(combo_box)
            if locked:
                combo_box.setEnabled(False)
            
        elif field_type == 'checkbox':
            checkboxes = []
            for item in items:
                checkbox = QCheckBox(item)
                if default_value and item in default_value:
                    checkbox.setChecked(True)
                field_layout.addWidget(checkbox)
                checkboxes.append(checkbox)
                if locked:
                    checkbox.setEnabled(False)
            fields[field_name] = checkboxes
            
        elif field_type == 'file':
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
        layout.addLayout(field_layout)

    form_widget.setLayout(layout)
    
    def get_values():
        values = {}
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

# 使用示例
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QApplication([])

    config = [
        {'field': '输入字段', 'type': 'input', 'defaultValue': '默认值'},
        {'field': '锁定输入字段', 'type': 'input', 'defaultValue': '锁定值', 'locked': True},
        {'field': '单选', 'type': 'ratio', 'items': ['A', 'B'], 'defaultValue': 'A', 'locked': True},
        {'field': '下拉单选', 'type': 'dropdown', 'items': ['A', 'B'], 'defaultValue': 'A', 'locked': True},
        {'field': '复选框', 'type': 'checkbox', 'items': ['选项1', '选项2'], 'defaultValue': ['选项1'], 'locked': True},
        {'field': '文件选择', 'type': 'file'}
    ]

    form_widget, get_values = create_form(config)
    # 测试获取表单值
    def print_values():
        values = get_values()
        print(values)

    window = QMainWindow()
    window.show()

    dialog = QDialog(window)
    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(form_widget)
    dialog.layout().addWidget(button_box)
    dialog.exec_()
    print_values()

    # show.clicked.connect(print_values)
    import sys
    sys.exit(app.exec_())