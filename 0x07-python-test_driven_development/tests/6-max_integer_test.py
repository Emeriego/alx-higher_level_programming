#!/usr/bin/python3
"""Unittest for module: max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCases for the max_integer function."""

    def test_withempty(self):
        """Run with an empty list: should return None"""
        list_data = []
        outcom = max_integer(list_data)
        self.assertEqual(outcom, None)

    def test_withneg(self):
        """Test with a list of negative values: should return the max"""
        list_data = [-5, -10, -1]
        outcom = max_integer(list_data)
        self.assertEqual(outcom, -1)

    def test_withvalid(self):
        """Run module with valid list of ints: returns max int"""
        list_data = [1, 5, 8, 4, 5]
        outcom = max_integer(list_data)
        self.assertEqual(outcom, 8)

    def test_withnotlist(self):
        """Run with not a list: Raises a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_withsingle(self):
        """Test with a single value int: Returns the value of this int"""
        list_data = [8]
        outcom = max_integer(list_data)
        self.assertEqual(outcom, 8)

    def test_withinvalid(self):
        """Run module with invalid list of items:
        raises a TypeError exception"""
        list_data = [9, "t", "k"]
        self.assertRaises(TypeError, max_integer, list_data)

    def test_withfloat(self):
        """Run with mixed, ints and floats: success return"""
        list_data = [3.1, 5, 2]
        outcom = max_integer(list_data)
        self.assertEqual(outcom, 5)

    def test_withfloat(self):
        """Test with a list of mixed ints and floats: should return the max"""
        list_data = [3.1, 7.9, 2]
        outcom = max_integer(list_data)
        self.assertEqual(outcom, 7.9)

    def test_withmults(self):
        """Test with a list of identical values: Returns the value"""
        list_data = [2, 2, 2, 2, 2, 2, 2, 2]
        outcom = max_integer(list_data)
        self.assertEqual(outcom, 2)

    def test_withstrings(self):
        """Test with strings: Returns the first string"""
        list_data = ["hello", "Alx"]
        outcom = max_integer(list_data)
        self.assertEqual(outcom, "hello")

    def test_withnone(self):
        """Test with None: Raises a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
