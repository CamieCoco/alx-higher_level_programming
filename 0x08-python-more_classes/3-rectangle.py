#!/usr/bin/python3
"""3-rectangle.py
this module makes an empty class Rectangle that defines a rectangle"""


class Rectangle:
    '''an empty class Rectangle that defines a rectangle by:
    (basen on 2-rectangle.py)'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width + self.__height) * 2)

    def __str__(self):
        empty_string = ""
        if self.__height != 0 and self.__width != 0:
            empty_string = "".join(("#" * self.__width + "\n") * self.__height)
            empty_string = empty_string[:-1]
        return(empty_string)
