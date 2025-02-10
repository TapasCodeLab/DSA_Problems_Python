import unittest
from Leetcode_3174_Clear_Digits import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_solution1(self):
        self.assertEqual("abc",self.solution.clearDigits("abc"))

    def test_solution2(self):
        self.assertEqual("a", self.solution.clearDigits("abc12"))

    def test_solution3(self):
        self.assertEqual("", self.solution.clearDigits("abc123"))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()