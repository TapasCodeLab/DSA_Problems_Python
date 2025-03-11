class Solution:
    def countWays(self, n):
        # code here
        dp = [-1] * max((n + 1), 3)
        dp[0], dp[1], dp[2] = 0, 1, 2

        def helper(n):
            if dp[n] == -1:
                dp[n] = helper(n - 1) + helper(n - 2)
            return dp[n]

        return helper(n)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countWays(1),1)

    def testcase2(self):
        self.assertEqual(self.solution.countWays(2),2)

    def testcase3(self):
        self.assertEqual(self.solution.countWays(4),5)

    def testcase4(self):
        self.assertEqual(self.solution.countWays(44),1134903170)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()

