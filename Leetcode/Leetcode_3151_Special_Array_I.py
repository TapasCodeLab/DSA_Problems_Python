from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i]%2 + nums[i+1]%2 != 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isArraySpecial([1])==True)
    print(s.isArraySpecial([2,1,4]) == True)
    print(s.isArraySpecial([4,3,1,6]) == False)