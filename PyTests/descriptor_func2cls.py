from functools import partial


class kls:
    def __init__(self, func) -> None:
        self.func = func
        pass

    def __call__(self, *args, **kwargs):
        print(f"kls call  - {args} - {kwargs}")
        return self.func(*args, **kwargs)
    
    def __get__(self, ins, obj):
        return partial(self.__call__, ins)

def de(f):
    def df(*args, **kwargs):
        print(f"you are kalami - {f.__name__} - {args} - {kwargs}")
        return "you are kalami"
    return df

def dw(f):
    return kls(f)

class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def f(self, c):
        return self.a + self.b + c
  
    @de
    def g(self, d):
        return self.a + self.b + d
  
    @dw
    def h(self, e):
        return self.a + self.b + e


a = A()

# print(a.f(3))
# print(a.g(4))
print(a.h(4))

"""
6
you are kalami - g - (<__main__.A object at 0x7fbde668ae50>, 4) - {}
you are kalami
kls call  - (<__main__.A object at 0x7fbde668ae50>, 4) - {}
7
"""
