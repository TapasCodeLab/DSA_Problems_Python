from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j = i + 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break

        return nums


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.applyOperations([1,2,2,1,1,0]), [1,4,2,0,0,0])

    def testcase2(self):
        self.assertEqual(self.solution.applyOperations([0,1]), [1,0])

    def testcase3(self):
        self.assertEqual(self.solution.applyOperations([1,2]), [1,2])

    def testcase4(self):
        self.assertEqual(self.solution.applyOperations([0,0]), [0,0])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()