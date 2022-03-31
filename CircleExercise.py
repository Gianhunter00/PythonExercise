
from math import pi

class Circle(object):
    def __init__(self, radius=-1, diameter=-1):
        self.radius, self.diameter = (radius, radius*2) if radius != -1 else (diameter * 0.5, diameter)
        self.area = pi * self.radius**2
        
    def __str__(self):
        return f"CIRCLE PRINT:\nradius: {self.radius}\ndiameter: {self.diameter}\narea: {self.area}\n"
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def sort(self):
        return self.radius
    
    
circle_one = Circle(5)
circle_two = Circle(5)
circle_three = Circle(10)

print(circle_one == circle_two)
print(circle_three > circle_two)

circle_add = circle_one + circle_three

print(circle_add)

circle_list = [circle_one, circle_two, circle_three, circle_add]
circle_list.sort(key=Circle.sort)

print(*circle_list)

