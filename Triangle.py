"""
This module provides a function to classify triangles
based on the lengths of their sides.
"""

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its three sides.
    
    Args:
        a (int): The length of side a.
        b (int): The length of side b.
        c (int): The length of side c.
    
    Returns:
        str: A string indicating the type of triangle ('Equilateral', 'Isoceles', 
        'Scalene', 'Right', 'NotATriangle', or 'InvalidInput').
    """
    if any(side > 200 or side <= 0 for side in [a, b, c]):
        result = 'InvalidInput'
    elif not all(isinstance(side, int) for side in [a, b, c]):
        result = 'InvalidInput'
    else:
        sides = sorted([a, b, c])
        if sides[0] + sides[1] <= sides[2]:
            result = 'NotATriangle'
        elif a == b == c:
            result = 'Equilateral'
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                result = 'Right'
            else:
                result = 'Isoceles'
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            result = 'Right'
        else:
            result = 'Scalene'

    return result
