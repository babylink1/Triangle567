# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:44:00 2023


The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Lijuan Liu

"""


def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    def classifyTriangle(a, b, c):
        # Require that the input values be >= 0 and <= 200
        if a > 200 or b > 200 or c > 200:
            return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Verify that all 3 inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Check if it's a valid triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # Now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 'Right'
    elif a != b and b != c and a != c:
        return 'Scalene'
    else:
        return 'Isosceles'
