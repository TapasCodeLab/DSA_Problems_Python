class Solution:
    def lcs(self, s1, s2):
        # code here
        dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        for r in range(1, len(s2) + 1):
            for c in range(1, len(s1) + 1):
                if s1[c - 1] == s2[r - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

        return dp[len(s2)][len(s1)]


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.lcs(s1="ABCDGH", s2="AEDFHR"),3)

    def testcase2(self):
        self.assertEqual(self.solution.lcs(s1 = "ABC", s2 = "AC"),2)

    def testcase3(self):
        self.assertEqual(self.solution.lcs(s1 = "XYZW", s2 = "XYWZ"),3)

    def testcase4(self):
        self.assertEqual(self.solution.lcs(s1 = "XYZW", s2 = "ABCD"),0)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()