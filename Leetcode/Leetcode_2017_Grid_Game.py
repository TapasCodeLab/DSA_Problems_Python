from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pref = [[0 for _ in range(n)] for _ in range(2)]
        total = 0
        for c in range(n-1,-1,-1):
            pref[0][c] = grid[0][c]+total
            total += grid[0][c]

        total = 0
        for c in range(n):
            pref[1][c] = grid[1][c]+total
            total += grid[1][c]

        res = float('inf')
        prev = 0
        for i in range(n-1):
            mx = max(prev,pref[0][i+1])
            res = min(res,mx)
            prev = pref[1][i]

        res = min(res,pref[1][n-2])

        return res if n>1 else 0


# Failed for testcase - [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]

if __name__ == '__main__':
    s = Solution()
    print(s.gridGame([[2,5,4],[1,5,1]]) == 4)
    print(s.gridGame([[3,3,1],[8,5,2]]) == 4)
    print(s.gridGame([[1,3,1,15],[1,3,3,1]]) == 7)
    print(s.gridGame([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]) == 63)


