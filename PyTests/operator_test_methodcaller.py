import math
import operator

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def distance(self,x,y):
        return math.hypot(self.x-x,self.y-y)

p = Point(2, 3)

d1 = getattr(p, 'distance')(0,0)
d2 = operator.methodcaller("distance", 0, 0)(p)
print(d1,d2)    # 3.605551275463989 3.605551275463989