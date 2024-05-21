#!/usr/bin/python3

"""Define a class rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):

        """Initialize rectangle.

        Args:
            width(int) = width of rectangle.
            height(int) = height of rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the current width of rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get/set the current height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
