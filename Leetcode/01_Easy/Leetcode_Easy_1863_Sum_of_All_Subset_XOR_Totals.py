from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        self.res = 0
        def helper(ind, total, n):
            if ind==n:
                self.res += total
                return
            else:
                helper(ind+1,total,n)
                helper(ind+1,total^nums[ind],n)

        helper(0,0,n)
        return self.res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.subsetXORSum([1,3]),6)

    def testcase2(self):
        self.assertEqual(self.solution.subsetXORSum([5,1,6]),28)

    def testcase3(self):
        self.assertEqual(self.solution.subsetXORSum([3,4,5,6,7,8]),480)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
