from abc import ABCMeta,abstractmethod

class A:
    a =  1
    @abstractmethod
    def fun(self):
        print(locals())
        pass

a = A()
print(a.a)
print(a.fun())

class B(metaclass=ABCMeta):
    b =  1
    @abstractmethod
    def fun(self):
        print(locals())
        pass

b = B()
"""
    b = B()
TypeError: Can't instantiate abstract class B with abstract methods fun
"""
# print(b.b)
# print(b.fun())
