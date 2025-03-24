from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        start, end = meetings[0]
        res = start - 1
        for meeting in meetings[1:]:
            if meeting[0] > end:
                res += meeting[0] - 1 - end
            end = max(end, meeting[1])

        if days > end:
            res += days - end

        return res

        # Below code works but gives MLE as days <= 10^9
        # prefix_sum = [0]*days
        # for start, end in meetings:
        #     prefix_sum[start-1] += 1
        #     if end<days:
        #         prefix_sum[end] -= 1

        # res = 0
        # prefix = 0
        # for x in prefix_sum:
        #     prefix += x
        #     if prefix == 0:
        #         res += 1

        # return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_Solution_1(self):
        self.assertEqual(self.solution.countDays(10, [[5,7],[1,3],[9,10]]),2)

    def test_Solution_2(self):
        self.assertEqual(self.solution.countDays(5, [[2,4],[1,3]]), 1)

    def test_Solution_3(self):
        self.assertEqual(self.solution.countDays(6, [[1,6]]), 0)

    def test_Solution_4(self):
        self.assertEqual(self.solution.countDays(1000000000, [[1,1000000000]]), 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()