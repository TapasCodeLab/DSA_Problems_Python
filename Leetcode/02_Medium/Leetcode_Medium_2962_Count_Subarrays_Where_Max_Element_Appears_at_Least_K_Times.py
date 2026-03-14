from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, count, max_elem, length = 0, 0, max(nums), len(nums)
        start = 0
        for end in range(length):
            count += 1 if nums[end]==max_elem else 0
            while count>=k:
                res += length-end
                count -= 1 if nums[start]==max_elem else 0
                start += 1

        return res


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countSubarrays([1,3,2,3,3], 2),6)

    def testcase2(self):
        self.assertEqual(self.solution.countSubarrays([1,4,2,1],3),0)

    def testcase3(self):
        self.assertEqual(self.solution.countSubarrays([1,4,2,4,1],1),12)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()