from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        prefix_time, prefix_duration, total = [], [], 0
        for i in range(len(startTime)):
            prefix_time.append(endTime[i])
            total += endTime[i]-startTime[i]
            prefix_duration.append(total)
        prefix_time.append(eventTime)
        prefix_duration.append(total)

        # print(prefix_time)
        # print(prefix_duration)

        total, duration = prefix_time[k], prefix_duration[k]
        result = total - duration
        for i in range(k+1, len(prefix_time)):
            total, duration = prefix_time[i]-prefix_time[i-k-1], prefix_duration[i]-prefix_duration[i-k-1]
            result = max(result,total - duration)

        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]),2)

    def test_testcase2(self):
        self.assertEqual(self.solution.maxFreeTime(eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]),6)

    def test_testcase3(self):
        self.assertEqual(self.solution.maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]),0)

    def test_testcase4(self):
        self.assertEqual(self.solution.maxFreeTime(eventTime = 15, k = 2, startTime = [1,3,5,7], endTime = [2,5,6,9]),7)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()