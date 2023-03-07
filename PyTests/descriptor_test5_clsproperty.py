# from utils import debug
# from functools import wraps
#
# class ClassMethod(object):
#     "Emulate PyClassMethod_Type() in Objects/funcobject.c"
#
#     @debug
#     def __init__(self, f):
#         self.f = f
#
#     @debug
#     def __get__(self, obj, klass=None):
#         assert obj is None and klass is not None
#         def newfunc(*args):
#             return self.f(klass, *args)
#         return newfunc
#
# @debug
# def clsproperty(*args,**kwargs):
#     func = args[0]
#     func_name = func.__name__
#
#     @debug
#     def inner(cls, *args, **kwargs):
#         # cls.func_name = func(cls, *args, **kwargs)
#         setattr(cls, func_name, func(cls, *args, **kwargs))
#
#     return inner
#
#
#
#
# class ClsProperty:
#     def __init__(self, f):
#         self.f = f
#         pass
#
#     def __get__(self, instance, owner):
#         assert instance is None and owner is not None
#         func_name = self.f.__name__
#         clsp_name = f"clsp_{func_name}"
#         if clsp_name not in owner.__dict__:
#             setattr(owner, clsp_name, self.f(owner))
#         return getattr(owner, clsp_name)


class A:

    # @ClassMethod
    # @clsproperty
    # @ClsProperty
    # @debug
    def fun(*args, **kwargs):
        return 10086

A.fun
getattr(A, 'fun')


# A.fun()
# print(A.__dict__.items())
# print(A.fun)
# print(A.__dict__.items())
# a = A()
# a.fun()

