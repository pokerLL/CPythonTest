class MyDescriptor:
    def __get__(self, instance, owner):
        print(locals())
        if instance is not None:
            return "bound_method"
        return "function"
        

class MyClass:
    desc = MyDescriptor()

obj = MyClass()

print(MyClass.desc)     # function
print(obj.desc)         #  bound_method

MyClass.desc
obj.desc