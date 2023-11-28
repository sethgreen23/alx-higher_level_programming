#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class to test the 6-max_integer module
    """

    def test_length_0(self):
        """Empty list"""

        self.assertEqual(max_integer([]), None)


    def test_on_number(self):
        """on number in the list"""

        self.assertEqual(max_integer([1]), 1)


    def test_all_positive_numbers(self):
        """All elements are positive numbers"""

        self.assertEqual(max_integer([1, 2, 300, 3]), 300)


    def test_max_beggining(self):
        """Max value at the beggining"""

        self.assertEqual(max_integer([300, 1, 3, 5, 6]), 300)


    def test_max_end(self):
        """Max value at the end"""

        self.assertEqual(max_integer([1, 2, 3, 4, 300]), 300)


    def test_all_negative(self):
        """All values are negative"""

        self.assertEqual(max_integer([-1, -232, -50, -10, -150]), -1)


    def test_one_negative(self):
        """Just one value is negative"""

        self.assertEqual(max_integer([-1, 201, 34, 50]), 201)


    def test_one_positive(self):
        """Just one element is positive"""

        self.assertEqual(max_integer([300, -10, -300, -25]), 300)

    def test_none(self):
        """Argument list is none"""

        with self.assertRaises(TypeError):
            max_integer(None)


    def test_non_integer_value_inside(self):
        """On element in the list is non integer"""

        with self.assertRaises(TypeError):
            max_integer([1, 2, "non-int", 3])


if __name__ == "__main__":
    unittest.main()
