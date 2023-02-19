import inspect

def debug(func):
    def wrapper(*args, **kwargs):
        # 获取函数名称
        function_name = func.__name__
        # 获取局部变量
        local_vars = inspect.currentframe().f_back.f_locals
        # 打印函数名和局部变量
#         print(f"""
# Calling {function_name} 
#     with args: {args} 
#     kwargs: {kwargs} 
#     local variables: {local_vars}
    
#         """)

        return func(*args, **kwargs)
    return wrapper


class Property:
    @debug
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    @debug
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    @debug
    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    @debug
    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    @debug
    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)
    
    @debug
    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)
    
    @debug
    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @Property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @Property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @Property
    def area(self):
        return self._width * self._height


r = Rectangle(3, 4)

print(r.width)  # Output: 3


print(r.height)  # Output: 4
print(r.area)  # Output: 12

r.width = 5
print(r.width)  # Output: 5
print(r.area)  # Output: 20

del r.height
print(r.height)  # Raise AttributeError: can't delete attribute