from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        lenr, lenc = len(grid), len(grid[0])
        row, col, total = {}, {}, 0
        for r in range(lenr):
            for c in range(lenc):
                if grid[r][c] == 1:
                    if r in row or c in col:
                        total += 1
                        grid[r][c] = 0
                        if r in row:
                            x, y = row[r]
                            if grid[x][y] == 1:
                                total += 1
                                grid[x][y] = 0
                        else:
                            row[r] = [r, c]
                        if c in col:
                            x, y = col[c]
                            if grid[x][y] == 1:
                                total += 1
                                grid[x][y] = 0
                        else:
                            col[c] = [r, c]
                    else:
                        row[r] = [r, c]
                        col[c] = [r, c]
        return total


if __name__ == '__main__':
    s = Solution()
    print(s.countServers([[1,0],[0,1]]) == 0)
    print(s.countServers([[1,0],[1,1]]) == 3)
    print(s.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4)
    print(s.countServers([[1,1,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]) == 3)
    print(s.countServers([[0,0,1,0],[0,0,0,0],[0,0,0,0],[1,0,1,0]]) == 3)