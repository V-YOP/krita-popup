from typing import Generic, Protocol, TypeVar

def false_me() -> None:
    return False

if false_me():
    from typing import Self

T = TypeVar('T')

class BaseItem(Generic[T]):
    """
    Item interface, **must be inherited**, listen popup show, hide and editing me.
    
    T: Configuration Class, **must be Json serializable and deserializable**
    """
    @staticmethod
    def default_configuration() -> T:
        """
        A default configuration
        """

    @staticmethod
    def create(configuration: T) -> 'Self':
        """
        Create instance by configuration. the client has no need to store the config_id because it's only used for identify configuration and will be given when store config
        
        configuration: A configuration class
        """

    def start_editing(self) -> T | None:
        """
        return edited configuration, return None if no editing. 

        subclass **has no need** to update itself with new configuration, it will be deleted (on_hide method will be invoked) and then recreated. 
        """

    def on_show(self): 
        """
        Invoked when popup shows
        """

    def on_hide(self): 
        """
        Invoked when popup hides and deleted from editing popup
        """
    