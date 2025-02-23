from typing import List
from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        indegree = [0] * (k + 1)
        adj_row = {i: [] for i in range(1, k + 1)}
        for above, below in rowConditions:
            indegree[below] += 1
            adj_row[above].append(below)

        rows, r = {}, 0
        queue = deque([])
        for i in range(1, k + 1):
            if indegree[i] == 0:
                rows[i] = r
                r += 1
                queue.append(i)
        while queue:
            i = queue.popleft()
            for nxt in adj_row[i]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    rows[nxt] = r
                    r += 1
                    queue.append(nxt)

        # print(rows)
        if len(rows) != k:
            return []

        indegree = [0] * (k + 1)
        adj_col = {i: [] for i in range(1, k + 1)}
        for left, right in colConditions:
            indegree[right] += 1
            adj_col[left].append(right)

        cols, c = {}, 0
        queue = deque([])
        for i in range(1, k + 1):
            if indegree[i] == 0:
                cols[i] = c
                c += 1
                queue.append(i)
        while queue:
            i = queue.popleft()
            for nxt in adj_col[i]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    cols[nxt] = c
                    c += 1
                    queue.append(nxt)

        # print(cols)
        if len(cols) != k:
            return []

        res = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(1, k + 1):
            res[rows[i]][cols[i]] = i

        return res

# Test cases
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertIn(self.solution.buildMatrix(3, [[1,2],[3,2]],[[2,1],[3,2]]),[[[0,0,1],[3,0,0],[0,2,0]],[[3,0,0],[0,0,1],[0,2,0]]])

    def test_testcase2(self):
        self.assertEqual(self.solution.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]),[])


    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()




