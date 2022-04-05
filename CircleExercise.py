
from functools import total_ordering
from math import pi


@total_ordering
class Circle(object):
    
    @property
    def area(self):
        return pi * self.radius**2
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @classmethod
    def from_diameter(self, *,diameter):
        return Circle(radius=diameter / 2)
    
    def __init__(self,*, radius):
        if radius < 0:
            raise ValueError
        self.radius = radius
        
    def __str__(self):
        return f"CIRCLE PRINT:\nradius: {self.radius}\ndiameter: {self.diameter}\narea: {self.area}\n"
    
    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius

