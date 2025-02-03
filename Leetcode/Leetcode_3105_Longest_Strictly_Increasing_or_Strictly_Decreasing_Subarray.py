from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        inc_count, dec_count = 1, 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                inc_count += 1
                res = max(res, inc_count)
            else:
                inc_count = 1
            if nums[i + 1] < nums[i]:
                dec_count += 1
                res = max(res, dec_count)
            else:
                dec_count = 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestMonotonicSubarray([1,4,3,3,2])==2)
    print(s.longestMonotonicSubarray([3,3,3,3])==1)
    print(s.longestMonotonicSubarray([3,2,1])==3)