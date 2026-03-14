from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        lst = [grid[r][c] for c in range(len(grid[0])) for r in range(len(grid))]
        lst.sort()
        median = lst[len(lst) // 2]
        res = 0
        for num in lst:
            if abs(num - median) % x != 0:
                return -1
            res += abs(num - median) // x
        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minOperations([[2,4],[6,8]], 2),4)

    def testcase2(self):
        self.assertEqual(self.solution.minOperations([[1,5],[2,3]], 1), 5)

    def testcase3(self):
        self.assertEqual(self.solution.minOperations([[1,2],[3,4]], 2), -1)

    def testcase4(self):
        self.assertEqual(self.solution.minOperations([[2,4,16,78],[6,8,40,10]], 2), 62)

    def testcase5(self):
        self.assertEqual(self.solution.minOperations([[2,4,16,78,3],[6,8,40,10,7]], 2), -1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
