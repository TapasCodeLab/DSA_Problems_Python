from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        pref_max, suff_max = [], []
        pref, suff, res = 0, 0, 0
        for i in range(len(nums)):
            pref_max.append(pref)
            pref = max(pref, nums[i])

        for i in range(len(nums)-1,-1,-1):
            suff_max.append(suff)
            suff = max(suff, nums[i])

        suff_max = suff_max[::-1]

        for i in range(1,len(nums)-1):
            res = max(res, ((pref_max[i]-nums[i])*suff_max[i]))

        return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maximumTripletValue([12,6,1,2,7]),77)

    def testcase2(self):
        self.assertEqual(self.solution.maximumTripletValue([1,10,3,4,19]),133)

    def testcase3(self):
        self.assertEqual(self.solution.maximumTripletValue([1,2,3]),0)

    def testcase4(self):
        self.assertEqual(self.solution.maximumTripletValue([6,11,12,12,7,9,2,11,12,4,19,14,16,8,16]),190)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
