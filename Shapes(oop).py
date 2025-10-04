from abc import ABC, abstractmethod
import math
#fdghdfjgh
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

shapes = [Rectangle(3,4), Circle(2)]
for shape in shapes:
    print(f'Area : {shape.area():.2f}')
