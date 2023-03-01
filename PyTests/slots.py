class A:
    __slots__ = ['a','b','c']

class B:
    pass


A.__dict__

print(B.__dict__)
