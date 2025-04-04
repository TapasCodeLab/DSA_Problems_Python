# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
class Solution:
    def isCycle(self, V, edges):
        # Code here
        adj = {i: [] for i in range(V)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return True
            else:
                visited.add(node)
                flag = False
                for nxt in adj[node]:
                    if nxt != parent:
                        flag = flag or dfs(nxt, node)
                return flag

        return dfs(0, -1)


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.isCycle(V = 4, edges = [[0, 1], [0, 2], [1, 2], [2, 3]]))

    def testcase2(self):
        self.assertFalse(self.solution.isCycle(V = 4, edges = [[0, 1], [1, 2], [2, 3]]))


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
