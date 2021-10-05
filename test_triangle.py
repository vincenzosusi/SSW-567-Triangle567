# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """
    Tests the classify_triangle function
    """

    def test_right_triangle_a(self):
        """
        Tests that classify_triangle correctly classifies right triangles where a^2 + b^2 = c^2
        """
        self.assertEqual('Right', classify_triangle(3, 4, 5), '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """
        Tests that classify_triangle correctly classifies right triangles where b^2 + c^2 = a^2
        """
        self.assertEqual('Right', classify_triangle(5, 3, 4), '5,3,4 is a Right triangle')

    def test_right_triangle_c(self):
        """
        Tests that classify_triangle correctly classifies right triangles where c^2 + a^2 = b^2
        """
        self.assertEqual('Right', classify_triangle(4, 5, 3),  '4,5,3 is a Right triangle')

    def test_equilateral_triangles(self):
        """
        Tests that classify_triangle correctly classifies equilateral triangles
        """
        self.assertEqual('Equilateral', classify_triangle(1, 1, 1), '1,1,1 should be equilateral')

    def test_invalid_triangle_a(self):
        """
        Tests that classify_triangle correctly classifies invalid triangles when
        sum of two sides is not greater than the third side
        """
        self.assertEqual('NotATriangle', classify_triangle(1, 4, 7), '1,4,7 is not a Triangle')

    def test_invalid_triangle_b(self):
        """
        Tests that classify_triangle correctly classifies invalid triangles when a side length is 0
        """
        self.assertEqual('InvalidInput', classify_triangle(0, 0, 7), '0,0,7 is not a Triangle')

    def test_invalid_triangle_c(self):
        """
        Tests that classify_triangle correctly classifies invalid triangles with
        a negative side length
        """
        self.assertEqual('InvalidInput', classify_triangle(-10, 6, 8), '-10,6,8 is not a Triangle')

    def test_isosceles_triangle_a(self):
        """
        Tests that classify_triangle correctly classifies isosceles triangles
        """
        self.assertEqual('Isosceles', classify_triangle(1, 2, 2), '1,2,2 should be Isosceles')

    def test_isosceles_triangle_b(self):
        """
        Tests that classify_triangle correctly classifies isosceles triangles
        """
        self.assertEqual('Isosceles', classify_triangle(2, 1, 2), '2,1,2 should be Isosceles')

    def test_isosceles_triangle_c(self):
        """
        Tests that classify_triangle correctly classifies isosceles triangles
        """
        self.assertEqual('Isosceles', classify_triangle(2, 2, 1), '2,2,1 should be Isosceles')

    def test_scalene_triangle_a(self):
        """
        Tests that classify_triangle correctly classifies scalene triangles
        """
        self.assertEqual('Scalene', classify_triangle(2, 3, 1), '2,3,1 should be scalene')

    def test_scalene_triangle_b(self):
        """
        Tests that classify_triangle correctly classifies scalene triangles
        """
        self.assertEqual('Scalene', classify_triangle(1, 2, 3), '1,2,3 should be scalene')

    def test_scalene_triangle_c(self):
        """
        Tests that classify_triangle correctly classifies scalene triangles
        """
        self.assertEqual('Scalene', classify_triangle(3, 1, 2), '3,1,2 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
