import unittest
from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Count set bits
        def setbits(n):
            res = 0
            while n:
                res += 1
                n = n & (n - 1)
            return res

        arr.sort(key=lambda x: (setbits(x), x))
        return arr


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertListEqual(self.solution.sortByBits(arr), [0, 1, 2, 4, 8, 3, 5, 6, 7])

    def testcase2(self):
        arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
        self.assertListEqual(self.solution.sortByBits(arr), [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])

    def testcase3(self):
        arr = [0, 1, 3, 7, 8, 5, 6, 2, 4]
        self.assertListEqual(self.solution.sortByBits(arr), [0, 1, 2, 4, 8, 3, 5, 6, 7])

    def tearDown(self):
        pass