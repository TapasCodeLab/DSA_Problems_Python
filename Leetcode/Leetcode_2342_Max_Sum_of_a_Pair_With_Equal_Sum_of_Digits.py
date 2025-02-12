from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumDigits(n):
            total = 0
            while n:
                total += n % 10
                n = n // 10
            return total

        freq = {}
        for n in nums:
            x = sumDigits(n)
            if x not in freq:
                freq[x] = [n]
            else:
                freq[x].append(n)
                freq[x].sort(reverse=True)
                freq[x] = freq[x][:2]

        ans = 0
        for val in freq.values():
            if len(val) == 2:
                ans = max(ans, val[0] + val[1])

        return -1 if ans == 0 else ans
