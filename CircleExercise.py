
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

