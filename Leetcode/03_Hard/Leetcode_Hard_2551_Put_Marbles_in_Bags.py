from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        import heapq
        minHeap, maxHeap = [], []
        for i in range(len(weights)-1):
            heapq.heappush(minHeap, weights[i]+weights[i+1])
            heapq.heappush(maxHeap, -(weights[i]+weights[i+1]))

        #minScore breaking points which will give least score, maxScore is opposite
        # Both will have two end points
        minScore, maxScore = weights[0]+weights[-1], weights[0]+weights[-1]
        for _ in range(k-1):
            x = heapq.heappop(minHeap)
            y = -heapq.heappop(maxHeap)
            minScore += x
            maxScore += y

        return maxScore-minScore


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.putMarbles(weights = [1,3,5,1], k = 2),4)

    def testcase2(self):
        self.assertEqual(self.solution.putMarbles(weights = [1, 3], k = 2),0)

    def testcase3(self):
        self.assertEqual(self.solution.putMarbles(weights = [1,3,5,1,4,5,2,3,5,3,2,1,8,9,5,8,4,6,3,6,2,1], k = 5),41)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()