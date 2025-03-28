# https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

class Solution:
    def activitySelection(self, start, finish):
        # code here
        activity = [[start[i], finish[i]] for i in range(len(start))]
        activity.sort(key=lambda x: x[1])
        res = 0
        end = 0
        for act in activity:
            if act[0] > end:
                res += 1
                end = act[1]

        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.activitySelection(start = [1, 3, 0, 5, 8, 5], finish = [2, 4, 6, 7, 9, 9]),4)

    def testcase2(self):
        self.assertEqual(self.solution.activitySelection(start = [10, 12, 20], finish = [20, 25, 30]), 1)

    def testcase3(self):
        self.assertEqual(self.solution.activitySelection(start = [1, 3, 2, 5], finish = [2, 4, 3, 6]), 3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()