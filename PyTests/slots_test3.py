"""
>>> obj
<slots_test3.MyClass object at 0x00000268E1BE92C8>
>>> obj.x
2
>>> type(obj.x) 
<class 'int'>
>>> type(MyClass.x) 
<class 'int'>
"""

class MyClass:
    x = 1

obj = MyClass()
obj.x = 2

print(MyClass.x)    # 1
print(obj.x)        # 2
print(MyClass.x)    # 1