#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered_array = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_array), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered_array = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered_array), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        highest_num = [4, 3, 2, 1]
        self.assertEqual(max_integer(highest_num), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one = [7]
        self.assertEqual(max_integer(one), 7)

    def test_floats(self):
        """Test a list of floats."""
        float_num = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(float_num), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        diff_num = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(diff_num), 15.5)

    def test_string(self):
        """Test a string."""
        name = "Brennan"
        self.assertEqual(max_integer(name), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        sentences = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(sentences), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

