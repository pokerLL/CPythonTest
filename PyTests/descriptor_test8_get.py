from utils import debug

class MyDescriptor:

    @debug
    def __get__(self, instance, owner):
        pass

    @debug
    def __set__(self, instance, value):
        pass


a = MyDescriptor()
a
a = 1
# 啥都没有...
"""
"""