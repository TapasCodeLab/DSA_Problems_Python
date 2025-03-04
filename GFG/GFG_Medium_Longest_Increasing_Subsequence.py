class Solution:
    def lis(self, arr):
        # code here
        dp = [1] * len(arr)
        for i in range(1, len(arr), 1):
            temp = [0]
            for j in range(i):
                if arr[j] < arr[i]:
                    temp.append(dp[j])
            dp[i] = max(temp) + 1
        return max(dp)


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.lis([5, 8, 3, 7, 9, 1]),3)

    def testcase2(self):
        self.assertEqual(self.solution.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]),6)

    def testcase3(self):
        self.assertEqual(self.solution.lis([3, 10, 2, 1, 20]),3)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()