class A:
    __slots__ = ['a','b','c']


a1 = A()
a2 = A()
# print(A.__dict__) # {'__module__': '__main__', '__slots__': ['a', 'b', 'c'], 'a': <member 'a' of 'A' objects>, 'b': <member 'b' of 'A' objects>, 'c': <member 'c' of 'A' objects>, '__doc__': None}
# print(a1.__slots__ is A.__slots__)  # True
# print(a1.__slots__ is a2.__slots__) # True
# a1.a = 1
# print(A.a)      # <member 'a' of 'A' objects>
# print(a1.a)     # 1
# print(a2.a)     # AttributeError: a

# A.a = 2
# print(a1.a)     # 2 - so why?
# print(a2.a)     # 2

# class B:
#     pass
# print(B.__dict__) # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None}


