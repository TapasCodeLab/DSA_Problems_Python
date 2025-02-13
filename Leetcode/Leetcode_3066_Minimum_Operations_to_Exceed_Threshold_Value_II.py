import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap, ans = [], 0
        for n in nums:
            heapq.heappush(heap, n)

        while len(heap) >= 2:
            if heap[0] >= k:
                break
            ans += 1
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            heapq.heappush(heap, x * 2 + y)

        return ans
