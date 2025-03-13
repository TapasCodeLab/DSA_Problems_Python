#https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        n = len(val)
        dp = [[-1]*(W+1) for _ in range(n)]
        def helper(i, weight):
            if i <0 or weight<0:
                return 0
            else:
                if dp[i][weight] == -1:
                    if weight-wt[i]>=0:
                        dp[i][weight] = val[i]+helper(i-1,weight-wt[i])
                    dp[i][weight] = max(dp[i][weight],helper(i-1,weight))
                return dp[i][weight]

        return helper(n-1,W)

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.knapsack(4, [1, 2, 3], [4, 5, 1] ), 3)

    def testcase2(self):
        self.assertEqual(self.solution.knapsack(3, [1, 2, 3], [4, 5, 6] ), 0)

    def testcase3(self):
        self.assertEqual(self.solution.knapsack(5, [10, 40, 30, 50], [5,4,2,3] ), 80)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

