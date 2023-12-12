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


    """ --------------- Task 4 --------------- """
    def test_area_1(self):
        """ test area 1 """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        
    def test_area_2(self):
        """ test area 2 """
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)
        

    """ --------------- Task 5 - 7 --------------- """
    def test_class_display(self):
        """ test class display """
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        msg = "Rectangle.display() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(e.exception))

    def test_display_1(self):
        """ test display 1 """
        r1 = Rectangle(1, 1)
        io1 = StringIO()
        msg1 = "#\n"
        with redirect_stdout(io1):
            r1.display()
        self.assertEqual(msg1, io1.getvalue())

    def test_display_2(self):
        """ test display 2 """
        r2 = Rectangle(2, 2)
        io2 = StringIO()
        msg2 = "##\n##\n"
        with redirect_stdout(io2):
            r2.display()
        self.assertEqual(msg2, io2.getvalue())

    def test_display_3(self):
        """ test display 3 """
        r3 = Rectangle(4, 6)
        io3 = StringIO()
        msg3 = "####\n####\n####\n####\n####\n####\n"
        with redirect_stdout(io3):
            r3.display()
        self.assertEqual(msg3, io3.getvalue())

    def test_display_xy1(self):
        """ test display xy1 """
        r1 = Rectangle(2, 3, 2, 2)
        msg1 = "\n\n  ##\n  ##\n  ##\n"
        io1 = StringIO()
        with redirect_stdout(io1):
            r1.display()
        self.assertEqual(msg1, io1.getvalue())

    def test_display_xy2(self):
        """ test display xy2 """
        r2 = Rectangle(3, 2, 1, 0)
        msg2 = " ###\n ###\n"
        io2 = StringIO()
        with redirect_stdout(io2):
            r2.display()
        self.assertEqual(msg2, io2.getvalue())

    def test_display_xy3(self):
        """ test display xy3 """            
        r3 = Rectangle(2, 2, 0, 3)
        msg3 = "\n\n\n##\n##\n"
        io3 = StringIO()
        with redirect_stdout(io3):
            r3.display()
        self.assertEqual(msg3, io3.getvalue())


    """ --------------- Task 6 str --------------- """
    def test_class_str(self):
        """ test class str """
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        msg = "Rectangle.__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(e.exception))

    def test_str1(self):
        """ test str1 """            
        r1 = Rectangle(4, 6, 2, 1, 12)
        s1 = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), s1)

    def test_str2(self):
        """ test str2 """            
        r2 = Rectangle(5, 5, 1)
        s2 = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r2), s2)

    def test_str3(self):
        """ test str3 """            
        r3 = Rectangle(1, 1)
        s3 = "[Rectangle] (1) 0/0 - 1/1"
        self.assertEqual(str(r3), s3)

    """ --------------- Task 9 --------------- """
    def test_class_udpate(self):
        """ test class udpate """
        with self.assertRaises(TypeError) as e:
            Rectangle.update()
        msg = "Rectangle.update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_update_args_1(self):
        """ test update args 1 """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(2, 2, 3)
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__height"] = 3
        dic["id"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_args_2(self):
        """ test update args 2 """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(3, 3, 3, 3, 3)
        dic["_Rectangle__width"] = 3
        dic["_Rectangle__height"] = 3
        dic["_Rectangle__x"] = 3    
        dic["_Rectangle__y"] = 3
        dic["id"] = 3
        self.assertEqual(r.__dict__, dic)

    def test_update_arg_3(self):
        """ test update arg 3 """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(5, 4, 4, 4, 4)
        dic["_Rectangle__width"] = 4
        dic["_Rectangle__height"] = 4
        dic["_Rectangle__x"] = 4
        dic["_Rectangle__y"] = 4
        dic["id"] = 5
        self.assertEqual(r.__dict__, dic)

    def test_upadte_args_kwargs(self):
        """ test upadte args kwargs """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(4, 4, 4, 4, 4, width=5, height=5)
        dic["_Rectangle__width"] = 4
        dic["_Rectangle__height"] = 4
        dic["_Rectangle__x"] = 4
        dic["_Rectangle__y"] = 4
        dic["id"] = 4
        self.assertEqual(r.__dict__, dic)

    def test_update_kwargs_1(self):
        """ test update kwargs 1 """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(width=2)
        dic["_Rectangle__width"] = 2
        self.assertEqual(r.__dict__, dic)

    def test_update_kwargs_2(self):
        """ test update kwargs 2 """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(id=5)
        dic["id"] = 5
        self.assertEqual(r.__dict__, dic)

    def test_update_kwargs_3(self):
        """ test update kwargs 3 """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(height=5)
        dic["_Rectangle__height"] = 5
        self.assertEqual(r.__dict__, dic)

    def test_update_kwargs_4(self):
        """ test update kwargs 4 """
        r = Rectangle(1, 1)
        dic = r.__dict__.copy()

        r.update(y=1, width=2, x=3, id=89)
        dic["_Rectangle__y"] = 1
        dic["_Rectangle__width"] = 2
        dic["_Rectangle__x"] = 3
        dic["id"] = 89
        self.assertEqual(r.__dict__, dic)

    def test_update_to_negative_x(self):
        """ test update to negative x """
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError) as e:
            r.update(2, 1, 2, -1)
            
        msg = "x must be >= 0"
        self.assertEqual(msg, str(e.exception))

    def test_update_to_negative_y(self):
        """ test update to negative y """
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError) as e:
            r.update(1, 2, 2, 2, -1)
            
        msg = "y must be >= 0"
        self.assertEqual(msg, str(e.exception))

    def test_update_to_negative_width(self):
        """ test update to negative width """
        r = Rectangle(1, 1)
        with self.assertRaises(ValueError) as e:
            r.update(1, -2, 2)

        msg = "width must be > 0"
        self.assertEqual(msg, str(e.exception))

    """ --------------- Task 13 --------------- """
    def test_class_to_dic(self):
        """ test class to dic """
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
            
        msg = "Rectangle.to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(msg, str(e.exception))
        
    def test_to_dict(self):
        """ test to dict """
        r = Rectangle(10, 2, 1, 9)
        dic = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), dic)
        
    def test_coping_dict_to_another_obj(self):
        """ test coping dict to another obj """
        r = Rectangle(10, 2, 1, 9)
        rr = Rectangle(1, 1, 1, 1)
        dic = r.to_dictionary()
        rr.update(**dic)
        self.assertFalse(r == rr)    
        
    def test_coping_dict_to_another_obj_compare_them(self):
        """ test coping dict to another obj compare them """
        r = Rectangle(10, 2, 1, 9)
        rr = Rectangle(1, 1, 1, 1)
        dic = r.to_dictionary()
        rr.update(**dic)
        self.assertTrue(r.to_dictionary() == rr.to_dictionary())  
    
    def test_coping_dict_to_another_obj_update_then_compare_them(self):
        """ test coping dict to another obj update then compare them """
        r = Rectangle(10, 2, 1, 9)
        rr = Rectangle(1, 1)
        dic = r.to_dictionary()
        rr.update(**dic)
        r.update(2, 2, 2, 2)
        self.assertFalse(r.to_dictionary() == rr.to_dictionary())




if __name__ == "__main__":
    unittest.main()
