# https://www.geeksforgeeks.org/problems/smallest-divisor/1
class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        from math import ceil
        def check(x):
            res = 0
            for a in arr:
                res += ceil(a / x)
            return res

        low, high, ans = 1, max(arr), 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.smallestDivisor([1, 2, 5, 9],6),5)

    def testcase2(self):
        self.assertEqual(self.solution.smallestDivisor([1, 1, 1, 1],4),1)

    def testcase3(self):
        self.assertEqual(self.solution.smallestDivisor([4, 4, 4, 4],4),4)

    def testcase4(self):
        self.assertEqual(self.solution.smallestDivisor([1, 5, 3, 9, 15, 7],7),9)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()

