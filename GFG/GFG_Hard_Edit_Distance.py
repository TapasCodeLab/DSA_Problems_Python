#https://www.geeksforgeeks.org/problems/edit-distance3702/1
class Solution:
    def editDistance(self, s1, s2):
        # Code here
        rows, cols = len(s2), len(s1)
        dp = [[0] * (cols + 1) for r in range(rows + 1)]
        for r in range(rows + 1):
            dp[r][0] = r
        for c in range(cols + 1):
            dp[0][c] = c

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if s1[c - 1] == s2[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r][c - 1], dp[r - 1][c], dp[r - 1][c - 1])

        return dp[rows][cols]

        #         a b c d
        #     0   1 2 3 4
        # b   1
        # c   2
        # f   3
        # e   4

        # Below memorization method gives TLE

        # dp = {}

        # def helper(s1, s2):
        #     if (s1,s2) not in dp:
        #         if len(s1)==0:
        #             dp[(s1,s2)] = len(s2)  # All insert
        #         elif len(s2)==0:
        #             dp[(s1,s2)] = len(s1)  # All delete
        #         elif s1[0]==s2[0]:
        #             dp[(s1,s2)] = helper(s1[1:],s2[1:])
        #         else:
        #             insert = 1+helper(s1[:],s2[1:])
        #             remove = 1 + helper(s1[1:], s2[:])
        #             replace = 1 + helper(s1[1:], s2[1:])
        #             dp[(s1,s2)]= min(insert, remove, replace)
        #     return dp[(s1,s2)]

        # return helper(s1,s2)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.editDistance( s1 = "geek", s2 = "gesek"),1)

    def testcase2(self):
        self.assertEqual(self.solution.editDistance( s1 = "gfg", s2 = "gfg"),0)

    def testcase3(self):
        self.assertEqual(self.solution.editDistance( s1 = "abcd", s2 = "bcfe"),3)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()

