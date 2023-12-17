s = "FFFFF"

def func(x, y):
    if x == y:
        return 0
    return 1

class F:
    pass

func()


""" 
>>> text = open("./PyTests/codeobj_test1.py", 'r').read()
>>> text
's = "FFFFF"\n\ndef func(x, y):\n    if x == y:\n        return 0\n    return 1\n\nclass F:\n    pass\n\nfunc()\n\n\n'
>>> code = compile(text, 'cbt', 'exec')
>>> code
<code object <module> at 0x7ff04eaa2d20, file "cbt", line 1>
>>> def print_code(co):
    print(f'co_name:\t{co.co_name}')
    for attr in dir(co):
        if attr[0] != '_':
            print(f'  {attr}:\t{getattr(co,attr)}')
... 
>>> 
>>> def dfs(co):
    print_code(co)
    for c in co.co_consts:
        if isinstance(c, types.CodeType):
            dfs(c)
... 
>>> 
>>> import types
>>> dfs(code)
co_name:        <module>
  co_argcount:  0
  co_cellvars:  ()
  co_code:      b'd\x00Z\x00d\x01d\x02\x84\x00Z\x01G\x00d\x03d\x04\x84\x00d\x04\x83\x02Z\x02e\x01\x83\x00\x01\x00d\x05S\x00'
  co_consts:    ('FFFFF', <code object func at 0x7ff04eaa2780, file "cbt", line 3>, 'func', <code object F at 0x7ff04eaa2c90, file "cbt", line 8>, 'F', None)
  co_filename:  cbt
  co_firstlineno:       1
  co_flags:     64
  co_freevars:  ()
  co_kwonlyargcount:    0
  co_lnotab:    b'\x04\x02\x08\x05\x0e\x03'
  co_name:      <module>
  co_names:     ('s', 'func', 'F')
  co_nlocals:   0
  co_stacksize: 3
  co_varnames:  ()
co_name:        func
  co_argcount:  2
  co_cellvars:  ()
  co_code:      b'|\x00|\x01k\x02r\x0cd\x01S\x00d\x02S\x00'
  co_consts:    (None, 0, 1)
  co_filename:  cbt
  co_firstlineno:       3
  co_flags:     67
  co_freevars:  ()
  co_kwonlyargcount:    0
  co_lnotab:    b'\x00\x01\x08\x01\x04\x01'
  co_name:      func
  co_names:     ()
  co_nlocals:   2
  co_stacksize: 2
  co_varnames:  ('x', 'y')
co_name:        F
  co_argcount:  0
  co_cellvars:  ()
  co_code:      b'e\x00Z\x01d\x00Z\x02d\x01S\x00'
  co_consts:    ('F', None)
  co_filename:  cbt
  co_firstlineno:       8
  co_flags:     64
  co_freevars:  ()
  co_kwonlyargcount:    0
  co_lnotab:    b'\x08\x01'
  co_name:      F
  co_names:     ('__name__', '__module__', '__qualname__')
  co_nlocals:   0
  co_stacksize: 1
  co_varnames:  ()
"""