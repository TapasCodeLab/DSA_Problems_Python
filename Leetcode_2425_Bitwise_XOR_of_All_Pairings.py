from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        res = [0] * 32
        for n in nums1:
            for i in range(32):
                if ((n >> i) & 1) == 1:
                    res[31 - i] = (res[31 - i] + n2) % 2

        for n in nums2:
            for i in range(32):
                if ((n >> i) & 1) == 1:
                    res[31 - i] = (res[31 - i] + n1) % 2

        ans = 0
        for r in res:
            ans *= 2
            ans += r
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.xorAllNums([2,1,3],[10,2,5,0])==13)
    print(s.xorAllNums([1,2], [3,4]) == 0)

