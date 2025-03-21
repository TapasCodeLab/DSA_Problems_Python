# https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1
class Solution:
    def findMaxSum(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]
        else:
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
            return dp[n - 1]


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.findMaxSum([6, 5, 5, 7, 4]),15)

    def testcase2(self):
        self.assertTrue(self.solution.findMaxSum([1, 5, 3]),5)

    def testcase3(self):
        self.assertTrue(self.solution.findMaxSum([4,4,4,4]),8)

    def testcase4(self):
        self.assertTrue(self.solution.findMaxSum([4,4,4,4,4]),12)

    def testcase5(self):
        self.assertTrue(self.solution.findMaxSum([6]),6)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
