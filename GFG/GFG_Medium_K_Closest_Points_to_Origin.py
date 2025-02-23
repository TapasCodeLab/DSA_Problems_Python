# https://www.geeksforgeeks.org/problems/k-closest-points-to-origin--172242/1

from typing import List

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        maxheap = []
        size = 0

        for x, y in points:
            heapq.heappush(maxheap, [-(x * x + y * y), x, y])
            if size == k:
                heapq.heappop(maxheap)
            else:
                size += 1

        return [[x, y] for d, x, y in maxheap]

# Test

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.kClosest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2),[[-2, 2], [0, 1]])

    def test_testcase2(self):
        self.assertEqual(self.solution.kClosest([[2, 4], [-1, -1], [0, 0]], 1),[[0, 0]])


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
