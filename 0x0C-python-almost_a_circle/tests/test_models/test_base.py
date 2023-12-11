#!/usr/bin/python3
"""UnitTest for Base Class Module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """UnitTest for Base Class Class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_doc_class(self):
        """ Task 1 """
        self.assertTrue(len(Base.__doc__) > 0)
    
    def test_is__Base_class(self):
        b = Base()
        self.assertTrue(str(b.__class__), "<class 'models.base.Base'>")

    def test_class_has_id(self):
        b = Base()
        self.assertTrue(hasattr(b, "id"))

    def test_class_has_id(self):
        b = Base()
        self.assertTrue(hasattr(b, "_Base__nb_objects"))

    def test_no_id(self):
        b = Base()
        self.assertEqual(getattr(b, "_Base__nb_objects"), b.id)

    def test_zero_id(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_two_empty_instances(self):
        b = Base()
        bb = Base()
        self.assertEqual(b.id + 1, bb.id)

    def test_two_instances(self):
        b = Base(5)
        b = Base()
        self.assertEqual(b.id, 1)

    def test_positive_id(self):
        b = Base(13)
        self.assertEqual(b.id, 13)

    def test_negative_id(self):        
        b = Base(-5)
        self.assertEqual(b.id, -5)
    
    def test_none_id(self):
        b = Base(None)
        self.assertEqual(b.id, 1) 