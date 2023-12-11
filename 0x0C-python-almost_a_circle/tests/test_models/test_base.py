#!/usr/bin/python3
"""
Testing module for the calsses Base , Rectangles
In this module we will test all the available Functionalities
and Comme up with adequate testes
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBaseIdValidValues(unittest.TestCase):
    """
    TestBaseIdValidValues is a class that test
    id valid values and make sure that we get
    good information out of it
    """

    def setUp(self):
        """Set up the start of objects"""
        Rectangle.set_nb_objects()

    def test_id_two_classes(self):
        """
        test the output of two classes indexes
        """

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_three_classes(self):
        """
        test the output of three classes
        """

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_provided(self):
        """
        test with provided id in
        the object creation
        """

        b1 = Base(12)
        b2 = Base(-12)
        b3 = Base(-15)
        b4 = Base()
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, -12)
        self.assertEqual(b3.id, -15)
        self.assertEqual(b4.id, 1)

    def test_to_json_string(self):
        """Test the to json string static method"""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        expected_output = json.dumps([dictionary])
        actual_output = Base.to_json_string([dictionary])
        self.assertEqual(expected_output, actual_output)

        r = Rectangle(10, 7)
        dictionary = r.to_dictionary()
        expected_output = json.dumps([dictionary])
        actual_output = Base.to_json_string([dictionary])
        self.assertEqual(expected_output, actual_output)

        r = Rectangle(10, 7, 2, 8, 13)
        dictionary = r.to_dictionary()
        expected_output = json.dumps([dictionary])
        actual_output = Base.to_json_string([dictionary])
        self.assertEqual(expected_output, actual_output)

        dictionary = []
        actual_output = Base.to_json_string([dictionary])
        expected_output = json.dumps([dictionary])
        self.assertEqual(expected_output, actual_output)

        dictionary = [{}]
        actual_output = Base.to_json_string([dictionary])
        expected_output = json.dumps([dictionary])
        self.assertEqual(expected_output, actual_output)

        dictionary = [{}, {"age": 23, "name": "Arsene"}, {}]
        actual_output = Base.to_json_string([dictionary])
        expected_output = json.dumps([dictionary])
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
