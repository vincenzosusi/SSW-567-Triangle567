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
        self.assertEqual('Right', classifyTriangle(3, 4, 5), '3,4,5 is a Right triangle')
    def testRightTriangleB(self):
        self.assertEqual('Right', classifyTriangle(5, 3, 4), '5,3,4 is a Right triangle')
    def testRightTriangleC(self):
        self.assertEqual('Right', classifyTriangle(4, 5, 3),  '4,5,3 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual('Equilateral', classifyTriangle(1, 1, 1), '1,1,1 should be equilateral')

    def testInvalidTriangleA(self):
        self.assertEqual('NotATriangle', classifyTriangle(1, 4, 7), '1,4,7 is not a Triangle')
    def testInvalidTriangleB(self):
        self.assertEqual('InvalidInput', classifyTriangle(0, 0, 7), '0,0,7 is not a Triangle')
    def testInvalidTriangleC(self):
        self.assertEqual('InvalidInput', classifyTriangle(-10, 6, 8), '-10,6,8 is not a Triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual('Isosceles', classifyTriangle(1, 2, 2), '1,2,2 should be Isosceles')
    def testIsoscelesTriangleB(self):
        self.assertEqual('Isosceles', classifyTriangle(2, 1, 2), '2,1,2 should be Isosceles')
    def testIsoscelesTriangleC(self):
        self.assertEqual('Isosceles', classifyTriangle(2, 2, 1), '2,2,1 should be Isosceles')

    def testScaleneTriangleA(self):
        self.assertEqual('Scalene', classifyTriangle(2, 3, 1), '2,3,1 should be scalene')
    def testScaleneTriangleB(self):
        self.assertEqual('Scalene', classifyTriangle(1, 2, 3), '1,2,3 should be scalene')
    def testScaleneTriangleC(self):
        self.assertEqual('Scalene', classifyTriangle(3, 1, 2), '3,1,2 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
