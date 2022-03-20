#!/usr/bin/env python3

# Imports
import math
import unittests
from main import adding
# Start

class Maintester(unittests.Testcase):
    def setUp(self):
        pass
    def testAdding(self):
        self.assertEqual(adding(3, 5), 8)



if __name__ == '__main__':
    unittest.main()
