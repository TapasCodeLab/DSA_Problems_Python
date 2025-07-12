# https://www.geeksforgeeks.org/problems/gold-mine-problem2608/1

class Solution:
    def maxGold(self, mat):
        # code here
        rows, cols = len(mat), len(mat[0])

        dp = [mat[r][cols - 1] for r in range(rows)]
        for col in range(cols - 2, -1, -1):
            newdp = [0] * rows
            for row in range(rows):
                newdp[row] = mat[row][col] + max(
                    [dp[row - 1] if row > 0 else 0, dp[row], dp[row + 1] if row < rows - 1 else 0])
            dp = newdp

        return max(dp)


import unittest


class TestSolution(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maxGold([[1, 3, 3], [2, 1, 4], [0, 6, 4]]), 12)

    def testcase2(self):
        self.assertEqual(self.solution.maxGold([[1, 3, 1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]), 16)

    def testcase3(self):
        self.assertEqual(self.solution.maxGold([[1, 3, 3], [2, 1, 4], [0, 7, 5]]), 14)

    def testcase4(self):
        self.assertEqual(self.solution.maxGold([[1, 3, 3, 4, 2], [2, 1, 4, 5, 7],[0, 6, 4, 6, 1]]), 25)

    def testcase5(self):
        self.assertEqual(self.solution.maxGold([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]), 0)

if __name__ == '__main__':
    unittest.main()