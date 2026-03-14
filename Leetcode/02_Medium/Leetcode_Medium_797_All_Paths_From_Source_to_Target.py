from typing import List
import unittest

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.all_paths = []
        self.target = len(graph)-1

        def dfs(current_path, visited):
            current_node = current_path[-1]
            if current_node == self.target:
                self.all_paths.append(current_path[:])
                return
            else:
                for nxt in graph[current_node]:
                    if nxt not in visited:
                        visited.add(nxt)
                        current_path.append(nxt)
                        dfs(current_path, visited)
                        visited.remove(nxt)
                        current_path.pop()

        dfs([0],set([0]))  #Source is 0
        return self.all_paths



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        graph = [[1, 2], [3], [3], []]
        self.assertListEqual(self.solution.allPathsSourceTarget(graph), [[0, 1, 3], [0, 2, 3]])

    def testcase2(self):
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        self.assertListEqual(self.solution.allPathsSourceTarget(graph), [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])

    def testcase3(self):
        graph = [[], []]
        self.assertListEqual(self.solution.allPathsSourceTarget(graph), [])

    def tearDown(self):
        pass