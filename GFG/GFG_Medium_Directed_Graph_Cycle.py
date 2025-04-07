# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

class Solution:
    def isCycle(self, V, edges):
        # code here
        adj = {i: [] for i in range(V)}
        for src, tgt in edges:
            adj[src].append(tgt)

        visited = [False] * V
        recStack = [False] * V

        def dfs(node):
            visited[node] = True
            recStack[node] = True

            for nxt in adj[node]:
                if not visited[nxt]:
                    if dfs(nxt):
                        return True
                elif recStack[nxt]:
                    return True

            recStack[node] = False
            return False

        for node in range(V):
            if not visited[node]:
                if dfs(node):
                    return True

        return False


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.isCycle(V = 4, edges = [[0, 1], [1, 2], [2, 3], [3, 3]]))

    def testcase1(self):
        self.assertFalse(self.solution.isCycle(V=3, edges=[[0, 1], [1, 2]]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()