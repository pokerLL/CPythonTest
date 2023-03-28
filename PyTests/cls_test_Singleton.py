from .utils import debug

class Singleton:
    _instance = None

    @debug
    def __init__(self, *args, **kwargs) -> None:
        pass

    @debug
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton(1,2,3)
"""
Calling __new__ 
    with args: (<class '__main__.Singleton'>, 1, 2, 3)
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D3258DEB08>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/class_test.py', '__cached__': None, 'inspect': <module 'inspect' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\inspect.py'>, 'debug': <function debug at 0x000001D3259B5E58>, 'Singleton': <class '__main__.Singleton'>}

Calling __init__
    with args: (<__main__.Singleton object at 0x000001D325B15CC8>, 1, 2, 3)
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D3258DEB08>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/class_test.py', '__cached__': None, 'inspect': <module 'inspect' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\inspect.py'>, 'debug': <function debug at 0x000001D3259B5E58>, 'Singleton': <class '__main__.Singleton'>}
"""
s2 = Singleton(4,5,6,me="Lei")
"""
Calling __new__
    with args: (<class '__main__.Singleton'>, 4, 5, 6)
    kwargs: {'me': 'Lei'}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000023466A0EB08>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\Program\\Workspace\\CPythonTest\\PyTests\\class_test_Singleton.py', '__cached__': None, 'inspect': <module 'inspect' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\inspect.py'>, 'debug': <function debug at 0x0000023466AE8048>, 'Singleton': <class '__main__.Singleton'>, 's1': <__main__.Singleton object at 0x0000023466AEE9C8>}

Calling __init__
    with args: (<__main__.Singleton object at 0x0000023466AEE9C8>, 4, 5, 6)
    kwargs: {'me': 'Lei'}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000023466A0EB08>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\Program\\Workspace\\CPythonTest\\PyTests\\class_test_Singleton.py', '__cached__': None, 'inspect': <module 'inspect' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\inspect.py'>, 'debug': <function debug at 0x0000023466AE8048>, 'Singleton': <class '__main__.Singleton'>, 's1': <__main__.Singleton object at 0x0000023466AEE9C8>}
"""

print(s1 is s2) # True