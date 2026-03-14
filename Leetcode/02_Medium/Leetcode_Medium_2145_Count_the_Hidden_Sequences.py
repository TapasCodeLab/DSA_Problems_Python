from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        res, low, high = 0, 0, 0
        for d in differences:
            res += d
            low = min(low, res)
            high = max(high, res)

        res = (upper - lower) - (high - low) + 1
        return res if res >= 0 else 0

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.numberOfArrays([1,-3,4], 1, 6),2)

    def testcase2(self):
        self.assertEqual(self.solution.numberOfArrays([3,-4,5,1,-2], -4, 5),4)

    def testcase3(self):
        self.assertEqual(self.solution.numberOfArrays([4,-7,2], 3, 6),0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()