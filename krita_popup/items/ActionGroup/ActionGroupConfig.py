
from typing import TypedDict


class ActionGroupConfig(TypedDict):
    """
    actions: action object names

    horizontal: horizontal layout
    """
    actions: list[str]
    horizontal: bool