import types
from functools import wraps

from utils import debug

class Profiled:
    @debug
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    @debug
    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    @debug
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

@Profiled
def my_func(x, y):
    return x + y

my_func(3, 4) # returns 7
my_func.ncalls # returns 1
"""
Calling __init__ with
    args: (<__main__.Profiled object at 0x0000027CB9F8B988>, <function my_func at 0x0000027CB9F88048>)
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000027CB9EAEB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/decorator_test_profiled.py', '__cached__': None, 'types': <module 'types' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\types.py'>, 'wraps': <function wraps at 0x0000027CB9F9EAF8>, 'debug': <function debug at 0x0000027CB9F9E948>, 'Profiled': <class '__main__.Profiled'>}

Calling __call__ with
    args: (<__main__.Profiled object at 0x0000027CB9F8B988>, 3, 4)
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000027CB9EAEB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/decorator_test_profiled.py', '__cached__': None, 'types': <module 'types' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\types.py'>, 'wraps': <function wraps at 0x0000027CB9F9EAF8>, 'debug': <function debug at 0x0000027CB9F9E948>, 'Profiled': <class '__main__.Profiled'>, 'my_func': <__main__.Profiled object at 0x0000027CB9F8B988>}
"""

class MyClass:
    @Profiled
    def my_method(self, x, y):
        return x + y

obj = MyClass()
obj.my_method(3, 4) # returns 7
print(obj.my_method.ncalls) # prints 1
"""
Calling __init__ with
    args: (<__main__.Profiled object at 0x000001EAC023BA88>, <function MyClass.my_method at 0x000001EAC03AEC18>) 
    kwargs: {} 
    local variables: {'__module__': '__main__', '__qualname__': 'MyClass'}
    
Calling __get__ with
    args: (<__main__.Profiled object at 0x000001EAC023BA88>, <__main__.MyClass object at 0x000001EAC0242848>, <class '__main__.MyClass'>) 
    kwargs: {} 
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001EAC015EB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/decorator_test_profiled.py', '__cached__': None, 'types': <module 'types' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\types.py'>, 'wraps': <function wraps at 0x000001EAC024EC18>, 'debug': <function debug at 0x000001EAC024EA68>, 'Profiled': <class '__main__.Profiled'>, 'MyClass': <class '__main__.MyClass'>, 'obj': <__main__.MyClass object at 0x000001EAC0242848>}
    
Calling __call__ with
    args: (<__main__.Profiled object at 0x000001EAC023BA88>, <__main__.MyClass object at 0x000001EAC0242848>, 3, 4) 
    kwargs: {} 
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001EAC015EB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/decorator_test_profiled.py', '__cached__': None, 'types': <module 'types' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\types.py'>, 'wraps': <function wraps at 0x000001EAC024EC18>, 'debug': <function debug at 0x000001EAC024EA68>, 'Profiled': <class '__main__.Profiled'>, 'MyClass': <class '__main__.MyClass'>, 'obj': <__main__.MyClass object at 0x000001EAC0242848>}

Calling __get__ with
    args: (<__main__.Profiled object at 0x000001EAC023BA88>, <__main__.MyClass object at 0x000001EAC0242848>, <class '__main__.MyClass'>)
    kwargs: {}
    local variables: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001EAC015EB48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:/Program/Workspace/CPythonTest/PyTests/decorator_test_profiled.py', '__cached__': None, 'types': <module 'types' from 'D:\\Program\\IDLEs\\miniconda3\\envs\\CPythonTest\\lib\\types.py'>, 'wraps': <function wraps at 0x000001EAC024EC18>, 'debug': <function debug at 0x000001EAC024EA68>, 'Profiled': <class '__main__.Profiled'>, 'MyClass': <class '__main__.MyClass'>, 'obj': <__main__.MyClass object at 0x000001EAC0242848>}

1
"""