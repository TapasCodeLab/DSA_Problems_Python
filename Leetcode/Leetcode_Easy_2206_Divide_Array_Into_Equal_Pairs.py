from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        freq = Counter(nums)
        for val in freq.values():
            if val&1==1:
                return False
        return True

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.divideArray([3,2,3,2,2,2]))

    def testcase2(self):
        self.assertFalse(self.solution.divideArray([1,2,3,4]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
