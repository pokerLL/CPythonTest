# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value

# A class with a descriptor
class Person:
    name = String('name')

    def __init__(self, name):
        self.name = name            # 等同于 Person.name.__set__(Person.name, self, name)


p =  Person()
p.name = "Lei"      # 等同于 Person.name.__set__(Person.name, p, "Lei")
p.name              # 等同于 Person.name.__get__(Person.name, p ,type(p))