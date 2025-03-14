from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def maxChild(candy):
            res = 0
            for x in candies:
                res += x // candy
            return res

        ans = 0
        low, high = 1, max(candies)
        while low <= high:
            mid = (low + high) // 2
            if maxChild(mid) >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maximumCandies([5,8,6],3),5)

    def testcase2(self):
        self.assertEqual(self.solution.maximumCandies([2,5],11),0)

    def testcase3(self):
        self.assertEqual(self.solution.maximumCandies([5,9,6],6),3)

    def testcase4(self):
        self.assertEqual(self.solution.maximumCandies([5,90,6],6),15)

    def testcase5(self):
        self.assertEqual(self.solution.maximumCandies([5,90,6],1),90)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
