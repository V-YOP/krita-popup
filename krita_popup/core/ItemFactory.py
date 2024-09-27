from krita_popup.helper import singleton


@singleton
class ItemFactory:
    """
    Responsible for creating items by configuration, and dump configuration from items
    """