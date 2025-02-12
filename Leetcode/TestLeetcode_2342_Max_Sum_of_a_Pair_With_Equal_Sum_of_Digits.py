import unittest
from Leetcode_2342_Max_Sum_of_a_Pair_With_Equal_Sum_of_Digits import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(54, self.solution.maximumSum([18,43,36,13,7]))

    def testcase2(self):
        self.assertEqual(-1, self.solution.maximumSum([10,12,19,14]))

    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()