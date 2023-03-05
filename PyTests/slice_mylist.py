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

l[0]
l[::-1]
l[0:10:1]