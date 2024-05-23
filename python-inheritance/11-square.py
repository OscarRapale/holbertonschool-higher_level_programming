#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle class """

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of Square object"""
        return super().area()

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        rectangle_str = super().__str__()
        square_str =  rectangle_str.replace("Rectangle", "Square")
        return square_str
