import weakref

class MyInt(int):
    pass

i1 = int(1)
i2 = MyInt(2)
# weakref.ref(i1)
"""
Traceback (most recent call last):
  File "d:/Programs/Workspace/cpython-v3.7.4/PyTests/weakref_int.py", line 8, in <module>
    weakref.ref(i1)
TypeError: cannot create weak reference to 'int' object
"""
# weakref.ref(i2)
"""
Traceback (most recent call last):
  File "d:/Programs/Workspace/cpython-v3.7.4/PyTests/weakref_int.py", line 8, in <module>
    weakref.ref(i1)
TypeError: cannot create weak reference to 'int' object
"""

print(MyInt.__mro__)        # (<class '__main__.MyInt'>, <class 'int'>, <class 'object'>)
print("MRO:",[c for c in MyInt.__mro__ if "__weakref__" in c.__dict__])    # MRO: []