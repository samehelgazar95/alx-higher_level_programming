#!/usr/bin/python3
""" 
Test Square Module 
"""
import unittest
import models.square
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
        pass
    
    def tearDown(self):
        pass
    
    def test_size(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
               
    def test_size_x(self):
        s = Square(1, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 1)
       
    def test_size_x_y(self):
        s = Square(1, 1, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 1)
                
    def test_string_size(self):
        with self.assertRaises(TypeError) as e:
            r = Square('1')
        msg = "width must be an integer"
        self.assertEqual(msg, str(e.exception))


    def test_string_x(self):
        with self.assertRaises(TypeError) as e:
            r = Square(1, '1')
        msg = "x must be an integer"
        self.assertTrue(msg in str(e.exception))

    def test_string_y(self):
        with self.assertRaises(TypeError) as e:
            r = Square(1, 1, '1')
        msg = "y must be an integer"
        self.assertTrue(msg in str(e.exception))

    def test_instance(self):
        r = Square(1, 2, 3, 4)
        self.assertEqual(str(r), "[Square] (4) 2/3 - 1")
        
    def test_negative_size(self):
        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_negative_x(self):
        with self.assertRaises(ValueError) as e:
            r = Square(1, -1)
        msg = "x must be >= 0"
        self.assertTrue(msg in str(e.exception))

    def test_negative_y(self):
        with self.assertRaises(ValueError) as e:
            r = Square(1, 1, -1)
        msg = "y must be >= 0"
        self.assertTrue(msg in str(e.exception))

    def test_negative_size(self):
        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(msg, str(e.exception))

    