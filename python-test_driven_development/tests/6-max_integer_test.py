#!/usr/bin/python3
"""Tests"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_one_max(self):
        test_list = [12]
        self.assertEqual(max_integer(test_list), 12)

    def test_max_end(self):
        test_list = [0, 1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_first(self):
        test_list = [4, 3, 2, 1, 0]
        self.assertEqual(max_integer(test_list), 4)

    def test_max_middle(self):
        test_list = [134, 212, 444, 321, 111]
        self.assertEqual(max_integer(test_list), 444)

    def test_max_one_negative(self):
        test_list = [1, 5, -3, 4, 99]
        self.assertEqual(max_integer(test_list), 99)

    def test_max_all_negative(self):
        test_list = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(test_list), -1)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)
