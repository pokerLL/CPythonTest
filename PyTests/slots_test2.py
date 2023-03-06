"""
>>> A.a
<member 'a' of 'A' objects>
>>> type(A.a) 
<class 'member_descriptor'>
>>> type(a.a) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: a
>>> a.a = 1
>>> A.a
<member 'a' of 'A' objects>
>>> a.a
1
>>> A.a = 2
>>> a.a
2
"""

class A:
    __slots__ = ['a','b','c']

a = A()
# a.a = 1
# print(a.a)  # 1
# print(A.a)  # <member 'a' of 'A' objects>
# A.a = 2
# print(a.a)  # 2
# print(A.a)  # 2
# a.a = 1     # AttributeError: 'A' object attribute 'a' is read-only
# A.a = 3
# print(a.a)  # 3
# print(A.a)  # 3

A.d = 4
print(a.d)  # 4
print(A.d)  # 4

# a.e = 4     # AttributeError: 'A' object has no attribute 'e'
# print(a.e)  # AttributeError: 'A' object has no attribute 'e'
# print(A.e)  # AttributeError: type object 'A' has no attribute 'e'