from utils import debug

class MyDescriptor:
    @debug
    def __get__(self, instance, owner):
        return instance._x
    
    @debug
    def __set__(self, instance, value):
        instance._x = value


class Parent:
    x = MyDescriptor()
    def __init__(self, x) -> None:
        self._x = x

class Son(Parent):
    pass

# p = Parent(20)
# print(p.x) 
# p.x = 30
"""
Calling __main__.__get__ at 2023-03-27 15:27:33.876480 with
    args:       (<__main__.MyDescriptor object at 0x0000020028D6E408>, <__main__.Parent object at 0x0000020028D6E448>, <class '__main__.Parent'>) 
    kwargs:     {} 
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020028C8E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/descriptor_test_subclass.py', '__cached__': None, 'debug': <function debug at 0x0000020028D71048>, 'MyDescriptor': <class '__main__.MyDescriptor'>, 'Parent': <class '__main__.Parent'>, 'Son': <class '__main__.Son'>, 'p': <__main__.Parent object at 0x0000020028D6E448>}
    result:     20
    process_time:       2.9000000000001247e-06
    pref_counter_time:  3.1800000000005435e-05

20
Calling __main__.__set__ at 2023-03-27 15:27:33.879477 with
    args:       (<__main__.MyDescriptor object at 0x0000020028D6E408>, <__main__.Parent object at 0x0000020028D6E448>, 30)
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000020028C8E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/descriptor_test_subclass.py', '__cached__': None, 'debug': <function debug at 0x0000020028D71048>, 'MyDescriptor': <class '__main__.MyDescriptor'>, 'Parent': <class '__main__.Parent'>, 'Son': <class '__main__.Son'>, 'p': <__main__.Parent object at 0x0000020028D6E448>}
    result:     None
    process_time:       5.400000000002625e-06
    pref_counter_time:  2.3599999999998622e-05

"""
s = Son(30)
print(s.x)   
s.x = 40
print(s.x)
"""
Calling __main__.__get__ at 2023-03-27 15:28:24.545093 with
    args:       (<__main__.MyDescriptor object at 0x000001D72FDEE408>, <__main__.Son object at 0x000001D72FDEE448>, <class '__main__.Son'>) 
    kwargs:     {} 
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D72FD0E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/descriptor_test_subclass.py', '__cached__': None, 'debug': <function debug at 0x000001D72FDF1048>, 'MyDescriptor': <class '__main__.MyDescriptor'>, 'Parent': <class '__main__.Parent'>, 'Son': <class '__main__.Son'>, 's': <__main__.Son object at 0x000001D72FDEE448>}
    result:     30
    process_time:       3.099999999991998e-06
    pref_counter_time:  3.0099999999991245e-05

30
Calling __main__.__set__ at 2023-03-27 15:28:24.546094 with
    args:       (<__main__.MyDescriptor object at 0x000001D72FDEE408>, <__main__.Son object at 0x000001D72FDEE448>, 40)
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D72FD0E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/descriptor_test_subclass.py', '__cached__': None, 'debug': <function debug at 0x000001D72FDF1048>, 'MyDescriptor': <class '__main__.MyDescriptor'>, 'Parent': <class '__main__.Parent'>, 'Son': <class '__main__.Son'>, 's': <__main__.Son object at 0x000001D72FDEE448>}
    result:     None
    process_time:       5.200000000010752e-06
    pref_counter_time:  1.8799999999999373e-05

Calling __main__.__get__ at 2023-03-27 15:28:24.548093 with
    args:       (<__main__.MyDescriptor object at 0x000001D72FDEE408>, <__main__.Son object at 0x000001D72FDEE448>, <class '__main__.Son'>)
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001D72FD0E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/descriptor_test_subclass.py', '__cached__': None, 'debug': <function debug at 0x000001D72FDF1048>, 'MyDescriptor': <class '__main__.MyDescriptor'>, 'Parent': <class '__main__.Parent'>, 'Son': <class '__main__.Son'>, 's': <__main__.Son object at 0x000001D72FDEE448>}
    result:     40
    process_time:       4.799999999999249e-06
    pref_counter_time:  2.0300000000000873e-05

40
"""