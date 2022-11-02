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

        def collidePoint(self, point):
        return (self.x - point[0])** 2 + (self.y - point[1])**2 <= (self.r)**2


    def collideCircle(self, circle2):
        return (self.x - circle2.x)**2 + (self.y - circle2.y)**2 <= (self.r + circle2.r)**2


    def collideRect(self, rect):
        r_x = self.x
        r_y = self.y
        if (self.x < rect.x) :
                r_x = rect.x
        elif(self.x > rect.right) :
                r_x = rect.right
        if (self.y < rect.y) :
                r_y = rect.y
        elif (self.y > rect.bottom) :
                r_y = rect.bottom
        return (self.x - r_x)**2 + (self.y - r_y)**2 <= (self.r)**2
