class Solution:
    def count(self, coins, sum):
        # code here
        dp = [0 for _ in range(sum + 1)]
        dp[0] = 1
        coins.sort()

        for i in range(len(coins)):
            for j in range(sum + 1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[sum]

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.count([1,2,3],4),4)

    def testcase2(self):
        self.assertEqual(self.solution.count([2,5,3,6],10),5)

    def testcase3(self):
        self.assertEqual(self.solution.count([5,10],4),0)

    def testcase4(self):
        self.assertEqual(self.solution.count([4, 3, 7, 2, 8, 10, 9, 3, 2, 3],100),9146027)

    def testcase5(self):
        self.assertEqual(self.solution.count([4, 3, 7, 2, 8, 10, 9, 3, 2, 3],200),1869687600)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
