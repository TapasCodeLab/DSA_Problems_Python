from collections import deque
from typing import List
import unittest

class Solution:
    @staticmethod
    def findNeighbours(row, col, rowLength, colLength):
        res = []
        for new_row, new_col in [[row+1, col], [row-1,col], [row,col+1], [row,col-1]]:
            if 0 <= new_row < rowLength and 0 <= new_col < colLength:
                res.append([new_row, new_col])
        return res

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        time_reached = 0
        rowLength, colLength = len(grid), len(grid[0])
        # Add all the rotten oranges in the queue
        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == 2:
                    queue.append([row,col,0])  # row, col, time

        while queue:
            row, col, time = queue.popleft()
            for new_row, new_col in Solution.findNeighbours(row, col, rowLength, colLength):
                if grid[new_row][new_col] ==1:
                    grid[new_row][new_col] = 2
                    queue.append([new_row, new_col, time+1])
                    time_reached = max(time_reached, time+1)

        # Check if all the oranges are rotten
        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == 1:
                    return -1

        return time_reached


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]),4)

    def testcase2(self):
        self.assertEqual(self.solution.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]),-1)

    def testcase3(self):
        self.assertEqual(self.solution.orangesRotting(grid = [[0,2]]),0)

    def testcase4(self):
        self.assertEqual(self.solution.orangesRotting(grid = [[2,0,0],[0,0,0],[0,0,1]]),-1)

    def testcase5(self):
        self.assertEqual(self.solution.orangesRotting(grid = [[0]]),0)

    def tearDown(self):
        pass



