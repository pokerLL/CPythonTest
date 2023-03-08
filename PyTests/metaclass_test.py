from utils import debug

class MyMeta(type):
    # Optional
    @classmethod
    @debug
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__prepare__(name, bases)

    # Required
    @debug
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        return super().__new__(cls, name, bases, ns)

    # Required
    @debug
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        pass
        super().__init__(name, bases, ns)

class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass

"""
Calling __prepare__ with
    args: (<class '__main__.MyMeta'>, 'Spam', ())
    kwargs: {'debug': True, 'synchronize': True}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000022763C5EB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/metaclass_test.py', '__cached__': None, 'debug': <function debug at 0x0000022764138048>, 'MyMeta': <class '__main__.MyMeta'>}
    result: {}

Calling __new__ with
    args: (<class '__main__.MyMeta'>, 'Spam', (), {'__module__': '__main__', '__qualname__': 'Spam'})  
    kwargs: {'debug': True, 'synchronize': True}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000022763C5EB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/metaclass_test.py', '__cached__': None, 'debug': <function debug at 0x0000022764138048>, 'MyMeta': <class '__main__.MyMeta'>}
    result: <class '__main__.Spam'>

Calling __init__ with
    args: (<class '__main__.Spam'>, 'Spam', (), {'__module__': '__main__', '__qualname__': 'Spam'})    
    kwargs: {'debug': True, 'synchronize': True}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000022763C5EB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/metaclass_test.py', '__cached__': None, 'debug': <function debug at 0x0000022764138048>, 'MyMeta': <class '__main__.MyMeta'>}
    result: None
"""