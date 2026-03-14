from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, more = [], [], []
        for n in nums:
            if n<pivot:
                less.append(n)
            if n==pivot:
                equal.append(n)
            if n>pivot:
                more.append(n)
        return less+equal+more

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.pivotArray([9,12,5,10,14,3,10],10),[9,5,3,10,10,12,14])

    def testcase2(self):
        self.assertEqual(self.solution.pivotArray([-3,4,3,2],2),[-3,2,4,3])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
