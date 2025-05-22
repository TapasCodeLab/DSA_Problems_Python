class Solution:
    def minDeletions(self, s):
        # code here
        word, rev = s, s[::-1]
        print(word, rev)
        n = len(s)
        mat = [[0] * (n + 1) for _ in range(n + 1)]
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                if word[c - 1] == rev[r - 1]:
                    mat[r][c] = max(mat[r - 1][c], mat[r][c - 1], 1 + mat[r - 1][c - 1])
                else:
                    mat[r][c] = max(mat[r - 1][c], mat[r][c - 1])

        return n - mat[n][n]


import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def testcase1(self):
        self.assertEqual(self.s.minDeletions('aebcbda'),2)

    def testcase2(self):
        self.assertEqual(self.s.minDeletions('geeksforgeeks'),8)

    def tearDown(self):
        pass
