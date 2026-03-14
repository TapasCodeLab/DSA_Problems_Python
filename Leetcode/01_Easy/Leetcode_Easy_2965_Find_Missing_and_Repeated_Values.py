from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        _total_sum, _total_xor = 0, 0
        for i in range(n ** 2 + 1):
            _total_sum += i
            _total_xor ^= i

        _xor = 0
        _set = set()
        for r in range(n):
            for c in range(n):
                _set.add(grid[r][c])
                _xor ^= grid[r][c]

        missing = _total_sum - sum(_set)
        repeated = _total_xor ^ missing ^ _xor

        return [repeated, missing]

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.findMissingAndRepeatedValues([[1,3],[2,2]]),[2,4])

    def testcase2(self):
        self.assertEqual(self.solution.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]),[9,5])

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()