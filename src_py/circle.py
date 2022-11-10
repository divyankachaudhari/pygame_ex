import math


class Circle:
    def __init__(self, x, y, r):
        self.x: int
        self.y: int
        self.r: int
        self.x = x
        self.y = y
        self.r = r
        self.diameter = 2 * self.r
        self.area = math.pi * (self.r**2)
        self.circumference = math.pi * self.diameter

    def collidePoint(self, point):
        """checking the collision of cirlce with a point"""
        return (self.x - point[0]) ** 2 + (self.y - point[1]) ** 2 <= (self.r) ** 2

    def collideCircle(self, circle2):
        """checking the collision of cirlce with another circle"""
        return (self.x - circle2.x) ** 2 + (self.y - circle2.y) ** 2 <= (
            self.r + circle2.r
        ) ** 2

    def collideRect(self, rect):
        """checking the collision of cirlce with a rect"""
        r_x = self.x
        r_y = self.y
        if self.x < rect.x:
            r_x = rect.x
        elif self.x > rect.right:
            r_x = rect.right
        if self.y < rect.y:
            r_y = rect.y
        elif self.y > rect.bottom:
            r_y = rect.bottom
        return (self.x - r_x) ** 2 + (self.y - r_y) ** 2 <= (self.r) ** 2

    def copy(self):
        """Returns a copy of the circle"""
        return Circle(self.x, self.y, self.r)

    def move_ip(self, x, y):
        """moves the circle, in place"""
        self.x = self.x + x
        self.y = self.y + y

    def move(self, x, y):
        """Returns a copy of the circle moved"""
        return Circle(self.x + x, self.y + y, self.r)

    def inflate(self, r):
        """Returns a copy of the circle inflated"""
        return Circle(self.x, self.y, self.r + r)

    def inflate_ip(self, r):
        """Inflates the circle in place"""
        self.r += r

    def update(self, x, y, r):
        """Updates the circle, in place"""
        self.x = x
        self.y = y
        self.r = r

    # Rect only has Clamp, to clamp a rectangle inside another rectangle
    # However, we have split it into 2 different functions
    # ClampRect and ClampCircle, clamps our circle into a rectangle and circle respectively
    def clampRect(self, rect):
        """moves the circle inside the argument rect"""
        return Circle(rect.x, rect.y, self.r)

    def clampCircle(self, circle):
        """moves the circle inside the argument circle"""
        return Circle(circle.x, circle.y, self.r)

    def clampRect_ip(self, rect):
        """moves the circle inside the argument rect, in place"""
        self.x = rect.x
        self.y = rect.y

    def clampCircle_ip(self, circle):
        """moves the circle inside the argument circle, in place"""
        self.x = circle.x
        self.y = circle.y

    """Clip not possible in circle. it's possible in rectangle because the overlapping area of any two rectangles is also a rectangle. in circle it's a shape called Vesica piscis"""

    def union(self, B):
        """Returns the smallest circle that contains both circles"""
        dx = self.x - B.x
        dy = self.y - B.y
        d = math.sqrt(dx * dx + dy * dy)
        if d <= abs(self.r - B.r):
            if self.r > B.r:
                return self.copy()
            else:
                return B.copy()
        else:
            r = (d + self.r + B.r) / 2
            return Circle(
                (self.x + B.x) / 2 + (B.x - self.x) * (r - self.r) / d,
                (self.y + B.y) / 2 + (B.y - self.y) * (r - self.r) / d,
                r,
            )

    def union_ip(self, B):
        """Returns the smallest circle that contains both circles, in place"""
        dx = self.x - B.x
        dy = self.y - B.y
        d = math.sqrt(dx * dx + dy * dy)
        if d <= abs(self.r - B.r):
            if self.r > B.r:
                return self.copy()
            else:
                return B.copy()
        else:
            r = (d + self.r + B.r) / 2
            self.x = (self.x + B.x) / 2 + (B.x - self.x) * (r - self.r) / d
            self.y = (self.y + B.y) / 2 + (B.y - self.y) * (r - self.r) / d
            self.r = r

    def unionAll(self, circles):
        """Returns the smallest circle that contains all circles"""
        if len(circles) == 0:
            return None
        elif len(circles) == 1:
            return circles[0].copy()
        else:
            circle = circles[0].copy()
            for i in range(1, len(circles)):
                circle = circle.union(circles[i])
            return circle

    def unionAll_ip(self, circles):
        """Returns the smallest circle that contains all circles, in place"""
        if len(circles) == 0:
            return None
        elif len(circles) == 1:
            return circles[0].copy()
        else:
            for i in range(1, len(circles)):
                self.union_ip(circles[i])
            return self

    def contains(self, B):
        """Returns True if the circle contains the argument circle"""
        dx = self.x - B.x
        dy = self.y - B.y
        return math.sqrt(dx * dx + dy * dy) + B.r <= self.r
