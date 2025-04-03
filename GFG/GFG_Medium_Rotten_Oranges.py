# https://www.geeksforgeeks.org/problems/rotten-oranges2536/1
class Solution:
    def orangesRotting(self, mat):
        # Code here
        from collections import deque
        queue = deque([])
        fresh, rotten, time = 0, 0, 0

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    fresh += 1
                elif mat[r][c] == 2:
                    queue.append([r, c])

        while queue:
            n = len(queue)
            time += 1
            for _ in range(n):
                r, c = queue.popleft()
                for row, col in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == 1:
                        mat[row][col] = 2
                        rotten += 1
                        queue.append([row, col])

        if rotten == fresh and time > 0:
            return time - 1
        elif fresh > rotten:
            return -1
        else:
            return 0

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.orangesRotting([[0, 1, 2], [0, 1, 2], [2, 1, 1]]),1)

    def testcase2(self):
        self.assertEqual(self.solution.orangesRotting([[2, 2, 0, 1]]),-1)

    def testcase3(self):
        self.assertEqual(self.solution.orangesRotting([[2, 2, 2], [0, 2, 0]]),0)

    def testcase4(self):
        self.assertEqual(self.solution.orangesRotting([[0,0,0,0]]),0)

    def testcase5(self):
        self.assertEqual(self.solution.orangesRotting([[2, 2, 2, 0]]),0)

    def testcase6(self):
        self.assertEqual(self.solution.orangesRotting([[1, 1, 0, 0]]),-1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
