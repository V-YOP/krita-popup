from dataclasses import Field, dataclass
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from typing import Generic, Literal, Optional, TypeVar, TypedDict, Union, overload, NotRequired

@dataclass
class InputField:
    """
    输入字段，结果将是字符串
    """
    field: str
    """
    字段名
    """
    defaultValue: str = ''
    """
    默认值
    """
    locked: bool = False
    """
    是否锁定（锁定表示仅提示用）
    """
    type: Literal['input'] = 'input'



@dataclass
class RatioField:
    """
    单选字段，结果将是字符串
    """

    field: str
    """
    字段名
    """
    items: list[str]
    """
    可选项
    """
    defaultValue: str | None = None
    """
    默认值
    """
    locked: bool = False
    """
    是否锁定（锁定表示仅提示用）
    """
    type: Literal['ratio'] = 'ratio'

@dataclass
class DropdownField:
    """
    下拉单选字段，结果将是字符串
    """

    field: str
    """
    字段名
    """
    items: list[str]
    """
    可选项
    """
    defaultValue: str | None = None
    """
    默认值
    """
    locked: bool = False
    """
    是否锁定（锁定表示仅提示用）
    """
    type: Literal['dropdown'] = 'dropdown'

@dataclass
class CheckboxField:
    """
    复选字段，结果将是一个列表
    """

    field: str
    """
    字段名
    """
    items: list[str]
    """
    可选项
    """

    defaultValue: list[str] = Field(default_factory=lambda: [])
    """
    默认值
    """

    locked: bool = False
    """
    是否锁定（锁定表示仅提示用）
    """
    type: Literal['checkbox'] = 'checkbox'

@dataclass
class FileField:
    """
    文件输入字段，结果将是文件路径 Path
    """

    field: str
    """
    字段名
    """
    type: Literal['file'] = 'file'

    

FieldType = Union[InputField, RatioField, DropdownField, CheckboxField, FileField]

class FieldHelper:
    def __init__(self, field: FieldType) -> None:
        self.__field = field
        self.__layout: QLayout | None = None
        

    def layout(self):
        if self.__layout:
            return self.__layout
        
        match self.__field.type:
            case 'input':
                pass