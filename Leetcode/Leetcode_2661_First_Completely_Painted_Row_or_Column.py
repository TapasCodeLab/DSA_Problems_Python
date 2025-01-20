from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        lenr, lenc = len(mat), len(mat[0])
        dr = {}
        dc = {}
        d = {}
        for r in range(lenr):
            for c in range(lenc):
                d[mat[r][c]] = (r,c)

        for i in range(len(arr)):
            r,c = d[arr[i]]
            dr[r] = dr.get(r,0)+1
            if dr[r] == lenc:
                return i
            dc[c] = dc.get(c,0)+1
            if dc[c] == lenr:
                return i




if __name__ == '__main__':
    s = Solution()
    print(s.firstCompleteIndex([1,4,5,2,6,3],[[4,3,5],[1,2,6]])==1)
    print(s.firstCompleteIndex([2,8,7,4,1,3,5,6,9],[[3,2,5],[1,4,6],[8,7,9]])==3)
    print(s.firstCompleteIndex([1,4,5,2,6,3],[[4,3,5],[1,2,6]])==1)