from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        distinct = set(nums)
        flag = True
        res = 0
        for n in distinct:
            if n>k:
                res += 1
            elif n<k:
                flag = False
        return res if flag else -1

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minOperations(nums = [5,2,5,4,5], k = 2),2)

    def testcase2(self):
        self.assertEqual(self.solution.minOperations(nums = [2,1,2], k = 2),-1)

    def testcase3(self):
        self.assertEqual(self.solution.minOperations(nums = [9,7,5,3], k = 1),4)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()