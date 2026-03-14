from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        pref, suff = [0] * n, [0] * n
        pref[0], suff[n - 1] = 1, 1
        for c in range(1, n):
            if ratings[c] > ratings[c - 1]:
                pref[c] = pref[c - 1] + 1
            else:
                pref[c] = 1

        for c in range(n - 2, -1, -1):
            if ratings[c] > ratings[c + 1]:
                suff[c] = suff[c + 1] + 1
            else:
                suff[c] = 1

        res = [max(pref[i], suff[i]) for i in range(n)]
        return sum(res)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.candy([1,0,2]),5)

    def testcase2(self):
        self.assertEqual(self.solution.candy([1,2,2]),4)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()