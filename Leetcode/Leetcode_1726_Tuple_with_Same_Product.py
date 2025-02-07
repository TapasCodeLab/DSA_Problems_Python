from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from math import factorial

        def ncr(n, r):
            return factorial(n)//(factorial(r)*factorial(n-r))

        d = {}
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x = nums[i]*nums[j]
                d[x] = d.get(x,0)+1

        for key, val in d.items():
            if val>=2:
                res += ncr(val, 2)*8

        return res