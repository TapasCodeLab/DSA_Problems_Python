# https://www.geeksforgeeks.org/problems/dice-throw5349/1

class Solution:
    def noOfWays(self, m, n, x):
        # code here

        # code here
        prev = [0] * (x + 1)
        for i in range(1, min(x + 1, m + 1)):
            prev[i] = 1
        for _ in range(n - 1):
            curr = [0] * (x + 1)
            for i in range(x + 1):
                res = 0
                for a in range(max(0, i - m), i):
                    res += prev[a]
                curr[i] = res

            prev = curr[:]

        return prev[x]


import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def testcase1(self):
        self.assertEqual(self.s.noOfWays(m = 6, n = 3, x = 12),25)

    def testcase2(self):
        self.assertEqual(self.s.noOfWays(m = 2, n = 3, x = 6),1)

    def tearDown(self):
        pass
