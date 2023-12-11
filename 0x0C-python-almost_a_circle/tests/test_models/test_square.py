#!/usr/bin/python3
"""Test module for the Square class"""


import unittest
import sys
from models.square import Square
from io import StringIO


class TestSqureClass(unittest.TestCase):
    """
    Class for testing Square class
    """
    def setUp(self):
        """ Setup the starting values"""
        Square.set_nb_objects()

    def test_dislay(self):
        """Test the display of the class"""
        captured_output = StringIO()
        sys.stdout = captured_output
        s = Square(5)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = "[Square] (1) 0/0 - 5"
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(s.area(), 25)
        captured_output.seek(0)
        captured_output.truncate(0)
        sys.stdout = captured_output
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        s.display()
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)

        captured_output.seek(0)
        captured_output.truncate(0)
        sys.stdout = captured_output
        s = Square(3, 1, 3)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = "[Square] (2) 1/3 - 3"
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(s.area(), 9)
        captured_output.seek(0)
        captured_output.truncate(0)
        sys.stdout = captured_output
        expected_output = "\n" \
                          "\n" \
                          "\n" \
                          " ###\n" \
                          " ###\n" \
                          " ###\n"
        s.display()
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)

        captured_output.seek(0)
        captured_output.truncate(0)
        sys.stdout = captured_output
        s = Square(3, 1, 3, 12)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        expected_output = "[Square] (12) 1/3 - 3"
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(s.area(), 9)
        captured_output.seek(0)
        captured_output.truncate(0)
        sys.stdout = captured_output
        expected_output = "\n" \
                          "\n" \
                          "\n" \
                          " ###\n" \
                          " ###\n" \
                          " ###\n"
        s.display()
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_size_value(self):
        """Test for the size value of the square"""
        s = Square(5)
        captured_output = StringIO()
        sys.stdout = captured_output
        expected_output = "[Square] (1) 0/0 - 5"
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        with self.assertRaises(TypeError):
            s.size = "9"
        with self.assertRaises(TypeError):
            s.size = [1, 2, 3]
        with self.assertRaises(TypeError):
            s.size = {"age": 23}
        with self.assertRaises(ValueError):
            s.size = 0
        with self.assertRaises(ValueError):
            s.size = -100

    def test_update(self):
        """Test update function"""
        s = Square(5)
        expected_output = "[Square] (1) 0/0 - 5"
        captured_output = StringIO()
        sys.stdout = captured_output
        s.update()
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        captured_output.seek(0)
        captured_output.truncate(0)
        expected_output = "[Square] (10) 0/0 - 5"
        sys.stdout = captured_output
        s.update(10)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        captured_output.seek(0)
        captured_output.truncate(0)
        expected_output = "[Square] (1) 0/0 - 2"
        sys.stdout = captured_output
        s.update(1, 2)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        captured_output.seek(0)
        captured_output.truncate(0)
        expected_output = "[Square] (1) 3/0 - 2"
        sys.stdout = captured_output
        s.update(1, 2, 3)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        captured_output.seek(0)
        captured_output.truncate(0)
        expected_output = "[Square] (1) 3/4 - 2"
        sys.stdout = captured_output
        s.update(1, 2, 3, 4)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        captured_output.seek(0)
        captured_output.truncate(0)
        expected_output = "[Square] (1) 12/4 - 2"
        sys.stdout = captured_output
        s.update(x=12)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        captured_output.seek(0)
        captured_output.truncate(0)
        expected_output = "[Square] (1) 12/1 - 7"
        sys.stdout = captured_output
        s.update(size=7, y=1)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)
        captured_output.seek(0)
        captured_output.truncate(0)
        expected_output = "[Square] (89) 12/1 - 7"
        sys.stdout = captured_output
        s.update(size=7, id=89, y=1)
        print(s, end="")
        sys.stdout = sys.__stdout__
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_to_dictinary(self):
        """Test the Method to dictionary"""
        s = Square(10, 2, 1)
        s_dict = s.to_dictionary()
        for key, value in s_dict.items():
            if key == "id":
                self.assertEqual(s.id, value)
            elif key == "size":
                self.assertEqual(s.size, value)
            elif key == "x":
                self.assertEqual(s.x, value)
            elif key == "y":
                self.assertEqual(s.y, value)
        self.assertEqual(len(set(s_dict.keys())), 4)
        self.assertTrue(isinstance(s_dict, dict))

        s = Square(5, 6, 7)
        s_dict = s.to_dictionary()
        for key, value in s_dict.items():
            if key == "id":
                self.assertEqual(s.id, value)
            elif key == "size":
                self.assertEqual(s.size, value)
            elif key == "x":
                self.assertEqual(s.x, value)
            elif key == "y":
                self.assertEqual(s.y, value)
        self.assertEqual(len(set(s_dict.keys())), 4)
        self.assertTrue(isinstance(s_dict, dict))

        s = Square(13, 5, 86, 12)
        s_dict = s.to_dictionary()
        for key, value in s_dict.items():
            if key == "id":
                self.assertEqual(s.id, value)
            elif key == "size":
                self.assertEqual(s.size, value)
            elif key == "x":
                self.assertEqual(s.x, value)
            elif key == "y":
                self.assertEqual(s.y, value)
        self.assertEqual(len(set(s_dict.keys())), 4)
        self.assertTrue(isinstance(s_dict, dict))


if __name__ == '__main__':
    unittest.main()
