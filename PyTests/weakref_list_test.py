import random
import weakref

ITEM_NUM = 10000000
ITEM_NUM = 0

class MyList(list):
    pass

l = MyList()
addr = set()
for i in range(ITEM_NUM):
    _i = random.randint(0,10**100)
    l.append(_i)
    if id(l) not in addr:
        print(f"ADDR CHANGE  {i}/{ITEM_NUM} {id(l)}")
        addr.add(id(l))
"""
ADDR CHANGE  0/10000000 2282120903800
"""

l = []
addr = set()
for i in range(ITEM_NUM):
    _i = random.randint(0,10**100)
    l.append(_i)
    if id(l) not in addr:
        print(f"ADDR CHANGE  {i}/{ITEM_NUM} {id(l)}")
        addr.add(id(l))
"""
ADDR CHANGE  0/10000000 2282093917000
"""

print(MyList.__mro__) # (<class '__main__.MyList'>, <class 'list'>, <class 'object'>)
print("MRO:",[c for c in MyList.__mro__ if "__weakref__" in c.__dict__])    # MRO: [<class '__main__.MyList'>]

# l1 = list()
# weakref.ref(l1)
"""
Traceback (most recent call last):
  File "d:/Programs/Workspace/cpython-v3.7.4/PyTests/weakref_list_test.py", line 38, in <module>
    weakref.ref(l1)
TypeError: cannot create weak reference to 'list' object
"""
l2 = MyList()
weakref.ref(l2)