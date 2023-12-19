import pdb

def func(a, b):
    pdb.set_trace()  # 设置断点
    sum = 0
    for i in range(b):
        sum += a
    return sum

x = 5
y = 3
z = func(x, y)
print(z)

"""
一旦进入调试模式，你可以使用 `pdb` 提供的命令来检查变量、执行代码和跟踪代码执行流程。以下是一些常用的命令：

* `l [<line>]` 或 `list`: 显示当前代码/<line>上下文的片段, 多次执行则显示更多。
* `n` 或 `next`: 执行下一行代码，如果有函数调用则执行函数调用（不进入）。
* `c` 或 `continue`: 继续执行代码直到下一个断点。
* `p` 或 `print`: 打印变量的值。
* `s` 或 `step`: 逐步执行代码，如果有函数调用，则进入函数内部。
* `q` 或 `quit`: 退出调试器。
* `w` 或 `where`: 显示当前调用栈。
* `u` 或 `up`: 移动到当前调用栈的上一层。
* `a` 或 `args`: 打印当前函数的参数列表。
* `r` 或 `return`: 执行代码直到从当前函数返回。
* `unt <line>`: 执行代码直到指定行。
* `b <line>`: 在指定行设置断点。
* `cl <line>`: 清除指定行的断点。
* `help <command>`: 显示指定命令的帮助信息。
"""