# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testInvalidTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 4, 7), 'NotATriangle', '1,4,7 is not a Triangle')
    def testInvalidTrianglesB(self):
        self.assertEqual(classifyTriangle(0, 0, 7), 'NotATriangle', '0,0,7 is not a Triangle')
    def testInvalidTrianglesC(self):
        self.assertEqual(classifyTriangle(-10, 6, 8), 'NotATriangle', '-10,6,8 is not a Triangle')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isosceles', '1,2,2 should be Isosceles')
    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(2, 1, 2), 'Isosceles', '2,1,2 should be Isosceles')
    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isosceles', '2,2,1 should be Isosceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(2, 3, 1), 'Scalene', '2,3,1 should be scalene')
    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'Scalene', '1,2,3 should be scalene')
    def testScaleneTrianglesC(self):
        self.assertEqual(classifyTriangle(3, 1, 2), 'Scalene', '3,1,2 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
