import unittest
from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        matrix, n = [], len(grid)
        for r in range(n):
            cnt = 0
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    cnt += 1
                else:
                    break
            matrix.append([r, n - 1 - cnt])

        # Matrix holds the current row vs min allowed row for the gird row
        result = 0
        for src in range(n):
            # select the min row which should be in place of src
            for dest in range(src, n):
                if matrix[dest][1] <= src:
                    break
            # return -1 if no such row exists
            if matrix[dest][1] > src:
                return -1
            # change the rows according to the earlier find # Similar to Bubble sort
            for i in range(dest, src, -1):
                matrix[i], matrix[i-1] = [matrix[i-1][0]+1, matrix[i-1][1]], [matrix[i][0]-1, matrix[i][1]]
                result += 1

        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
        self.assertEqual(self.solution.minSwaps(grid),3)

    def testcase2(self):
        grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
        self.assertEqual(self.solution.minSwaps(grid),-1)

    def testcase3(self):
        grid = [[1,0,0],[1,1,0],[1,1,1]]
        self.assertEqual(self.solution.minSwaps(grid),0)

    def tearDown(self):
        pass
