#!/usr/bin/python3
"""Base class Module"""

import json
import os


class Base:
    """
    Class Base

    Parameters:
        id (int): instance attribute integer
        nb_objects (int): class attribute integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init function"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def set_nb_objects(cls):
        """Class method to set the value of nb_objest to zero"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that return string representation
        of list_dictonaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the Json string representaion of list_objs"""
        filename = "{:s}.json".format(cls.__name__)
        if list_objs is None:
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(Base.to_json_string([]))
        else:
            list_dict = []
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return list of json string represontation json_string"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        class_name = cls.__name__
        if class_name == "Rectangle":
            obj = Rectangle(1, 1)
        else:
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Return a list of instanceses"""
        from models.rectangle import Rectangle
        from models.square import Square

        objs_list = []
        class_name = cls.__name__
        filename = "{:s}.json".format(class_name)
        if os.path.isfile(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                list_dict_objs = Base.from_json_string(json_string)
                for obj in list_dict_objs:
                    if class_name == "Rectangle":
                        objs_list.append(Rectangle.create(**obj))
                    else:
                        objs_list.append(Square.create(**obj))
                return objs_list
        else:
            return []
