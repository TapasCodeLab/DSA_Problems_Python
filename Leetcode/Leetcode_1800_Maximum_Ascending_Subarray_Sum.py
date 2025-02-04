from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, total, prev = 0, 0, 0
        for n in nums:
            if n > prev:
                total += n
            else:
                total = n
            prev = n
            res = max(total, res)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65)
    print(s.maxAscendingSum([10,20,30,40,50]) == 150)
    print(s.maxAscendingSum([12,17,15,13,10,11,12]) == 33)
