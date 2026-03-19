from typing import List
import unittest

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        mat = [[[1,0] if grid[r][c]=='X' else [0,1] if grid[r][c]=='Y' else [0,0] for c in range(col)] for r in range(row)]
        result = 0

        for r in range(row):
            for c in range(col):
                prev_row, flag_row = (mat[r-1][c],1) if (r-1)>=0 else ([0,0],0)
                prev_col, flag_col = (mat[r][c-1],1) if (c-1)>=0 else ([0,0],0)
                if flag_row and flag_col:
                    mat[r][c][0] = mat[r][c][0] + prev_row[0] + prev_col[0] -mat[r-1][c-1][0]
                    mat[r][c][1] = mat[r][c][1] + prev_row[1] + prev_col[1] -mat[r-1][c-1][1]
                else:
                    mat[r][c][0] = mat[r][c][0] + prev_row[0] + prev_col[0]
                    mat[r][c][1] = mat[r][c][1] + prev_row[1] + prev_col[1]
                result += 1 if mat[r][c][0]==mat[r][c][1] and mat[r][c][0]>0 else 0

        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.numberOfSubmatrices(grid = [["X","Y"],["Y","X"]]),3)

    def testcase2(self):
        self.assertEqual(self.solution.numberOfSubmatrices(grid = [["X","Y","X"],["Y","X","Y"],["X","Y","X"]]),5)

    def testcase3(self):
        self.assertEqual(self.solution.numberOfSubmatrices(grid = [["X","Y","."],["Y",".","."]]),3)

    def testcase4(self):
        self.assertEqual(self.solution.numberOfSubmatrices(grid = [["X","X"],["X","Y"]]),0)

    def testcase5(self):
        self.assertEqual(self.solution.numberOfSubmatrices(grid = [[".","."],[".","."]]),0)

    def tearDown(self):
        pass
