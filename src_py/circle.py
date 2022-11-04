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
        '''checking the collision of cirlce with a point'''
        return (self.x - point[0])** 2 + (self.y - point[1])**2 <= (self.r)**2


    def collideCircle(self, circle2):
        '''checking the collision of cirlce with another circle'''
        return (self.x - circle2.x)**2 + (self.y - circle2.y)**2 <= (self.r + circle2.r)**2


    def collideRect(self, rect):
        '''checking the collision of cirlce with a rect'''
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

    def copy(self):
        '''Returns a copy of the circle'''
        return Circle(self.x, self.y, self.r)
    
    def move_ip(self, x, y):
        '''Moves the circle, in place'''
        self.x = self.x + x
        self.y = self.y + y
    
    def move(self, x, y):
        '''Returns a copy of the circle moved'''
        return Circle(self.x + x,self.y + y, self.r)
    
    def inflate(self, r):
        '''Returns a copy of the circle inflated'''
        return Circle(self.x, self.y, self.r + r)
    
    def inflate_ip(self, r):
        '''Inflates the circle in place'''
        self.r += r
    
    def update(self, x, y, r):
        '''Updates the circle, in place'''
        self.x = x
        self.y = y
        self.r = r

    # Rect only has Clamp, to clamp a rectangle inside another rectangle
    # However, we have split it into 2 different functions
    # ClampRect and ClampCircle, clamps our circle into a rectangle and circle respectively
    