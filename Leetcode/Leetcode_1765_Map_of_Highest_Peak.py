from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        lenr, lenc = len(isWater), len(isWater[0])
        res = [[-1 for _ in range(lenc)] for _ in range(lenr)]
        queue = deque([])
        level = 0
        for r in range(lenr):
            for c in range(lenc):
                if isWater[r][c] == 1:
                    queue.append([r,c])

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if res[r][c] == -1:
                    res[r][c] = level
                    if 0<=r+1<lenr:
                        queue.append([r+1,c])
                    if 0<=r-1<lenr:
                        queue.append([r-1,c])
                    if 0<=c+1<lenc:
                        queue.append([r, c+1])
                    if 0<=c-1<lenc:
                        queue.append([r,c-1])
            level += 1

        return res



if __name__ == '__main__':
    s = Solution()
    print(s.highestPeak([[0,1],[0,0]]) == [[1,0],[2,1]])
    print(s.highestPeak([[0,0,1],[1,0,0],[0,0,0]]) == [[1,1,0],[0,1,1],[1,2,2]])
    print(s.highestPeak([[0,0,0],[0,1,0],[0,0,0]]) == [[2,1,2],[1,0,1],[2,1,2]])
    print(s.highestPeak([[1,1,1],[1,1,1],[1,1,1]]) == [[0,0,0],[0,0,0],[0,0,0]])

