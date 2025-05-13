class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        import heapq
        dist = [float('inf')] * V
        heap = []
        adj = {i: [] for i in range(V)}
        for u, v, wgt in edges:
            adj[u].append([v, wgt])
            adj[v].append([u, wgt])

        dist[src] = 0
        heapq.heappush(heap, [0, src])
        while heap:
            wgt, tgt = heapq.heappop(heap)
            if wgt > dist[tgt]:
                continue
            for nxt, wgt in adj[tgt]:
                if dist[tgt] + wgt < dist[nxt]:
                    dist[nxt] = dist[tgt] + wgt
                    heapq.heappush(heap, [dist[nxt], nxt])

        return dist



def test(V, E, input_edges, src):
    edges = []
    for edge in input_edges:
        u, v, w = edge
        edges.append([u, v, w])
        edges.append([v, u, w])  # Since the graph is undirected

    obj = Solution()
    res = obj.dijkstra(V, edges, src)
    return res


# if __name__ == "__main__":
#     test(3, 3, [[0, 1, 1], [1, 2, 3], [0, 2, 6]], 2)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(test(3, 3, [[0, 1, 1], [1, 2, 3], [0, 2, 6]], 2),[4, 3, 0])

    def testcase2(self):
        self.assertEqual(test(5, 5, [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], 0), [0, 4, 8, 10, 10])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()