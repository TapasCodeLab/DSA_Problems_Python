import unittest

from Leetcode_1352_Product_of_the_Last_K_Numbers import ProductOfNumbers

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = ProductOfNumbers()

    def testcase1(self):
        self.solution.add(3)
        self.solution.add(0)
        self.solution.add(2)
        self.solution.add(5)
        self.solution.add(4)
        self.assertEqual(self.solution.getProduct(2),20)
        self.assertEqual(self.solution.getProduct(3),40)
        self.assertEqual(self.solution.getProduct(4),00)
        self.solution.add(8)
        self.assertEqual(self.solution.getProduct(2),32)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
