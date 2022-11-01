import math

class Circle:
    def __init__(self,x,y,r):
        self.x : int
        self.y : int
        self.r : int
        self.x=x
        self.y=y
        self.r=r
        self.diameter = 2*self.r
        self.area = math.pi * (self.r**2)
        self.circumference = math.pi * self.diameter