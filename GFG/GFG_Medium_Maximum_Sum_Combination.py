# https://www.geeksforgeeks.org/problems/maximum-sum-combination/1

class Solution:
    def topKSumPairs(self, a, b, k):
        # code here
        import heapq
        a.sort(reverse=True)
        b.sort(reverse=True)
        visited = set([(0, 0)])
        i, j = 0, 0
        res, max_heap = [], []
        heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
        while k > 0:
            total, i, j = heapq.heappop(max_heap)
            res.append(-total)
            if i < len(a) - 1 and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
            if j < len(b) - 1 and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
            k -= 1

        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.topKSumPairs([3, 2], [1, 4], k = 2),[7, 6])

    def testcase2(self):
        self.assertEqual(self.solution.topKSumPairs([1, 4, 2, 3], [2, 5, 1, 6], k = 3),[10, 9, 9])

    def testcase3(self):
        self.assertEqual(self.solution.topKSumPairs([1, 4, 2, 3], [2, 5, 1, 6], k = 16),[10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2])

    def tearDown(self):
        pass
