# https://www.geeksforgeeks.org/problems/number-of-coins1824/1
class Solution:
    def minCoins(self, coins, sum):
        # code here
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0
        coins.sort()

        for coin in coins:
            for i in range(sum + 1):
                if i + coin <= sum:
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin])
                else:
                    continue

        # print(dp)
        return dp[sum] if dp[sum] != float('inf') else -1

        # Below solution works but gives TLE
        # dp=[float('inf')]*(sum+1)
        # dp[0] = 0
        # def helper(x):
        #     if x<0:
        #         return float('inf')
        #     elif dp[x] == float('inf'):
        #         for coin in coins:
        #             dp[x] = min(dp[x], 1+helper(x-coin))
        #     return dp[x]

        # helper(sum)
        # #print(dp)
        # return dp[sum] if dp[sum]!=float('inf') else -1

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minCoins([25, 10, 5],30),2)

    def testcase2(self):
        self.assertEqual(self.solution.minCoins([9, 6, 5, 1],19),3)

    def testcase3(self):
        self.assertEqual(self.solution.minCoins([5,1],0),0)

    def testcase4(self):
        self.assertEqual(self.solution.minCoins([25, 10, 5],14),-1)

    def testcase5(self):
        self.assertEqual(self.solution.minCoins([3, 6, 8],9),2)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()