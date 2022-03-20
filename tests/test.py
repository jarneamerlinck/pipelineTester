#!/usr/bin/env python3

# Imports
import math
import unittest
from main import *
# Start

class Maintester(unittest.TestCase):
    def setUp(self):
        pass
    def testSuperClass(self):
        obj = superClass()
        self.assertEqual(obj.execute(12, 4), None)
    
    def testAdding(self):
        obj = adding()
        self.assertEqual(obj.execute(12, 4), 16)
    def testingDivide(self):
        obj = divide()
        self.assertEqual(obj.execute(12, 4), 3)
    def testFormatting(self):
        self.assertEqual(formatting("a", "this is {} in b"), "this is a in b")
    

if __name__ == '__main__':
    unittest.main()
