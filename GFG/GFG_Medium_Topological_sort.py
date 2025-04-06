# https://www.geeksforgeeks.org/problems/topological-sort/1

class Solution:
    def topoSort(self, V, edges):
        # Code here
        from collections import deque
        indegree = [0] * V
        adj = {i: [] for i in range(V)}
        for u, v in edges:
            indegree[v] += 1
            adj[u].append(v)

        queue = deque([])
        res = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.append(node)
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertIn(self.solution.topoSort(V = 4, edges = [[3, 0], [1, 0], [2, 0]]), [[3, 2, 1, 0],[1, 2, 3, 0],[2, 3, 1, 0]])

    def testcase2(self):
        self.assertIn(self.solution.topoSort(V = 6, edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]),
                      [[4, 5, 1, 0, 2, 3],[4, 5, 0, 1, 2, 3],[5, 2, 4, 0, 1, 3]]) # not complete list

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()