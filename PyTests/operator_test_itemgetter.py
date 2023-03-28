"""
>>> s = Stock('ACME', 50, 91.1)
>>> s
('ACME', 50, 91.1)
>>> s[0]
'ACME'
>>> s.name
'ACME'
>>> s.shares * s.price
4555.0
>>> s.shares = 23
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
"""

import operator

from utils import debug

class StructTupleMeta(type):
    @debug
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    @debug
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)
"""
Calling __main__.StructTupleMeta.__init__ at 2023-03-27 18:48:32.545949 with
    args:       (<class '__main__.StructTuple'>, 'StructTuple', (<class 'tuple'>,), {'__module__': '__main__', '__qualname__': 'StructTuple', '_fields': [], '__new__': <function debug.<locals>.wrapper at 0x000002EEDCA7B5E8>, '__classcell__': <cell at 0x000002EEDCA681F8: StructTupleMeta object at 0x000002EEDCAE2278>})
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002EEDC98E808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/operator_test_itemgetter.py', '__cached__': None, 'operator': <module 'operator' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\operator.py'>, 'debug': <function debug at 0x000002EEDCA72048>, 'StructTupleMeta': <class '__main__.StructTupleMeta'>}    
    result:     None
    process_time:       4.900000000002125e-06
    pref_counter_time:  2.239999999999881e-05

"""

class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

"""
Calling __main__.StructTupleMeta.__init__ at 2023-03-27 18:49:00.733091 with
    args:       (<class '__main__.Stock'>, 'Stock', (<class '__main__.StructTuple'>,), {'__module__': '__main__', '__qualname__': 'Stock', '_fields': ['name', 'shares', 'price']})
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000016ED18EE808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/operator_test_itemgetter.py', '__cached__': None, 'operator': <module 'operator' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\operator.py'>, 'debug': <function debug at 0x0000016ED19D44C8>, 'StructTupleMeta': <class '__main__.StructTupleMeta'>, 'StructTuple': <class '__main__.StructTuple'>}
    result:     None
    process_time:       2.1099999999996122e-05
    pref_counter_time:  3.3099999999994245e-05
"""

s = Stock('ACME', 50, 91.1)
"""

Calling __main__.StructTuple.__new__ at 2023-03-27 18:49:51.137446 with
    args:       (<class '__main__.Stock'>, 'ACME', 50, 91.1)
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001A45C00E6C8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/operator_test_itemgetter.py', '__cached__': None, 'operator': <module 'operator' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\operator.py'>, 'debug': <function debug at 0x000001A45C514558>, 'StructTupleMeta': <class '__main__.StructTupleMeta'>, 'StructTuple': <class '__main__.StructTuple'>, 'Stock': <class '__main__.Stock'>}
    result:     ('ACME', 50, 91.1)
    process_time:       7.900000000005125e-06
    pref_counter_time:  1.9999999999992246e-05

"""


"""
Calling __main__.StructTupleMeta.__init__ at 2023-03-27 18:50:46.555637 with
    args:       (<class '__main__.StructTuple'>, 'StructTuple', (<class 'tuple'>,), {'__module__': '__main__', '__qualname__': 'StructTuple', '_fields': [], '__new__': <function debug.<locals>.wrapper at 0x000002171050B0D8>, '__classcell__': <cell at 0x00000217104F8228: StructTupleMeta object at 0x000002171056EC18>})
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': '\n>>> s = Stock(\'ACME\', 50, 91.1)\n>>> s\n(\'ACME\', 50, 91.1)\n>>> s[0]\n\'ACME\'\n>>> s.name\n\'ACME\'\n>>> s.shares * s.price\n4555.0\n>>> s.shares = 23\nTraceback (most recent call last):\n    File "<stdin>", line 1, in <module>\nAttributeError: can\'t set attribute\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002170FFFE808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/operator_test_itemgetter.py', '__cached__': None, 'operator': <module 'operator' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\operator.py'>, 'debug': <function debug at 0x00000217105054C8>, 'StructTupleMeta': <class '__main__.StructTupleMeta'>}
    result:     None
    process_time:       5.600000000001437e-06
    pref_counter_time:  2.3799999999997434e-05

Calling __main__.StructTupleMeta.__init__ at 2023-03-27 18:50:46.557637 with
    args:       (<class '__main__.Stock'>, 'Stock', (<class '__main__.StructTuple'>,), {'__module__': '__main__', '__qualname__': 'Stock', '_fields': ['name', 'shares', 'price']})
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': '\n>>> s = Stock(\'ACME\', 50, 91.1)\n>>> s\n(\'ACME\', 50, 91.1)\n>>> s[0]\n\'ACME\'\n>>> s.name\n\'ACME\'\n>>> s.shares * s.price\n4555.0\n>>> s.shares = 23\nTraceback (most recent call last):\n    File "<stdin>", line 1, in <module>\nAttributeError: can\'t set attribute\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002170FFFE808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/operator_test_itemgetter.py', '__cached__': None, 'operator': <module 'operator' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\operator.py'>, 'debug': <function debug at 0x00000217105054C8>, 'StructTupleMeta': <class '__main__.StructTupleMeta'>, 'StructTuple': <class '__main__.StructTuple'>}
    result:     None
    process_time:       1.4700000000006375e-05
    pref_counter_time:  2.5299999999998934e-05

Calling __main__.StructTuple.__new__ at 2023-03-27 18:50:46.559639 with
    args:       (<class '__main__.Stock'>, 'ACME', 50, 91.1)
    kwargs:     {}
    local variables:    {'__name__': '__main__', '__doc__': '\n>>> s = Stock(\'ACME\', 50, 91.1)\n>>> s\n(\'ACME\', 50, 91.1)\n>>> s[0]\n\'ACME\'\n>>> s.name\n\'ACME\'\n>>> s.shares * s.price\n4555.0\n>>> s.shares = 23\nTraceback (most recent call last):\n    File "<stdin>", line 1, in <module>\nAttributeError: can\'t set attribute\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002170FFFE808>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:/Workspace/Program/CPythonTest/PyTests/operator_test_itemgetter.py', '__cached__': None, 'operator': <module 'operator' from 'C:\\Users\\datagrand\\miniconda3\\envs\\pyt\\lib\\operator.py'>, 'debug': <function debug at 0x00000217105054C8>, 'StructTupleMeta': <class '__main__.StructTupleMeta'>, 'StructTuple': <class '__main__.StructTuple'>, 'Stock': <class '__main__.Stock'>}
    result:     ('ACME', 50, 91.1)
    process_time:       6.900000000004125e-06
    pref_counter_time:  1.789999999998737e-05

"""