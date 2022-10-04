#!/usr/bin/python3
"""
Inherits from the Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Defining a Rectangle class
    private instance attributes:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initisalizing class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Set/get width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        validating setter method
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Set/get height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        validating setter method
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Set/get x value of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        validating setter method
        """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Set/get y value of the Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        validating setter method
        """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        defining area method
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character #
        """
        for x in range(self.__y):
            print()

        for y in range(self.__height):
            for z in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Update the class Rectangle by overriding
        the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle
        """
        attbt = ["id", "width", "height", "x", "y"]
        i = 0

        if args is not None and len(args) > 0:
            for arg in args:
                if i < 5:
                    setattr(self, attbt[i], arg)
                    i += 1

        elif (kwargs is not None):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle
        """
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })
