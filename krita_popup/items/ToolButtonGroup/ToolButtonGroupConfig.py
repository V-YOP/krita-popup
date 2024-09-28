
from typing import TypedDict


class ToolButtonGroupConfig(TypedDict):
    """
    tools: tool object names

    horizontal: horizontal layout
    """
    tools: list[str]
    horizontal: bool