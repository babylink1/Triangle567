# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Lijuan Liu

"""

import unittest
from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):

    def testEquilateral(self):
        # Test Equilateral triangle
        self.assertEqual(classifyTriangle(5, 5, 5),
                         'Equilateral', '5,5,5 should be Equilateral')

    def testRightTriangle(self):
        # Test Right triangle
        self.assertEqual(classifyTriangle(3, 4, 5),
                         'Right', '3,4,5 should be Right')

    def testIsosceles(self):
        # Test Isosceles triangle
        self.assertEqual(classifyTriangle(5, 5, 6),
                         'Isosceles', '5,5,6 should be Isosceles')

    def testScalene(self):
        # Test Scalene triangle
        self.assertEqual(classifyTriangle(7, 8, 9),
                         'Scalene', '7,8,9 should be Scalene')

    def testNotATriangle(self):
        # Test Not a triangle
        self.assertEqual(classifyTriangle(1, 2, 3),
                         'NotATriangle', '1,2,3 should be NotATriangle')

    def testInvalidInputA(self):
        # Test Invalid input (out of range)
        self.assertEqual(classifyTriangle(201, 200, 199),
                         'InvalidInput', '201,200,199 should be InvalidInput')

    def testInvalidInputB(self):
        # Test Invalid input (negative sides)
        self.assertEqual(classifyTriangle(-2, 3, 3),
                         'InvalidInput', '-2,3,3 should be InvalidInput')

    def testInvalidInputC(self):
        # Test Invalid input (zero side)
        self.assertEqual(classifyTriangle(0, 0, 0),
                         'InvalidInput', '0,0,0 should be InvalidInput')

    def testInvalidInputD(self):
        # Test Invalid input (float sides)
        self.assertEqual(classifyTriangle(1.3, 2, 2.3),
                         'InvalidInput', '1.3,2,2.3 should be InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
