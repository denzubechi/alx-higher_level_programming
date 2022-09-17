#!/usr/bin/python3
class Square:
    """ `Square` class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes private instance
            positive integer `size` and `position` """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple) \
           or len(position) != 2 \
           or any(map(lambda x: not isinstance(x, int), position)) \
           or any(map(lambda x: x < 0, position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """ getter for `__size` """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for `__size` """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ getter for `__position` """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter for `__position` """
        if not isinstance(value, tuple) \
           or len(value) != 2 \
           or any(map(lambda x: not isinstance(x, int), value)) \
           or any(map(lambda x: x < 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculates instance area """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with `#`s.
            Should probably be a `__repr__`. """
        row = (' ' * self.__position[0]) + ('#' * self.__size) + '\n'
        if self.__size > 0:
            print('\n' * self.__position[1], end="")
            print(row * self.__size, end="")
        else:
            print()
