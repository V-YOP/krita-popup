from functools import wraps

from .Logger import Logger
from PyQt5.QtCore import QObject

logger = Logger()

def singleton(cls):
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

