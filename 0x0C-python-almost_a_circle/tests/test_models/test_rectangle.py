#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from io import StringIO
from contextlib import redirect_stdout
import os
import json
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

    def test_instance(self):
        """ test instance """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")
        
    def test_area_1(self):
        """ test area 1 """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        
    def test_area_2(self):
        """ test area 2 """
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display_1(self):
        """ test display 1 """
        r1 = Rectangle(1, 1)
        io1 = StringIO()
        msg1 = "#\n"
        with redirect_stdout(io1):
            r1.display()
        self.assertEqual(msg1, io1.getvalue())

    def test_display_no_y(self):
        """ test display no y """
        r2 = Rectangle(3, 2, 1)
        msg2 = " ###\n ###\n"
        io2 = StringIO()
        with redirect_stdout(io2):
            r2.display()
        self.assertEqual(msg2, io2.getvalue())

    def test_update_args_1(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(2)
        dic["id"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_2(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(2, 2)
        dic["_Rectangle__width"] = 2
        dic["id"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_3(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(2, 2, 2)
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["id"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_4(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(2, 2, 2, 2)
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_4(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(2, 2, 2, 2, 2)
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        dic["_Rectangle__y"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_1(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(**{'id': 2})
        dic["id"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_2(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(**{'id': 2, 'width': 2})
        dic["_Rectangle__width"] = 2
        dic["id"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_3(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(**{'id': 2, 'width': 2, 'height': 2})
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["id"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_4(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(**{'id': 2, 'width': 2, 'height': 2, 'x': 2})
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_4(self):
        """ test update args 1 """
        r = Rectangle(5, 5, 5, 5, 5)
        dic = r.__dict__.copy()

        r.update(**{'id': 2, 'width': 2, 'height': 2, 'x': 2, 'y': 2})
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        dic["_Rectangle__y"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_create1(self):
        r = Rectangle.create(**{'id':2})
        r_str = "[Rectangle] (2) 0/0 - 1/1"
        self.assertEqual(str(r), r_str)
  
    def test_create2(self):
        r = Rectangle.create(**{'id':2, 'width':2})
        r_str = "[Rectangle] (2) 0/0 - 2/1"
        self.assertEqual(str(r), r_str)
        
    def test_create3(self):
        r = Rectangle.create(**{'id':2, 'width':2, 'height':2})
        r_str = "[Rectangle] (2) 0/0 - 2/2"
        self.assertEqual(str(r), r_str)
  
    def test_create4(self):
        r = Rectangle.create(**{'id':2, 'width':2, 'height':2, 'x':1})
        r_str = "[Rectangle] (2) 1/0 - 2/2"
        self.assertEqual(str(r), r_str)
  
    def test_create5(self):
        r = Rectangle.create(**{'id':2, 'width':2, 'height':2, 'x':1, 'y':1})
        r_str = "[Rectangle] (2) 1/1 - 2/2"
        self.assertEqual(str(r), r_str)
    
    def test_save_to_file1(self): 
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", 'r') as f:
            file_content = f.read()
            os.remove("Rectangle.json")
            expected_content = [{'x':0, 'y':0, 'id':1, 'width': 1, 'height':2}]
            self.assertEqual(file_content, json.dumps(expected_content))        
    
    def test_save_to_file2(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            file_content = f.read()
            os.remove("Rectangle.json")
            expected_content = []
            self.assertEqual(file_content, json.dumps(expected_content))        
    
    def test_save_to_file3(self):
        Rectangle.save_to_file([])
        file_name = "{}.json".format(Rectangle.__name__)
        with open(file_name, 'r') as f:
            file_content = f.read()
            os.remove(file_name)
            expected_content = []
            self.assertEqual(file_content, json.dumps(expected_content))        
    
    
if __name__ == "__main__":
    unittest.main()
