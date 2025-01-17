from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        temp = 0
        for n in derived:
            temp ^= n

        return temp == 0


if __name__ == '__main__':
    s = Solution()
    print(s.doesValidArrayExist([1,1,0])==True)
    print(s.doesValidArrayExist([1,1]) == True)
    print(s.doesValidArrayExist([1,0])==False)
    print(s.doesValidArrayExist([1,1,0,1,1,0,1,0,1,0]) == True)
    print(s.doesValidArrayExist([0,0])==True)
    print(s.doesValidArrayExist([0,1,0,1,0,1,0,1,0,1,0]) == False)