# 生成新的 task 时的命名计数器
# 这里不采用 +=1 的操作是因为协程并非线程安全
# 通过迭代器不断的向后计数，可以完美的保证线程安全（Ps: GET 新技能）
import itertools


_task_name_counter = itertools.count(1).__next__

_task_name_counter()