# encoding: utf-8
class Parent(object):
    def eat(self):
        print("\tparent --- 爱吃饭")

class Son1(Parent):
    def eat(self):
        print("son1 --- eat()")
        super().eat()
        print("\tson1  ---  爱吃蔬菜\n")

class Son2(Parent):
    def eat(self):
        print("son2 --- eat()")
        super().eat()
        print("\tson2  ---  爱吃水果\n")

class Grandson(Son1, Son2):
    def eat(self):
        print("grandson --- eat()")
        super().eat()
        print("\tgrandson --- 爱吃零食")
    
    def eat2(self):
        return super(Son1, self).eat()

if __name__ == '__main__':
    g = Grandson()
    print(Grandson.__mro__) # (<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <type 'object'>)

    g.eat()
    """
    grandson --- eat()
    son1 --- eat()
    son2 --- eat()
            parent --- 爱吃饭
            son2  ---  爱吃水果

            son1  ---  爱吃蔬菜

            grandson --- 爱吃零食
    """
    # g.eat2()
    """
    son2 --- eat()
        parent --- 爱吃饭
        son2  ---  爱吃水果
    """

