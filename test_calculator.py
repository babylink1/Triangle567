import unittest
from Triangle import classifyTriangle

class TestTriangleClassification(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isosceles')

   # def test_scalene(self):
    #    self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene')

    #def test_not_a_triangle(self):
    #    self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def test_right_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def test_invalid_input(self):
        self.assertEqual(classifyTriangle(201, 1, 1), 'NotATriangle')

   # def test_non_integer_input(self):
   #     self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

if __name__ == '__main__':
    unittest.main()
