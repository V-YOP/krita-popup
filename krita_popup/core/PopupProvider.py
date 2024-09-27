
from krita_popup.helper import singleton


@singleton
class PopupProvider:
    """
    The guy who makes his hand dirty handling everything about popup including toggle, edit, configuration r/w
    """

    def __init__(self) -> None:
        pass