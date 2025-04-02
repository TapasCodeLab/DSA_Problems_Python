from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    res = max(res, ((nums[i]-nums[j])*nums[k]))

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


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
