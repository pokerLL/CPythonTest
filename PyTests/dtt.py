# decorator test
def AA(func):
    print('AA OUTER')
    def func_a(*args, **kwargs):
        print('AA INNER BEFORE')
        res = func(*args, **kwargs)
        print('AA INNER AFTER')
        return res
    return func_a

def BB(func):
    print('BB OUTER')
    def func_b(*args, **kwargs):
        print('BB INNER BEFORE')
        res = func(*args, **kwargs)
        print('BB INNER AFTER')
        return res
    return func_b

@BB
@AA
def f(x):
    print('F CALLED')
    return x * 10

## 完全等价于
# f = BB(AA(f))

# 在调用被装饰的函数之前输出-即即使注释掉下面对f的调用也会输出
# AA OUTER
# BB OUTER

print(f(1))

# BB INNER BEFORE
# AA INNER BEFORE
# F CALLED
# AA INNER AFTER
# BB INNER AFTER
# 10