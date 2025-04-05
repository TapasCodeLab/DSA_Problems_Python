# https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1
class Solution:
    def numIslands(self, grid):
        # code here
        res = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "W":
                return
            else:
                grid[row][col] = "W"
                for r, c in [[row - 1, col], [row - 1, col + 1], [row, col + 1], [row + 1, col + 1], [row + 1, col],
                             [row + 1, col - 1], [row, col - 1], [row - 1, col - 1]]:
                    dfs(r, c)
                return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'L':
                    res += 1
                    dfs(row, col)

        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.numIslands(
            [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'],
             ['L', 'W', 'L', 'L', 'W']]), 4)

    def testcase2(self):
        self.assertEqual(self.solution.numIslands(
            [['W', 'L', 'L', 'L', 'W', 'W', 'W'], ['W', 'W', 'L', 'L', 'W', 'L', 'W']]), 2)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()



