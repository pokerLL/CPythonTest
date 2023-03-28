import types
from functools import wraps

from utils import debug

class Profiled:
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
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

# add(2,3)
# print(add.ncalls)
"""
Calling __main__.__call__ at 2023-03-27 17:35:40.416777 with
    args:       (<__main__.Profiled object at 0x0000024F42DEC908>, 2, 3) 
    kwargs:     {} 
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000024F42D0E7C8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/decorator_test7_profiled.py', '__cached__': None, 'types': <module 'types' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\types.py'>, 'wraps': <function wraps at 0x0000024F42E048B8>, 'debug': <function debug at 0x0000024F42E044C8>, 'Profiled': <class '__main__.Profiled'>, 'add': <__main__.Profiled object at 0x0000024F42DEC908>, 'Spam': <class '__main__.Spam'>}
    result:     5
    process_time:       5.299999999999749e-06
    pref_counter_time:  2.920000000000006e-05

1
"""
sp = Spam()
sp.bar(2)
print(Spam.bar.ncalls)
"""
Calling __main__.__get__ at 2023-03-27 17:35:54.881729 with
    args:       (<__main__.Profiled object at 0x000001E68770CA08>, <__main__.Spam object at 0x000001E68770CD48>, <class '__main__.Spam'>) 
    kwargs:     {} 
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E68722E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/decorator_test7_profiled.py', '__cached__': None, 'types': <module 'types' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\types.py'>, 'wraps': <function wraps at 0x000001E687724948>, 'debug': <function debug at 0x000001E687724558>, 'Profiled': <class '__main__.Profiled'>, 'add': <__main__.Profiled object at 0x000001E68770C988>, 'Spam': <class '__main__.Spam'>, 'sp': <__main__.Spam object at 0x000001E68770CD48>}
    result:     <bound method Spam.bar of <__main__.Spam object at 0x000001E68770CD48>>
    process_time:       2.9000000000001247e-06
    pref_counter_time:  2.0800000000001373e-05

<__main__.Spam object at 0x000001E68770CD48> 2
Calling __main__.__call__ at 2023-03-27 17:35:54.882766 with
    args:       (<__main__.Profiled object at 0x000001E68770CA08>, <__main__.Spam object at 0x000001E68770CD48>, 2)
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E68722E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/decorator_test7_profiled.py', '__cached__': None, 'types': <module 'types' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\types.py'>, 'wraps': <function wraps at 0x000001E687724948>, 'debug': <function debug at 0x000001E687724558>, 'Profiled': <class '__main__.Profiled'>, 'add': <__main__.Profiled object at 0x000001E68770C988>, 'Spam': <class '__main__.Spam'>, 'sp': <__main__.Spam object at 0x000001E68770CD48>}
    result:     None
    process_time:       0.0001994999999999983
    pref_counter_time:  0.0002117999999999981

Calling __main__.__get__ at 2023-03-27 17:35:54.885424 with
    args:       (<__main__.Profiled object at 0x000001E68770CA08>, None, <class '__main__.Spam'>)
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001E68722E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/decorator_test7_profiled.py', '__cached__': None, 'types': <module 'types' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\types.py'>, 'wraps': <function wraps at 0x000001E687724948>, 'debug': <function debug at 0x000001E687724558>, 'Profiled': <class '__main__.Profiled'>, 'add': <__main__.Profiled object at 0x000001E68770C988>, 'Spam': <class '__main__.Spam'>, 'sp': <__main__.Spam object at 0x000001E68770CD48>}
    result:     <__main__.Profiled object at 0x000001E68770CA08>
    process_time:       5.299999999999749e-06
    pref_counter_time:  3.0499999999995808e-05

1
"""