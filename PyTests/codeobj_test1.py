s = "FFFFF"

def func(x, y):
    if x == y:
        return 0
    return 1

def deractor(func):
    def wrapper(*args, **kwargs):
        print("wrapper")
        return func(*args, **kwargs)
    return wrapper

class F:
    pass

func()

""" 
>>> text = open("./PyTests/codeobj_test1.py", 'r').read()
>>> text
's = "FFFFF"\n\ndef func(x, y):\n    if x == y:\n        return 0\n    return 1\n\ndef deractor(func):\n    def wrapper(*args, **kwargs):\n        print("wrapper")\n        return func(*args, **kwargs)\n    return wrapper\n\nclass F:\n    pass\n\nfunc()'
>>> code = compile(text, 'cbt', 'exec')
>>> def print_code(co):
...     print(f'co_name:\t{co.co_name}')
...     for attr in dir(co):
...         if attr[0] != '_':
...             print(f'  {attr}:\t{getattr(co,attr)}')
... 
>>> def dfs(co):
...     print_code(co)
...     for c in co.co_consts:
...         if isinstance(c, types.CodeType):
...             dfs(c)
... 
>>> import types
>>> dfs(code)
co_name:        <module>
  co_argcount:  0
  co_cellvars:  ()
  co_code:      b'\x97\x00d\x00Z\x00d\x01\x84\x00Z\x01d\x02\x84\x00Z\x02\x02\x00G\x00d\x03\x84\x00d\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z\x03\x02\x00e\x01\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x05S\x00'
  co_consts:    ('FFFFF', <code object func at 0x7fba5e04f5d0, file "cbt", line 3>, <code object deractor at 0x7fba5df36320, file "cbt", line 8>, <code object F at 0x7fba5df36f50, file "cbt", line 14>, 'F', None)
  co_exceptiontable:    b''
  co_filename:  cbt
  co_firstlineno:       1
  co_flags:     0
  co_freevars:  ()
  co_kwonlyargcount:    0
  co_lines:     <built-in method co_lines of code object at 0x7fba5df2aa30>
  co_linetable: b'\xf0\x03\x01\x01\x01\xd8\x04\x0b\x80\x01\xf0\x04\x03\x01\r\xf0\x00\x03\x01\r\xf0\x00\x03\x01\r\xf0\n\x04\x01\x13\xf0\x00\x04\x01\x13\xf0\x00\x04\x01\x13\xf0\x0c\x01\x01\t\xf0\x00\x01\x01\t\xf0\x00\x01\x01\t\xf0\x00\x01\x01\t\xf0\x00\x01\x01\t\xf1\x00\x01\x01\t\xf4\x00\x01\x01\t\xf0\x00\x01\x01\t\xf0\x06\x00\x01\x05\x80\x04\x81\x06\x84\x06\x80\x06\x80\x06\x80\x06'
  co_lnotab:    b'\x00\xff\x02\x01\x04\x02\x06\x05\x06\x06\x1a\x03'
  co_name:      <module>
  co_names:     ('s', 'func', 'deractor', 'F')
  co_nlocals:   0
  co_positions: <built-in method co_positions of code object at 0x7fba5df2aa30>
  co_posonlyargcount:   0
  co_qualname:  <module>
  co_stacksize: 4
  co_varnames:  ()
  replace:      <built-in method replace of code object at 0x7fba5df2aa30>
co_name:        func
  co_argcount:  2
  co_cellvars:  ()
  co_code:      b'\x97\x00|\x00|\x01k\x02\x00\x00\x00\x00r\x02d\x01S\x00d\x02S\x00'
  co_consts:    (None, 0, 1)
  co_exceptiontable:    b''
  co_filename:  cbt
  co_firstlineno:       3
  co_flags:     3
  co_freevars:  ()
  co_kwonlyargcount:    0
  co_lines:     <built-in method co_lines of code object at 0x7fba5e04f5d0>
  co_linetable: b'\x80\x00\xd8\x07\x08\x88A\x82v\x80v\xd8\x0f\x10\x88q\xd8\x0b\x0c\x881'
  co_lnotab:    b'\x02\x01\x0c\x01\x04\x01'
  co_name:      func
  co_names:     ()
  co_nlocals:   2
  co_positions: <built-in method co_positions of code object at 0x7fba5e04f5d0>
  co_posonlyargcount:   0
  co_qualname:  func
  co_stacksize: 2
  co_varnames:  ('x', 'y')
  replace:      <built-in method replace of code object at 0x7fba5e04f5d0>
co_name:        deractor
  co_argcount:  1
  co_cellvars:  ('func',)
  co_code:      b'\x87\x00\x97\x00\x88\x00f\x01d\x01\x84\x08}\x01|\x01S\x00'
  co_consts:    (None, <code object wrapper at 0x7fba5e0b1e30, file "cbt", line 9>)
  co_exceptiontable:    b''
  co_filename:  cbt
  co_firstlineno:       8
  co_flags:     3
  co_freevars:  ()
  co_kwonlyargcount:    0
  co_lines:     <built-in method co_lines of code object at 0x7fba5df36320>
  co_linetable: b'\xf8\x80\x00\xf0\x02\x02\x05%\xf0\x00\x02\x05%\xf0\x00\x02\x05%\xf0\x00\x02\x05%\xf0\x00\x02\x05%\xf0\x06\x00\x0c\x13\x80N'
  co_lnotab:    b'\x04\x01\n\x03'
  co_name:      deractor
  co_names:     ()
  co_nlocals:   2
  co_positions: <built-in method co_positions of code object at 0x7fba5df36320>
  co_posonlyargcount:   0
  co_qualname:  deractor
  co_stacksize: 2
  co_varnames:  ('func', 'wrapper')
  replace:      <built-in method replace of code object at 0x7fba5df36320>
co_name:        wrapper
  co_argcount:  0
  co_cellvars:  ()
  co_code:      b'\x95\x01\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x89\x02|\x00i\x00|\x01\xa4\x01\x8e\x01S\x00'
  co_consts:    (None, 'wrapper')
  co_exceptiontable:    b''
  co_filename:  cbt
  co_firstlineno:       9
  co_flags:     31
  co_freevars:  ('func',)
  co_kwonlyargcount:    0
  co_lines:     <built-in method co_lines of code object at 0x7fba5e0b1e30>
  co_linetable: b'\xf8\x80\x00\xdd\x08\r\x88i\xd1\x08\x18\xd4\x08\x18\xd0\x08\x18\xd8\x0f\x13\x88t\x90T\xd0\x0f$\x98V\xd0\x0f$\xd0\x0f$\xd0\x08$'
  co_lnotab:    b'\x04\x01\x1e\x01'
  co_name:      wrapper
  co_names:     ('print',)
  co_nlocals:   2
  co_positions: <built-in method co_positions of code object at 0x7fba5e0b1e30>
  co_posonlyargcount:   0
  co_qualname:  deractor.<locals>.wrapper
  co_stacksize: 5
  co_varnames:  ('args', 'kwargs')
  replace:      <built-in method replace of code object at 0x7fba5e0b1e30>
co_name:        F
  co_argcount:  0
  co_cellvars:  ()
  co_code:      b'\x97\x00e\x00Z\x01d\x00Z\x02d\x01S\x00'
  co_consts:    ('F', None)
  co_exceptiontable:    b''
  co_filename:  cbt
  co_firstlineno:       14
  co_flags:     0
  co_freevars:  ()
  co_kwonlyargcount:    0
  co_lines:     <built-in method co_lines of code object at 0x7fba5df36f50>
  co_linetable: b'\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\xd8\x04\x08\x80D'
  co_lnotab:    b'\n\x01'
  co_name:      F
  co_names:     ('__name__', '__module__', '__qualname__')
  co_nlocals:   0
  co_positions: <built-in method co_positions of code object at 0x7fba5df36f50>
  co_posonlyargcount:   0
  co_qualname:  F
  co_stacksize: 1
  co_varnames:  ()
  replace:      <built-in method replace of code object at 0x7fba5df36f50>
"""