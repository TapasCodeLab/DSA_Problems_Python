from typing import List
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq
        events.sort(key=lambda x: (x[0], x[1]), reverse=True)
        max_day = max([end for start, end in events])
        result, day = 0, 0
        min_heap = []
        while day <= max_day:
            while events and events[-1][0] <= day:
                start, end = events.pop()
                heapq.heappush(min_heap, end)
            if min_heap and day <= min_heap[0]:
                heapq.heappop(min_heap)
                result += 1
                day += 1
            elif min_heap:
                heapq.heappop(min_heap)
            else:
                day += 1

        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.maxEvents([[1,2],[2,3],[3,4]]),3)

    def test_testcase2(self):
        self.assertEqual(self.solution.maxEvents([[1,2],[2,3],[3,4],[1,2]]),4)

    def test_testcase3(self):
        self.assertEqual(self.solution.maxEvents([[1,2],[2,3],[3,4],[1,2],[1,2]]),4)

    def test_testcase4(self):
        self.assertEqual(self.solution.maxEvents([[1,2],[2,3],[3,4],[1,2],[1,2],[1,2],[1,2],[1,2],[1,9]]),5)

    def test_testcase5(self):
        self.assertEqual(self.solution.maxEvents([[1,5],[2,3],[2,3],[1,5],[1,5]]),5)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()