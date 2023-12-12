#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from io import StringIO
from random import randrange
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
import models.rectangle


class TestRectangle(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass
    
    def test_is_instance(self):
        """ test is instance """
        r = Rectangle(1, 1)
        self.assertTrue(isinstance(r, Base))

    def test_doc_class(self):
        """ test doc class """
        self.assertTrue(len(models.rectangle.__doc__) > 0)

    def test_init_one_arg(self):
        """ test init one arg """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        msg = "Rectangle.__init__() missing 1 required positional argument: 'height'"

    def test_is_Rectangle_class(self):
        """ test is Rectangle class """
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_is_inheritance(self):
        """ test is inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_width_heigth_getters(self):
        """ test width heigth getters """
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

    def test_getters_x_y(self):
        """ test getters x y """
        r = Rectangle(1, 1, 15, 20)
        self.assertEqual(15, r.x)
        self.assertEqual(20, r.y)

    def test_initiate_Rectangle(self):
        """ test initiate Rectangle """
        r = Rectangle(1, 1, 2)
        self.assertEqual(r.id, 1)

    def test_three_initiate(self):
        """ test three initiate """
        r = Rectangle(1, 1)
        rr = Rectangle(1, 1, 1, 2, 5)
        rrr = Rectangle(1, 1)
        self.assertEqual(r.id + 1, rrr.id)

    def test_two_initiate(self):
        """ test two initiate """
        r = Rectangle(1, 1)
        rr = Rectangle(1, 1)
        self.assertEqual(r.id + 1, rr.id)

    def invalid_values(self):
        """ invalid values """
        invalids = (3.14, -3.14, float('inf'), float('-inf'), True,
                   False, "str", (1, 2), [1], {1, 2}, {1: 2}, None)
        return invalids

    def test_all_TypeErrors(self):
        """ test all TypeErrors """
        r = Rectangle(1, 1)
        items = ["width", "height", "x", "y"]
        for item in items:
            msg = "{} must be an integer".format(item)
            for invalid in self.invalid_values():
                with self.assertRaises(TypeError) as e:
                    setattr(r, item, invalid)
                self.assertEqual(msg, str(e.exception))

    def test_width_less_zero(self):
        """ test width less zero """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 1)
        msg = "width must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_height_less_zero(self):
        """ test height less zero """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -1)
        msg = "height must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_width_equals_zero(self):
        """ test width equals zero """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 1)
        msg = "width must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_height_equals_zero(self):
        """ test height equals zero"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_x_less_zero(self):
        """ test x less zero """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 1, -1, 1)
        msg = "x must be >= 0"
        self.assertTrue(msg in str(e.exception))

    def test_y_less_zero(self):
        """ test y less zero """
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 1, 1, -1)
        msg = "y must be >= 0"
        self.assertTrue(msg in str(e.exception))


    def test_string_width(self):
        """ test string width """
        with self.assertRaises(TypeError) as e:
            r = Rectangle('1', 1)
        msg = "width must be an integer"
        self.assertTrue(msg in str(e.exception))

    def test_string_height(self):
        """ test string height """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, '1')
        msg = "height must be an integer"
        self.assertTrue(msg in str(e.exception))

    def test_string_x(self):
        """ test string x """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, '1')
        msg = "x must be an integer"
        self.assertTrue(msg in str(e.exception))

    def test_string_y(self):
        """ test string y """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, '1')
        msg = "y must be an integer"
        self.assertTrue(msg in str(e.exception))



if __name__ == "__main__":
    unittest.main()
