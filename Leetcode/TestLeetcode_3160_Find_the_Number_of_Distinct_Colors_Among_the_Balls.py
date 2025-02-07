import unittest
from Leetcode.Leetcode_3160_Find_the_Number_of_Distinct_Colors_Among_the_Balls import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_queryResults_override(self):
        self.assertEqual(self.solution.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]), [1,2,2,3])

    def test_queryResults_same_color(self):
        self.assertEqual(self.solution.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]), [1,2,2,3,4])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
