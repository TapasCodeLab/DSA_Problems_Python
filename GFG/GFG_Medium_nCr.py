# https://www.geeksforgeeks.org/problems/ncr1019/1
class Solution:
    def nCr(self, n, r):
        # code here
        def fact(n):
            if n == 0:
                return 1
            else:
                return n * fact(n - 1)

        if r > n:
            return 0
        else:
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i

            return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.nCr(n = 5, r = 2),10)

    def testcase2(self):
        self.assertEqual(self.solution.nCr(n = 2, r = 4),0)

    def testcase3(self):
        self.assertEqual(self.solution.nCr(n = 5, r = 0),1)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()