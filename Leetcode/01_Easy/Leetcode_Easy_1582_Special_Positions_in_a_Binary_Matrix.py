import unittest
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_len, col_len = len(mat), len(mat[0])
        rows, columns = {r:0 for r in range(row_len)}, {c:0 for c in range(col_len)}
        for r in range(row_len):
            for c in range(col_len):
                if mat[r][c] == 1:
                    rows[r] += 1
                    columns[c] += 1

        result = 0
        for r in range(row_len):
            for c in range(col_len):
                if mat[r][c] == 1 and rows[r]==1 and columns[c]==1:
                    result += 1

        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.numSpecial([[1,0,0],[0,0,1],[1,0,0]]),1)

    def testcase2(self):
        self.assertEqual(self.solution.numSpecial([[1,0,0],[0,1,0],[0,0,1]]),3)

    def tearDown(self):
        pass