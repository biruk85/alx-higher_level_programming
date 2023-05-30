#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        """
        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
