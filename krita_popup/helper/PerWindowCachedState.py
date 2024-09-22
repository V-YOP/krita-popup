from functools import wraps
import types
from krita import *
from typing import TypeVar, Callable, Generic

T = TypeVar('T')
R = TypeVar('R')

class PerWindowCachedState(Generic[T]):
    def __init__(self, state_getter: Callable[[Window], T]) -> None:
        self.__state_getter = state_getter
        self.cache: dict[str, T] = {}
    
    def __window_id(self, window: Window):
        return window.qwindow().objectName()
    
    def get(self, window: Window) -> T:
        id = self.__window_id(window)
        if id in self.cache:
            return self.cache[id]
        self.cache[id] = self.__state_getter(window)
        return self.cache[id]
    
    def clear(self, window: Window | None = None):
        if window is None:
            self.cache = {}
            return
        
        if (id := self.__window_id(window)) in self.cache:
            del self.cache[id]

    def chain(self, mapper: Callable[[T], R]) -> "PerWindowCachedState[R]":
        parent = self
        def cb(window: Window) -> R:
            res = parent.get(window)
            return mapper(res)
        result = PerWindowCachedState(cb)
        clear_self = result.clear
        def clear_all(window: Window = None):
            clear_self(window)
            parent.clear(window)
        result.clear = types.MethodType(clear_all, result)
        return result

def window_cache(func):
    state = PerWindowCachedState(func)

    @wraps(func)
    def wrapper(window: Window):
        return state.get(window)
    
    setattr(wrapper, 'clear', lambda: state.clear())

    return wrapper