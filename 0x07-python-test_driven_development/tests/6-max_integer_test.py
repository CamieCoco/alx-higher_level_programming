#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function from 6-max_integer module
    """
    def test_zero_list_length(self):
        """
        tests for empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_nice_int_list(self):
        """
        tests with a list of ints
        """
        biggest = max_integer([12, 60, 36])
        self.assertEqual(biggest, 60)
        with self.assertRaises(TypeError):
            max_integer(2, 5)

    def test_one_string(self):
        """
        passing a string to the function
        """
        highest_ascii = max_integer("asdf")
        self.assertEqual(highest_ascii, "s")

    def test_strings_list(self):
        """
        passing a list of strings
        """
        firstletter = max_integer(["egg", "oeuf", "fromage"])
        self.assertEqual(firstletter, "oeuf")

    def test_infinities(self):
        """
        comparing infinity and negative infinity
        """
        pos_infin = float("inf")
        neg_infin = float("-inf")
        big_infinity = max_integer([pos_infin, neg_infin])
        self.assertEqual(big_infinity, pos_infin)

    def test_neg_infinity_to_zero(self):
        """
        comparing negative infinity to 0
        """
        neg_infin = float("-inf")
        zero = max_integer([0, neg_infin])
        self.assertEqual(zero, 0)

    def test_end_max(self):
        """
        max at end
        """
        pos_infin = float("inf")
        self.assertEqual(max_integer([5, 4, pos_infin]), pos_infin)

    def test_mid_max(self):
        """
        max in the middle
        """
        pos_infin = float("inf")
        self.assertEqual(max_integer([-2, pos_infin, 9]), pos_infin)

    def test_neg_nums(self):
        """
        list of only negative numbers
        """
        neg_infin = float("-inf")
        self.assertEqual(max_integer([-12, -5, neg_infin, -200, -1]), -1)

    def test_one_element(self):
        """
        list of only one number
        """
        self.assertEqual(max_integer([3.14]), 3.14)

if __name__ == '__main__':
    unittest.main()
