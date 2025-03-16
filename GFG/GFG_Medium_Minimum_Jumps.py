# https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

class Solution:
    def minJumps(self, arr):
        # code here
        dp = [float('inf')]*len(arr)
        dp[0] = 0
        n = len(arr)
        for i in range(n):
            for x in range(1,arr[i]+1):
                if i+x<n:
                    dp[i+x] = min(dp[i+x],1+dp[i])
                if dp[n-1]!=float('inf'):
                    return dp[n-1]

        #return dp[n-1] if dp[n-1]!=float('inf') else -1
        return -1


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]),3)

    def testcase2(self):
        self.assertEqual(self.solution.minJumps([1, 4, 3, 2, 6, 7]),2)

    def testcase3(self):
        self.assertEqual(self.solution.minJumps([0, 10, 20]),-1)

    def testcase4(self):
        self.assertEqual(self.solution.minJumps([1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 9]),-1)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()