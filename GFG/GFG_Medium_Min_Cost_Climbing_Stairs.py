#https://www.geeksforgeeks.org/problems/min-cost-climbing-stairs/1
class Solution:
    def minCostClimbingStairs(self, cost):
        # Write your code here
        cost.append(0)
        n = len(cost)
        dp = [-1] * (n)

        def helper(n):
            if n < 0:
                return 0
            if dp[n] == -1:
                dp[n] = min(helper(n - 1), helper(n - 2)) + cost[n]
            return dp[n]

        return helper(n - 1)


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minCostClimbingStairs([10, 15, 20]),15)

    def testcase2(self):
        self.assertEqual(self.solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),6)

    def testcase3(self):
        self.assertEqual(self.solution.minCostClimbingStairs([1, 15]),1)

    def testcase4(self):
        self.assertEqual(self.solution.minCostClimbingStairs([10, 1]),1)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()