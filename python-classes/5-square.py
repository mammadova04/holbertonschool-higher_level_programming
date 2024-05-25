#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0) -> None:
        """Initialize Square with size attribute"""
        self.size = size  # Use the property setter to set the size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with the character #."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
