from collections import Iterable

def flatten(items, ignore_type=(str,bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_type):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8, "999"]
for x in flatten(items):
    print(x, end=' ')
# 1 2 3 4 5 6 7 8 999 