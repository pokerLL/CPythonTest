from utils import debug
class MyMeta(type):

    @debug
    def __init__(cls, name, bases, attr_dict):
        return super().__init__(name, bases, attr_dict)

    @classmethod
    @debug
    def __prepare__(cls, name, bases):
        return {'x': 42}

    @debug
    def __new__(cls, name, bases, namespace):
        return super().__new__(cls, name, bases, namespace)

class MyClass(metaclass=MyMeta):
    def foo(self):
        pass


'''
Calling __prepare__
    with args: (<class '__main__.MyMeta'>, 'MyClass', ())
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000025A5B710FD0>, '__spec__': None, '__annotations__': {}, '__bu
iltins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/metaclass.py', '__cached__': None, 'debug': <function debug at 0x0000025A5B79A040>, 'MyMeta': <class '__main__.MyMeta'>}

Calling __new__
    with args: (<class '__main__.MyMeta'>, 'MyClass', (), {'x': 42, '__module__': '__main__', '__qualname__': 'MyClass', 'foo': <function MyClass.foo at 0x0000025A5BA08670>})
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000025A5B710FD0>, '__spec__': None, '__annotations__': {}, '__bu
iltins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/metaclass.py', '__cached__': None, 'debug': <function debug at 0x0000025A5B79A040>, 'MyMeta': <class '__main__.MyMeta'>}

Calling __init__
    with args: (<class '__main__.MyClass'>, 'MyClass', (), {'x': 42, '__module__': '__main__', '__qualname__': 'MyClass', 'foo': <function MyClass.foo at 0x0000025A5BA08670>})
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000025A5B710FD0>, '__spec__': None, '__annotations__': {}, '__bu
iltins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/metaclass.py', '__cached__': None, 'debug': <function debug at 0x0000025A5B79A040>, 'MyMeta': <class '__main__.MyMeta'>}

'''