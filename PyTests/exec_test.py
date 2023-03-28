## GLOBAL
g = 1
print(globals())    # {'g': 1}
exec('g = 2')
exec('g2 = 1')
print(globals())    # {'g': 2, 'g2': 1}
print(g)            # 2
print(g2)           # 1
globals()
print(globals())    # {'g': 2, 'g2': 1}
print(g)            # 2
print(g2)           # 1


print('func1 ##################################')
## Local - Unchanged
def func1():
    l1 = 1
    print(locals()) # {'l1': 1}
    exec('l1 = 2')
    exec('ll1 = 1')
    print(locals()) # {'l1': 1}

func1()


print('func2 ##################################')
## Local
def func2():
    l2 = 1
    loc = locals()
    print(loc)      # {'l2': 1}
    exec('l2 = 2')
    # exec('ll2  = 1')
    print(loc)      # {'l2': 1, 'loc': {...}, 'll2': 1} 
    print(locals()) # {'l2': 1, 'loc': {...}, 'll2': 1}
    # print(ll2)      # NameError: name 'll2' is not defined
    print(locals().get('ll2'))  # 1

func2()


print('func3 ##################################')
def func3():
    x = 0
    loc = locals()
    print(loc)          # {'x': 0}
    exec('x += 1')      # {'x': 1, 'loc': {...}}
    print(loc)
    locals()            # {'x': 0, 'loc': {...}}
    print(loc)

func3()



print('func4 ##################################')
## Local
def func4():
    l2 = 1
    loc = locals()
    print(loc)      # {'l2': 1}
    exec('l2 = 2')
    print(loc)      # {'l2': 2, 'loc': {...}}
    print(locals()) # {'l2': 1, 'loc': {...}}
    print(l2)       # 1

func4()

"""
>>> dis.dis('exec("a=1")') 
  1           0 LOAD_NAME                0 (exec)
              2 LOAD_CONST               0 ('a=1')
              4 CALL_FUNCTION            1
              6 RETURN_VALUE

exec(source, globals=None, locals=None, /)
    Execute the given source in the context of globals and locals.

    The source may be a string representing one or more Python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
"""