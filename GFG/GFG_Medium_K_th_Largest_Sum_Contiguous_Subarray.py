# https://www.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1
from typing import List

class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        import heapq
        minheap, size = [], 0
        for i in range(len(arr)):
            total = 0
            for j in range(i ,len(arr)):
                total += arr[j]
                heapq.heappush(minheap, total)
                size += 1
                if size >k:
                    heapq.heappop(minheap)
                    size -=1

        return heapq.heappop(minheap)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.kthLargest([3, 2, 1], 2),5)

    def testcase2(self):
        self.assertEqual(self.solution.kthLargest([2, 6, 4, 1], 3),11)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()