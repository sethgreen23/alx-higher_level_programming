#!/usr/bin/python3
"""Rectangle class Module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init function that allow the creation of rectangle object
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Method to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set a value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Method to get the value to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set a value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method to get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method to set the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method to get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method to set the value to y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of a rectangle"""
        return self.height * self.width

    def display(self):
        """Print the rectangle with the character #"""
        for _ in range(self.y):
            print()
        i = self.height
        while (i > 0):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()
            i -= 1

    def __str__(self):
        """String representation of a rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

    def update(self, *args, **kwargs):
        """Update the instance of the object"""
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                if i == 1:
                    self.width = value
                if i == 2:
                    self.height = value
                if i == 3:
                    self.x = value
                if i == 4:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of a Rectangle"""
        obj_dict = {}
        for key, value in self.__dict__.items():
            words = key.split("__")
            if "id" in words:
                obj_dict["id"] = value
            elif "width" in words:
                obj_dict["width"] = value
            elif "height" in words:
                obj_dict["height"] = value
            elif "x" in words:
                obj_dict["x"] = value
            elif "y" in words:
                obj_dict["y"] = value
        return obj_dict
