import unittest
from Leetcode_2364_Count_Number_of_Bad_Pairs import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_solution1(self):
        self.assertEqual(5,self.solution.countBadPairs([4, 1, 3, 3]))

    def test_solution2(self):
        self.assertEqual(0, self.solution.countBadPairs([1, 2, 3, 4, 5]))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


