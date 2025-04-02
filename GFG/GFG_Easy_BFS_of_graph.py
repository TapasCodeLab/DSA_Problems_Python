# User function Template for python3
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        from collections import deque
        visited = set()
        queue = deque([0])
        res = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                res.append(node)
                visited.add(node)
                for x in adj[node]:
                    queue.append(x)

        return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.bfs( [[2, 3, 1], [0], [0, 4], [0], [2]]),[0, 2, 3, 1, 4])

    def testcase2(self):
        self.assertEqual(self.solution.bfs( [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]),[0, 1, 2, 3, 4])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
