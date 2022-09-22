#!/usr/bin/env python3

# Copyright (c) 2022 Edmundo Carmona Antoranz
# Released under the terms of GPLv3

import unittest

from pywerhose import Generator

class BasicTest(unittest.TestCase):

    def test_basic(self):
        generator = Generator()
        self.assertEqual((2, 2, 4), generator.next())
        self.assertEqual((2, 3, 8), generator.next())
        self.assertEqual((3, 2, 9), generator.next())
        self.assertEqual((2, 4, 16), generator.next())
        self.assertEqual((5, 2, 25), generator.next())
        self.assertEqual((3, 3, 27), generator.next())

    def test_with_min_base(self):
        generator = Generator(min_base = 4)
        self.assertEqual((4, 2, 16), generator.next())
        self.assertEqual((5, 2, 25), generator.next())
        self.assertEqual((6, 2, 36), generator.next())
        self.assertEqual((7, 2, 49), generator.next())
        self.assertEqual((4, 3, 64), generator.next())
        self.assertEqual((9, 2, 81), generator.next())
        self.assertEqual((10, 2, 100), generator.next())
        self.assertEqual((11, 2, 121), generator.next())
        self.assertEqual((5, 3, 125), generator.next())
    
    def test_with_min_power(self):
        generator = Generator(min_power = 3)
        self.assertEqual((2, 3, 8), generator.next())
        self.assertEqual((2, 4, 16), generator.next())
        self.assertEqual((3, 3, 27), generator.next())
        self.assertEqual((2, 5, 32), generator.next())
        self.assertEqual((2, 6, 64), generator.next())
        self.assertEqual((3, 4, 81), generator.next())
        self.assertEqual((5, 3, 125), generator.next())
        self.assertEqual((2, 7, 128), generator.next())

    def test_with_step(self):
        generator = Generator(step = 3)
        self.assertEqual((2, 2, 4), generator.next())
        self.assertEqual((2, 3, 8), generator.next())
        self.assertEqual((2, 4, 16), generator.next())
        self.assertEqual((5, 2, 25), generator.next())
        self.assertEqual((2, 5, 32), generator.next())
        self.assertEqual((2, 6, 64), generator.next())
        self.assertEqual((11, 2, 121), generator.next())
        self.assertEqual((5, 3, 125), generator.next())
        self.assertEqual((2, 7, 128), generator.next())

    def test_start_from_a_power(self):
        generator = Generator(start_from = 1000)
        self.assertEqual((10, 3, 1000), generator.next())
        self.assertEqual((2, 10, 1024), generator.next())
        self.assertEqual((33, 2, 1089), generator.next())
        self.assertEqual((34, 2, 1156), generator.next())

    def test_start_from_a_non_power(self):
        generator = Generator(start_from = 1001)
        self.assertEqual((2, 10, 1024), generator.next())
        self.assertEqual((33, 2, 1089), generator.next())
        self.assertEqual((34, 2, 1156), generator.next())

    def test_reverse_from_a_non_power(self):
        generator = Generator(start_from = 1001, reverse = True)
        self.assertEqual((10, 3, 1000), generator.next())
        self.assertEqual((31, 2, 961), generator.next())
        self.assertEqual((30, 2, 900), generator.next())
        self.assertEqual((29, 2, 841), generator.next())
        self.assertEqual((28, 2, 784), generator.next())
        self.assertEqual((3, 6, 729), generator.next())

    def test_reverse_from_a_power(self):
        generator = Generator(start_from = 1000, reverse = True)
        self.assertEqual((31, 2, 961), generator.next())
        self.assertEqual((30, 2, 900), generator.next())
        self.assertEqual((29, 2, 841), generator.next())
        self.assertEqual((28, 2, 784), generator.next())
        self.assertEqual((3, 6, 729), generator.next())

if __name__ == "__main__":
    unittest.main()

