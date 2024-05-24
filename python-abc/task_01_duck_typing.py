#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod    
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")

        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
def shape_info(Shape):

    area = Shape.area()
    perimeter = Shape.perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
