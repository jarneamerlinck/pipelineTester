#!/usr/bin/env python3

# Imports
import math
import unittest

# Start

class Maintester(unittest.TestCase):
    def setUp(self):
        pass
    def test_demo(self):
        self.assertEqual("test "+ "1 2 3", "test 1 2 3")

    

if __name__ == '__main__':
    unittest.main()
