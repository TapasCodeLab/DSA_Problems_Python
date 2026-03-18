import unittest
from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                prev_row, flag_row = (grid[r - 1][c], 1) if (r - 1) >= 0 else (0, 0)
                prev_col, flag_col = (grid[r][c - 1], 1) if (c - 1) >= 0 else (0, 0)
                if flag_row and flag_col:
                    grid[r][c] = grid[r][c] + prev_row + prev_col - grid[r - 1][c - 1]
                else:
                    grid[r][c] = grid[r][c] + prev_row + prev_col

        result = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] <= k:
                    result += 1

        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countSubmatrices(grid = [[7,6,3],[6,6,1]], k = 18),4)

    def testcase2(self):
        self.assertEqual(self.solution.countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20),6)

    def tearDown(self):
        pass