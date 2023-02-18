def de(cls):
    print(cls.a)
    cls.p = 3
    return cls

@de
class A:
    a = 1

print(A.p)

# print(__module__)
print(A.__module__)
# def dec(fun):
#     print("IN DEC")
#     print("func_name: ",fun.__name__)
#     return "something from dec"


# def f():
#     print("IN F")

# f = dec(f)

# print(f)


# def AA(func):
#     print('AA 1')
#     def func_a(*args, **kwargs):
#         print('AA 2')
#         return func(*args, **kwargs)
#     return func_a

# def BB(func):
#     print('BB 1')
#     def func_b(*args, **kwargs):
#         print('BB 2')
#         return func(*args, **kwargs)
#     return func_b

# # @BB
# # @AA
# def f(x):
#     print('F')
#     return x * 10

# ## 等价于
# BB(AA(f))