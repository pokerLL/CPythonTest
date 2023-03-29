list_ = list(range(10))
idx = 0
for i in list_:
    print(f'{idx} -- {i} -- {list_}')
    list_.pop(0)
    idx += 1

'''
0 -- 0 -- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
1 -- 2 -- [1, 2, 3, 4, 5, 6, 7, 8, 9]
2 -- 4 -- [2, 3, 4, 5, 6, 7, 8, 9]
3 -- 6 -- [3, 4, 5, 6, 7, 8, 9]
4 -- 8 -- [4, 5, 6, 7, 8, 9]
'''


# bad case
# 过滤大于 4 的元素
a = [3, 4, 5, 6]
for i in a:
    if i >= 4:
        a.remove(i)

print(a)    # [3, 5]

# bad case
# 过滤大于 4 的元素
a = [3, 4, 5, 6]
for i in a:
    a.remove(i)
    print(f"{i} -- {a}")
print(a)
"""
3 -- [4, 5, 6]
5 -- [4, 6]
[4, 6]
"""