# 切片操作
class MyList(object):

    def __init__(self):
        self.mlist = list()

    def __getitem__(self, index):
        print('__getitem__() called  ', locals())
        if isinstance(index, slice):
            return self.mlist[index]

    def __setitem__(self, index, value):
        print('__getitem__() called  ', locals())
        if isinstance(index, slice):
            self.mlist[index] = value

    def __delitem__(self, index):
        print('__delitem__() called  ', locals())
        if isinstance(index, slice):
            del self.mlist[index]

l = MyList()

# l[0]                # {'index': 0}
# l[::-1]             # {'index': slice(None, None, -1)}
# l[0:10:1]           # {'index': slice(0, 10, 1)}

# l[1:2,2:3,3:4]      # {'index': (slice(1, 2, None), slice(2, 3, None), slice(3, 4, None))}
# l[1:2,...,3:4]      # {'index': (slice(1, 2, None), Ellipsis, slice(3, 4, None))}
# l[1:2,...,3:4,...]  # {'index': (slice(1, 2, None), Ellipsis, slice(3, 4, None), Ellipsis)}

# l[1:...]            # {'index': slice(1, Ellipsis, None)}


l = [[1],[2],[3]]
sl = l[::2]
print(sl)           # [[1], [3]]
for p in sl:
    p.append(0)
print(sl)           # [[1, 0], [3, 0]]
print(l)            # [[1, 0], [2], [3, 0]]
sl[1] = "10086"
print(sl)           # [[1, 0], '10086']
print(l)            # [[1, 0], [2], [3, 0]]