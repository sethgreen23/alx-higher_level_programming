#!/usr/bin/python3
"""Square module for the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square represent a square

    Parameters:
        size (int): size of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a square object
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the object Square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.height)

    @property
    def size(self):
        """Getter for the size value"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Apdate the instance of the object"""
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                if i == 1:
                    self.size = value
                if i == 2:
                    self.x = value
                if i == 3:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
