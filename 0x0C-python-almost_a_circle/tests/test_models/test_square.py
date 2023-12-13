#!/usr/bin/python3
""" 
Test Square Module 
"""
import unittest
import os
import json
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
            s = Square('1')
        msg = "width must be an integer"
        self.assertEqual(msg, str(e.exception))


    def test_string_x(self):
        with self.assertRaises(TypeError) as e:
            s = Square(1, '1')
        msg = "x must be an integer"
        self.assertTrue(msg in str(e.exception))

    def test_string_y(self):
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, '1')
        msg = "y must be an integer"
        self.assertTrue(msg in str(e.exception))

    def test_instance(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")
        
    def test_negative_size(self):
        with self.assertRaises(ValueError) as e:
            s = Square(-1)
        msg = "width must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_negative_x(self):
        with self.assertRaises(ValueError) as e:
            s = Square(1, -1)
        msg = "x must be >= 0"
        self.assertTrue(msg in str(e.exception))

    def test_negative_y(self):
        with self.assertRaises(ValueError) as e:
            s = Square(1, 1, -1)
        msg = "y must be >= 0"
        self.assertTrue(msg in str(e.exception))

    def test_negative_size(self):
        with self.assertRaises(ValueError) as e:
            s = Square(0)
        msg = "width must be > 0"
        self.assertEqual(msg, str(e.exception))

    def test_update_args_1(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()

        s.update(2)
        dic["id"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_args_2(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()

        s.update(2, 2)
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_args_3(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()

        s.update(2, 2, 2)
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_args_4(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()

        s.update(2, 2, 2, 2)
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        dic["_Rectangle__y"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_kwargs_1(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()

        s.update(**{'id': 2})
        dic["id"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_kwargs_2(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()

        s.update(**{'id': 2, 'size': 2})
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_kwargs_3(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()

        s.update(**{'id': 2, 'size': 2, 'x': 2})
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_kwargs_4(self):
        """ test update args 1 """
        s = Square(5, 5, 5, 5)
        dic = s.__dict__.copy()
     
        s.update(**{'id': 2, 'size': 2, 'x': 2, 'y': 2})
        dic["id"] = 2
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 2
        dic["_Rectangle__x"] = 2
        dic["_Rectangle__y"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_create1(self):
        s = Square.create(**{'id':2})
        s_str = "[Square] (2) 0/0 - 1"
        self.assertEqual(str(s), s_str)
  
    def test_create2(self):
        s = Square.create(**{'id':2, 'size':2})
        s_str = "[Square] (2) 0/0 - 2"
        self.assertEqual(str(s), s_str)
        
    def test_create3(self):
        s = Square.create(**{'id':2, 'size':2, 'x':2})
        s_str = "[Square] (2) 2/0 - 2"
        self.assertEqual(str(s), s_str)
  
    def test_create4(self):
        s = Square.create(**{'id':2, 'size':2, 'x':2, 'y':2})
        s_str = "[Square] (2) 2/2 - 2"
        self.assertEqual(str(s), s_str)

    def test_save_to_file1(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", 'r') as f:
            file_content = f.read()
            os.remove("Square.json")
            expected_content = [{"size":1, 'x':0, 'y':0, 'id':1}]
            self.assertEqual(file_content, json.dumps(expected_content))        
    
    def test_save_to_file2(self):
        Rectangle.save_to_file(None)
        with open("Square.json", 'r') as f:
            file_content = f.read()
            os.remove("Square.json")
            expected_content = []
            self.assertEqual(file_content, json.dumps(expected_content))        
    
    def test_save_to_file3(self):
        Square.save_to_file([])
        with open("Square.json", 'r') as f:
            file_content = f.read()
            os.remove("Square.json")
            expected_content = []
            self.assertEqual(file_content, json.dumps(expected_content))        
    
if __name__ == "__main__":
    unittest.main()