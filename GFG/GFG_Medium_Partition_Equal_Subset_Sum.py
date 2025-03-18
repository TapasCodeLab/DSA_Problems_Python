# https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1
class Solution:
    def equalPartition(self, arr):
        # code here
        total = sum(arr)
        if total % 2 == 1:
            return False
        else:
            half = total // 2

        dp = [[-1 for c in range(len(arr) + 1)] for r in range(half + 1)]
        for c in range(len(arr) + 1):
            dp[0][c] = True

        def helper(total, ind):
            if total < 0 or ind <= 0:
                return False
            if dp[total][ind] == -1:
                dp[total][ind] = helper(total, ind - 1) or helper(total - arr[ind - 1], ind - 1)
            return dp[total][ind]

        return helper(half, len(arr))

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.equalPartition([1, 5, 11, 5]))

    def testcase2(self):
        self.assertFalse(self.solution.equalPartition([1, 3, 5]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
