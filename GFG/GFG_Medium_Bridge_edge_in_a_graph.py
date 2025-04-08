# https://www.geeksforgeeks.org/problems/bridge-edge-in-graph/1
class Solution:
    def isBridge(self, V, edges, c, d):
        # code here
        adj = {i: [] for i in range(V)}
        for u, v in edges:
            if (u == c and v == d) or (u == d and v == c):
                pass
            else:
                adj[u].append(v)
                adj[v].append(u)

        visited = [False for _ in range(V)]

        def dfs(node, target):
            if node == target:
                return True
            elif not visited[node]:
                visited[node] = True
                flag = False
                for nxt in adj[node]:
                    flag = flag or dfs(nxt, target)
                return flag
            else:
                return False

        return not dfs(c, d)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.isBridge(4, [[0,1],[1,2],[2,3]],1,2))

    def testcase2(self):
        self.assertFalse(self.solution.isBridge(5, [[0,1],[1,2],[2,0],[0,3],[3,4]],0,2))

    def testcase3(self):
        self.assertFalse(self.solution.isBridge(5, [[0,1],[1,2],[2,0],[0,3],[3,4]],1,2))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()