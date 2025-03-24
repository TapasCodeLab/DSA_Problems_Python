# https://www.geeksforgeeks.org/problems/total-decoding-messages1235/1

# User function Template for python3
class Solution:
    def countWays(self, digits):
        # Code here
        n = len(digits)
        dp = [0] * (n + 1)
        dp[0] = 1

        def isValid(st):
            return (len(st) == len(str(int(st)))) and (1 <= int(st)) and (int(st) <= 26)

        for i in range(n):
            if isValid(digits[i]):
                dp[i + 1] = dp[i]
            if i > 0 and isValid(digits[i - 1:i + 1]):
                dp[i + 1] += dp[i - 1]

        # print(dp)
        return dp[n]


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countWays("123"),3)

    def testcase2(self):
        self.assertEqual(self.solution.countWays("90"),0)

    def testcase3(self):
        self.assertEqual(self.solution.countWays("05"),0)

    def testcase4(self):
        self.assertEqual(self.solution.countWays("1232"),3)

    def testcase5(self):
        self.assertEqual(self.solution.countWays("1222"),5)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
