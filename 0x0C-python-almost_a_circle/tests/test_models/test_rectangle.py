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
    
    def test_is_Rectangle_class(self):
        """ test is Rectangle class """
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_is_inheritance(self):
        """ test is inheritance """
        self.assertTrue(issubclass(Rectangle, Base))


if __name__ == "__main__":
    unittest.main()
