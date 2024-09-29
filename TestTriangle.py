import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    # Test Right Triangles
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')
    
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5, 12, 13 is a Right triangle')

    # Test Equilateral Triangle
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    # Test Isosceles Triangles
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isoceles', '5, 5, 8 should be Isosceles')
    
    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(8, 8, 5), 'Isoceles', '8, 8, 5 should be Isosceles')

    # Test Scalene Triangle
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(7, 5, 9), 'Scalene', '7, 5, 9 should be Scalene')

    # Test Not A Triangle
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1, 2, 3 is not a triangle')
    
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(5, 9, 3), 'NotATriangle', '5, 9, 3 is not a triangle')

    # Test Invalid Inputs
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(201, 1, 1), 'InvalidInput', '201, 1, 1 is Invalid Input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1, 5, 7), 'InvalidInput', '-1, 5, 7 is Invalid Input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(5.5, 5, 5), 'InvalidInput', '5.5, 5, 5 is Invalid Input')

if __name__ == '__main__':
    unittest.main()

