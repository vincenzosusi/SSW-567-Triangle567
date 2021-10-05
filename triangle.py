# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(side_a, side_b, side_c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """

    # require that the input values be integers that are > 0 and <= 200
    valid = False
    if isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int):
        if 0 < side_a <= 200 and 0 < side_b <= 200 and 0 < side_c <= 200:
            valid = True
    if not valid:
        return 'InvalidInput'

    # This information was not in the requirements spec but is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side_a > (side_b + side_c)) or (side_b > (side_a + side_c)) or (side_c > (side_a + side_b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if (((side_a ** 2) + (side_b ** 2)) == (side_c ** 2) or
            ((side_c ** 2) + (side_b ** 2)) == (side_a ** 2) or
            ((side_a ** 2) + (side_c ** 2)) == (side_b ** 2)):
        return 'Right'
    if (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isosceles'
