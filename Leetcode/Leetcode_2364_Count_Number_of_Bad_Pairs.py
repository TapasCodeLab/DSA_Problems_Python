from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        for i, v in enumerate(nums):
            freq[v - i] = freq.get(v - i, 0) + 1

        total_pair = (len(nums) * (len(nums) - 1)) // 2
        good_pair = 0
        for k, v in freq.items():
            if v > 1:
                good_pair += (v * (v - 1)) // 2

        return total_pair - good_pair

