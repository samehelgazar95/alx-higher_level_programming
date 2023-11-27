#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_first_test(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_second_test(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_second_test(self):
        self.assertEqual(max_integer([1, 3, -4, -2]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_list(self):
        self.assertEqual(max_integer(), None)

    def test_duplicates(self):
        self.assertEqual(max_integer([9, 9, 9, 9, 9, 9, 9, 9, 9]), 9)

    def test_nan(self):
        self.assertEqual(max_integer([1, 2, 3, 4, float('nan')]), 4)

    def test_positive_infinity(self):
        self.assertEqual(max_integer([1, 2, 3, 4, float('inf')]), float('inf'))

    def test_negative_infinity(self):
        self.assertEqual(max_integer([1, 2, 3, 4, float('-inf')]), 4)

    def test_str(self):
        try:
            max_integer([1, 2, 3, '4'])
        except TypeError as e:
            err_msg = "'>' not supported between instances of 'str' and 'int'"
            self.assertIn(err_msg, str(e))

    def test_2d_list(self):
        try:
            max_integer([1, [2], 3, [4]])
        except TypeError as e:
            err_msg = "'>' not supported between instances of 'list' and 'int'"
            self.assertIn(err_msg, str(e))

    def test_dict(self):
        with self.assertRaises(TypeError):
            max_integer([1, 3, {'a': 2}])

    def test_int(self):
        try:
            max_integer(10)
        except TypeError as e:
            err_msg = "object of type 'int' has no len()"
            self.assertIn(err_msg, str(e))

    def test_float(self):
        with self.assertRaises(TypeError):
            max_integer(3.14)


if __name__ == '__main__':
    unittest.main()
