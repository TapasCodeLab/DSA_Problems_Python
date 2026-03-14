from typing import List
import unittest
from collections import deque

class Solution:
    @staticmethod
    def validNeighbours(row, col, rowlength, collength):
        return [[newrow, newcol] for newrow, newcol in
                [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col + 1], [row + 1, col + 1],
                 [row + 1, col], [row + 1, col - 1], [row, col - 1]] if
                0 <= newrow < rowlength and 0 <= newcol < collength]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowlength, collength = len(grid), len(grid[0])
        #if start or end is blocked
        if grid[0][0] == 1 or grid[rowlength-1][collength-1] == 1:
            return -1

        queue= deque([[[0,0]]])
        grid[0][0] = 1 #mark it as visited
        while queue:
            path = queue.popleft()
            lastnode = path[-1]
            if lastnode == [rowlength-1,collength-1]:
                print(f"Shortest path : {path}")
                return len(path)
            for newrow, newcol in Solution.validNeighbours(lastnode[0], lastnode[1], rowlength, collength):
                if grid[newrow][newcol] == 0:
                    grid[newrow][newcol] = 1
                    temppath = path[:]
                    temppath.append([newrow,newcol])
                    queue.append(temppath)

        if grid[rowlength-1][collength-1] == 0:  #not required
            return -1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]),2)

    def testcase2(self):
        self.assertEqual(self.solution.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]),4)

    def testcase3(self):
        self.assertEqual(self.solution.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]),-1)

    def testcase4(self):
        self.assertEqual(self.solution.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,1]]),-1)

    def testcase5(self):
        self.assertEqual(self.solution.shortestPathBinaryMatrix(grid = [[0,1,1],[1,1,1],[1,1,0]]),-1)

    def testcase6(self):
        self.assertEqual(self.solution.shortestPathBinaryMatrix(grid = [[0,0,0],[0,0,0],[0,0,0]]),3)

    def testcase7(self):
        self.assertEqual(self.solution.shortestPathBinaryMatrix(grid = [[0]]),1)

    def tearDown(self):
        pass


