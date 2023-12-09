#!/usr/bin/python3
"""
Testing module for the calsses  Rectangles
In this module we will test all the available Functionalities
and Comme up with adequate testes
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleValidValues(unittest.TestCase):
    """
    TestRectanleIdValidValues is a class that test
    id valid values and make sure that we get
    good information out of it
    """

    def setUp(self):
        """Set up the start of objects"""
        Rectangle.set_nb_objects()

    def test_id_two_classes(self):
        """
        test the value of one class id
        """

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id_three_classes(self):
        """
        test the output of three classes
        """

        r1 = Rectangle(4, 15)
        r2 = Rectangle(12, 65)
        r3 = Rectangle(12, 87)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r1.id, r3.id - 2)

    def test_id_provided(self):
        """
        test with provided id in
        the object creation
        """

        r1 = Rectangle(12, 54, 12, 54, 12)
        r2 = Rectangle(8, 78, 12, 54, -12)
        r3 = Rectangle(9, 45, 15, 23, -15)
        r4 = Rectangle(5, 12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, -12)
        self.assertEqual(r3.id, -15)
        self.assertEqual(r4.id, 1)

    def test_height_width_valid_values_types(self):
        """
        test with valid height and width
        valid values
        """

        r1 = Rectangle(12, 54)
        r2 = Rectangle(54, 1222222)
        r3 = Rectangle(1, 1)
        self.assertEqual(r1.height, 54)
        self.assertEqual(r2.height, 1222222)
        self.assertEqual(r3.height, 1)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r2.width, 54)
        self.assertEqual(r3.width, 1)

    def test_height_width_invalid_values_types(self):
        """
        test with valid height and width
        valid values
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("0", 54)

        with self.assertRaises(TypeError):
            r1 = Rectangle([1, 2, 3], 1222222)

        with self.assertRaises(TypeError):
            r1 = Rectangle({"age": 23}, 54)

        with self.assertRaises(TypeError):
            r1 = Rectangle(23.25, 54)

        with self.assertRaises(TypeError):
            r1 = Rectangle((1, 2, 3), 54)

        with self.assertRaises(TypeError):
            r1 = Rectangle(54, "54")

        with self.assertRaises(TypeError):
            r1 = Rectangle(25, [1, 2, 3])

        with self.assertRaises(TypeError):
            r1 = Rectangle(23, {"age": 23})

        with self.assertRaises(TypeError):
            r1 = Rectangle(23, 54.5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(25, (1, 2, 3))

        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 23)

        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 0)

        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 23)

        with self.assertRaises(ValueError):
            r1 = Rectangle(23, -10)

    def test_x_y_valid_values_types(self):
        """
        test with valid height and width
        valid values
        """

        r1 = Rectangle(12, 54, 1, 2)
        r2 = Rectangle(54, 1222222, 0, 2)
        r3 = Rectangle(1, 1, 100, 0)
        r4 = Rectangle(1, 1, 0, 0)

    def test_x_y_invalid_values_types(self):
        """
        test with valid height and width
        valid values
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 54, "0", 23)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, [1, 2, 3], 1222222)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, {"age": 23}, 54)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 23.25, 54)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, (1, 2, 3), 54)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 54, "54")

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 25, [1, 2, 3])

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 23, {"age": 23})

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 23, 54.5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 25, (1, 2, 3))

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -10, 23)

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 23, -10)

    def test_area(self):
        """Test the area values"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)


if __name__ == '__main__':
    unittest.main()
