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


if __name__ == '__main__':
    unittest.main()
