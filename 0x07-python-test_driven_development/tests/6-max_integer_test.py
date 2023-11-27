#!/usr/bin/python3
"""UnitTest for max_integer([])"""
import unittest
max_integer = __import__('..6-max_integer.py').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_EmptyList(self):
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
