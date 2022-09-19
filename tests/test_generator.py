#!/usr/bin/env python3

# Copyright (c) 2022 Edmundo Carmona Antoranz
# Released under the terms of GPLv3

import unittest

from pywerhose import Generator

class BasicTest(unittest.TestCase):

    def test_basic(self):
        generator = Generator()
        self.assertEqual((2, 2, 4), generator.next_power())
        self.assertEqual((2, 3, 8), generator.next_power())
        self.assertEqual((3, 2, 9), generator.next_power())
        self.assertEqual((2, 4, 16), generator.next_power())
        self.assertEqual((5, 2, 25), generator.next_power())
        self.assertEqual((3, 3, 27), generator.next_power())

    def test_with_min_base(self):
        generator = Generator(min_base = 4)
        self.assertEqual((4, 2, 16), generator.next_power())
        self.assertEqual((5, 2, 25), generator.next_power())
        self.assertEqual((6, 2, 36), generator.next_power())
        self.assertEqual((7, 2, 49), generator.next_power())
        self.assertEqual((4, 3, 64), generator.next_power())
        self.assertEqual((9, 2, 81), generator.next_power())
        self.assertEqual((10, 2, 100), generator.next_power())
        self.assertEqual((11, 2, 121), generator.next_power())
        self.assertEqual((5, 3, 125), generator.next_power())
    
    def test_with_min_power(self):
        generator = Generator(min_power = 3)
        self.assertEqual((2, 3, 8), generator.next_power())
        self.assertEqual((2, 4, 16), generator.next_power())
        self.assertEqual((3, 3, 27), generator.next_power())
        self.assertEqual((2, 5, 32), generator.next_power())
        self.assertEqual((2, 6, 64), generator.next_power())
        self.assertEqual((3, 4, 81), generator.next_power())
        self.assertEqual((5, 3, 125), generator.next_power())
        self.assertEqual((2, 7, 128), generator.next_power())

    def test_with_step(self):
        generator = Generator(step = 3)
        self.assertEqual((2, 2, 4), generator.next_power())
        self.assertEqual((2, 3, 8), generator.next_power())
        self.assertEqual((2, 4, 16), generator.next_power())
        self.assertEqual((5, 2, 25), generator.next_power())
        self.assertEqual((2, 5, 32), generator.next_power())
        self.assertEqual((2, 6, 64), generator.next_power())
        self.assertEqual((11, 2, 121), generator.next_power())
        self.assertEqual((5, 3, 125), generator.next_power())
        self.assertEqual((2, 7, 128), generator.next_power())


if __name__ == "__main__":
    unittest.main()

