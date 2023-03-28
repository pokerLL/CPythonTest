from utils import debug

class Parent:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return "111"
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Except a string")
        self._name = value


class Son(Parent):

    @Parent.name.setter
    def name(self, value):
        if len(value) < 10:
            raise ValueError("Name param at least 10 letters")
        super(Parent,Parent).name.__set__(self,value)


class Son2(Parent):

    @property
    def name(self):
        print("Son2 getting name")
        return super().name