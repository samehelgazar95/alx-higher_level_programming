#!/usr/bin/python3
""" 
Test Square Module 
I really don't whats's wrong here!!
But the checker refuse this file!!
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
    
    """ --------------- Task 10 --------------- """
    """ --------------- Initiate """
    def test_is_inheritance(self):
        self.assertTrue(issubclass(Square, Base))

    def test_is_inheritance(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_is_instance(self):
        s = Square(1, 1)
        self.assertTrue(isinstance(s, Base))

    def test_is_instance(self):
        s = Square(1, 1)
        self.assertTrue(isinstance(s, Rectangle))

    def test_doc_class(self):
        self.assertTrue(len(Square.__doc__) > 0)
        
    def test_doc_class(self):
        self.assertTrue(len(models.square.__doc__) > 0)
    

    def test_is_Square_class(self):
        s = Square(1, 1)
        self.assertTrue(str(s.__class__), "<class 'models.Square.Square'>")

    def test_init_zero_args(self):
        with self.assertRaises(Exception) as e:
            s = Square()
        msg = "Square.__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, 2, 3, 4, 5, 6)
        msg = "Square.__init__() takes from 2 to 5 positional arguments but 8 were given"
        self.assertTrue(str(e.exception) in msg)
        
    def test_initiate_Rectangle(self):
        s = Square(1, 1)
        self.assertEqual(s.id, 1)

    def test_two_initiate(self):
        s = Square(1, 1)
        ss = Square(1, 1)
        self.assertEqual(s.id + 1, ss.id)

    def test_three_initiate(self):
        s = Square(1, 1)
        ss = Square(1, 1, 1, 3)
        sss = Square(1, 1)
        self.assertEqual(s.id + 1, sss.id)
        
    """ --------------- area """
    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)
        
    def test_area(self):
        s = Square(2, 1, 1)
        self.assertEqual(s.area(), 4)

    """ --------------- display """
    def test_class_display(self):
        with self.assertRaises(TypeError) as e:
            Square().display()
        msg = "Square.__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(msg, str(e.exception))

    def test_display_1(self):
        from io import StringIO
        from contextlib import redirect_stdout

        s = Square(2)
        io = StringIO()
        msg = "##\n##\n"

        with redirect_stdout(io):
            s.display()
        self.assertEqual(msg, io.getvalue())

    def test_display_2(self):
        from io import StringIO
        from contextlib import redirect_stdout

        s = Square(2, 1, 1)
        io = StringIO()
        msg = "\n ##\n ##\n"

        with redirect_stdout(io):
            s.display()
        self.assertEqual(msg, io.getvalue())

    def test_display_3(self):
        from io import StringIO
        from contextlib import redirect_stdout
    
        s = Square(3, 2, 2)
        io = StringIO()
        msg = "\n\n  ###\n  ###\n  ###\n"
        
        with redirect_stdout(io):
            s.display()
        self.assertEqual(msg, io.getvalue())
        
    def test_display_4(self):
        from io import StringIO
        from contextlib import redirect_stdout
            
        s = Square(2, 0, 3)
        msg3 = "\n\n\n##\n##\n"
        io3 = StringIO()
        with redirect_stdout(io3):
            s.display()
        self.assertEqual(msg3, io3.getvalue())

    """ --------------- __str__ """
    def test_str_1(self):
        s = Square(2)
        msg = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(s), msg)
        
    def test_str_2(self):
        s = Square(4, 2, 3, 5)
        msg = "[Square] (5) 2/3 - 4"
        self.assertEqual(str(s), msg)
    
    def test_str_3(self):
        s = Square(2)
        s = Square(2)
        msg = "[Square] (2) 0/0 - 2"
        self.assertEqual(str(s), msg)
        
    """ --------------- Task 11 --------------- """
    """ ---------------  Getters & Setters """
    
    def invalid_values(self):
        invalids = (3.14, -3.14, float('inf'), float('-inf'), True,
                   False, "str", (1, 2), [1], {1, 2}, {1: 2}, None)
        return invalids

    def test_all_TypeErrors(self):
        s = Square(1, 1)
        items = ["size", "x", "y"]
        for item in items:
            if item == "size":
                msg = "width must be an integer"
            else:
                msg = "{} must be an integer".format(item)
            for invalid in self.invalid_values():
                with self.assertRaises(TypeError) as e:
                    setattr(s, item, invalid)
                self.assertEqual(msg, str(e.exception))

    def test_size_less_zero(self):
        with self.assertRaises(ValueError) as e:
            s = Square(-1)
        msg = "width must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_size_equals_zero(self):
        with self.assertRaises(ValueError) as e:
            s = Square(0)
        msg = "width must be > 0"
        self.assertTrue(msg in str(e.exception))

    def test_x_less_zero(self):
        with self.assertRaises(ValueError) as e:
            s = Square(1, -1)
        msg = "x must be >= 0"
        self.assertTrue(msg in str(e.exception))

    def test_y_less_zero(self):
        with self.assertRaises(ValueError) as e:
            s = Square(1, 1, -1)
        msg = "y must be >= 0"
        self.assertTrue(msg in str(e.exception))
    
    def test_size_setters(self):
        s = Square(1, 1)
        s.size = 10
        self.assertEqual(s.size, 10)
        
    def test_getters_x_y(self):
        s = Square(1, 5)
        self.assertEqual(5, s.x)
        self.assertEqual(0, s.y)

    def test_setters_x_y(self):
        s = Square(1, 10, 10)
        s.x = 20
        s.y = 30
        self.assertEqual(20, s.x)
        self.assertEqual(30, s.y)
        
    """ --------------- Task 12 --------------- """
    def test_class_str(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        msg = "Rectangle.__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(e.exception))

    def test_str1(self):            
        r1 = Rectangle(4, 6, 2, 1, 12)
        s1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), s1)

    def test_str2(self):            
        r2 = Rectangle(5, 5, 1)
        s2 = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r2), s2)

    def test_str3(self):            
        r3 = Rectangle(1, 1)
        s3 = "[Rectangle] (1) 0/0 - 1/1"
        self.assertEqual(str(r3), s3)
  
    def test_main_cases(self):
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
  
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
  
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")
        
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/4 - 2")
        
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")
        
    """ --------------- Task 9 --------------- """
    def test_class_udpate(self):
        with self.assertRaises(TypeError) as e:
            Square.update()
        msg = "Square.update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_update_args_1(self):
        s = Square(1)
        dic = s.__dict__.copy()

        s.update(2)
        dic["id"] = 2
        self.assertEqual(s.__dict__, dic)

    def test_update_args_2(self):
        s = Square(1)
        dic = s.__dict__.copy()

        s.update(3, 5, 3, 3)
        dic["id"] = 3
        dic["_Rectangle__width"] = 5
        dic["_Rectangle__height"] = 5
        dic["_Rectangle__x"] = 3    
        dic["_Rectangle__y"] = 3
        self.assertEqual(s.__dict__, dic)

    def test_update_kwargs(self):
        s = Square(1, 1)
        dic = s.__dict__.copy()

        s.update(y=1, size=3, x=1, id=13)
        dic["_Rectangle__y"] = 1
        dic["_Rectangle__width"] = 3
        dic["_Rectangle__height"] = 3
        dic["_Rectangle__x"] = 1
        dic["id"] = 13
        self.assertEqual(s.__dict__, dic)

    def test_update_arg_kwargs(self):
        s = Square(1)
        dic = s.__dict__.copy()

        s.update(4, 4, id=5, size=3)
        dic["id"] = 4
        dic["_Rectangle__width"] = 4
        dic["_Rectangle__height"] = 4
        self.assertEqual(s.__dict__, dic)

    def test_update_to_negative_x(self):
        s = Square(13, 2)
        with self.assertRaises(ValueError) as e:
            s.update(1, 1, -1)
            
        msg = "x must be >= 0"
        self.assertEqual(msg, str(e.exception))
        
    def test_update_to_negative_y(self):
        s = Square(13, 2)
        with self.assertRaises(ValueError) as e:
            s.update(1, 1, 1, -1)
            
        msg = "y must be >= 0"
        self.assertEqual(msg, str(e.exception))
        
    def test_update_to_negative_size(self):
        s = Square(13, 2)
        with self.assertRaises(ValueError) as e:
            s.update(1, -1)
            
        msg = "width must be > 0"
        self.assertEqual(msg, str(e.exception))


    """ --------------- Task 14 --------------- """
    def test_class_to_dic(self):
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
            
        msg = "Square.to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(e.exception))
    
    def test_to_dict(self):
        r = Square(10, 2, 1)
        dic = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertTrue(r.to_dictionary(), dic)

    def test_coping_dict_to_another_obj(self):
        r = Square(10, 2, 1)
        rr = Square(1, 1, 1, 1)
        dic = r.to_dictionary()
        rr.update(**dic)
        self.assertFalse(r == rr)    
        
    def test_coping_dict_to_another_obj_compare_them(self):
        r = Square(10, 2, 1)
        rr = Square(1, 1, 1, 1)
        dic = r.to_dictionary()
        rr.update(**dic)
        self.assertTrue(r.to_dictionary() == rr.to_dictionary())  

    def test_coping_dict_to_another_obj_update_then_compare_them(self):
        r = Square(10, 2, 1)
        rr = Square(1, 1)
        dic = r.to_dictionary()
        rr.update(**dic)
        r.update(2, 2, 2, 2)
        self.assertFalse(r.to_dictionary() == rr.to_dictionary())
