# https://www.geeksforgeeks.org/problems/unique-paths-in-a-grid--170647/1

class Solution:
    def uniquePaths(self, grid):
        # code here
        rows, cols = len(grid), len(grid[0])
        prev = [0] * cols
        prev[0] = 1 if grid[0][0] == 0 else 0
        for i in range(1, cols):
            if grid[0][i] == 0:
                prev[i] = prev[i - 1]
            else:
                prev[i] = 0

        for r in range(1, rows):
            curr = [0] * cols
            for c in range(cols):
                if grid[r][c] == 0:
                    if c == 0:
                        curr[c] = prev[c]
                    else:
                        curr[c] = prev[c] + curr[c - 1]
                else:
                    curr[c] = 0
            prev = curr

        return prev[cols - 1]

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.uniquePaths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),2)

    def testcase2(self):
        self.assertEqual(self.solution.uniquePaths([[1, 0, 0], [0, 1, 0], [0, 0, 0]]),0)

    def testcase3(self):
        self.assertEqual(self.solution.uniquePaths([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),0)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()