# https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1
import heapq

class Solution:
    def getMedian(self, arr):
        maxheap, minheap = [-arr[0]], []
        res = [arr[0]]

        for a in arr[1:]:
            if a < -maxheap[0]:
                heapq.heappush(maxheap, -a)
            else:
                heapq.heappush(minheap, a)

            if len(maxheap) < len(minheap):
                heapq.heappush(maxheap, -heapq.heappop(minheap))
            elif (len(maxheap) - len(minheap)) > 1:
                heapq.heappush(minheap, -heapq.heappop(maxheap))

            if len(maxheap) == len(minheap):
                res.append((-maxheap[0] + minheap[0]) / 2)
            else:
                res.append(-maxheap[0])

        return res


# {
# Driver Code Starts
# Initial Template for Python 3


# def main():
#     t = 1 # int(input().strip())
#     for _ in range(t):
#         s = input("Enter the stream of numbers: ").strip()
#         nums = list(map(int, s.split()))
#         ob = Solution()
#         ans = ob.getMedian(nums)
#         print(" ".join(f"{x:.1f}" for x in ans))

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_solution1(self):
        self.assertEqual([4.0, 3.5, 3.0, 3.5, 4.0, 13.0, 22.0, 14.0, 15.0, 10.5, 6.0],self.solution.getMedian([4, 3, 1, 29, 24, 22, 22, 6, 15, 2, 1]))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

# } Driver Code Ends