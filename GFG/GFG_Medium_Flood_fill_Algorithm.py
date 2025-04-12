class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # Code here
        from collections import deque
        queue = deque([[sr, sc]])
        oldColor = image[sr][sc]
        while queue:
            r, c = queue.popleft()
            if image[r][c] == newColor:
                continue
            image[r][c] = newColor
            for row, col in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == oldColor:
                    queue.append([row, col])

        return image


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.floodFill(image = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], sr = 1, sc = 2, newColor = 2),[[2, 2, 2, 0], [0, 2, 2, 2], [1, 0, 2, 2]])

    def testcase2(self):
        self.assertEqual(self.solution.floodFill(image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, newColor = 2),[[2, 2, 2], [2, 2, 0], [2, 0, 1]])

    def testcase3(self):
        self.assertEqual(self.solution.floodFill(image = [[0, 1, 0], [0, 1, 0]], sr = 0, sc = 1, newColor = 0),[[0, 0, 0], [0, 0, 0]])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()