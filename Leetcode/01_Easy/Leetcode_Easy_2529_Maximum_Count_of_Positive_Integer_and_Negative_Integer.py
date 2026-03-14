from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        first_pos = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > 0:
                first_pos = mid
                high = mid - 1
            else:
                low = mid + 1
        low, high = 0, n - 1
        last_neg = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < 0:
                last_neg = mid
                low = mid + 1
            else:
                high = mid - 1

        # print(last_neg, first_pos,last_neg+1,n-first_pos)
        return max(last_neg + 1, n - first_pos)


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maximumCount([-2,-1,-1,1,2,3]),3)

    def testcase2(self):
        self.assertEqual(self.solution.maximumCount([-3,-2,-1,0,0,1,2]),3)

    def testcase3(self):
        self.assertEqual(self.solution.maximumCount([5,20,66,1314]),4)

    def testcase4(self):
        self.assertEqual(self.solution.maximumCount([-5,-3,-2,-1]),4)

    def testcase5(self):
        self.assertEqual(self.solution.maximumCount([0,0,0,0,0]),0)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()