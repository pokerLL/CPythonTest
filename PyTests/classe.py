class Point:
    z = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
p = Point(1, 2)