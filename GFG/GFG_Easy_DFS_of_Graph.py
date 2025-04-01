# https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        visited = [False] * len(adj)
        res = []

        def rundfs(node):
            if visited[node]:
                return
            else:
                visited[node] = True
                res.append(node)
                for x in adj[node]:
                    rundfs(x)
                return

        rundfs(0)
        return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.dfs( [[2, 3, 1], [0], [0, 4], [0], [2]]),[0, 2, 4, 3, 1])

    def testcase2(self):
        self.assertEqual(self.solution.dfs( [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]),[0, 1, 2, 3, 4])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()