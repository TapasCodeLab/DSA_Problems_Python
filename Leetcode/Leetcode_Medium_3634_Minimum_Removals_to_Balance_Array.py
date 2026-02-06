from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        i, j = 0, 0
        while j < n:
            if nums[i]*k>= nums[j]:
                result = max(result, j-i+1)
                j += 1
            else:
                i+=1
        return n-result


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minRemoval([2,1,5],2),1)

    def testcase2(self):
        self.assertEqual(self.solution.minRemoval([1,6,2,9],3),2)

    def testcase3(self):
        self.assertEqual(self.solution.minRemoval([4,6],2),0)

    def testcase4(self):
        self.assertEqual(self.solution.minRemoval([1,6,2,9,3,7,2,8,3,2,1,9,4,10],3),6)

    def tearDown(self):
        pass
