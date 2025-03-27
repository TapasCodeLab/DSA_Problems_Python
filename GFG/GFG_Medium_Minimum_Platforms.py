# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        # code here
        train = []
        for a in arr:
            train.append([a, 1])
        for d in dep:
            train.append([d, -1])

        res, total = 0, 0
        train.sort(key=lambda x: x[0])
        for t in train:
            total += t[1]
            res = max(res, total)

        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minimumPlatform(arr = [900, 940, 950, 1100, 1500, 1800], dep = [910, 1200, 1120, 1130, 1900, 2000]),3)

    def testcase2(self):
        self.assertEqual(self.solution.minimumPlatform(arr = [900, 1235, 1100], dep = [1000, 1240, 1200]), 1)

    def testcase3(self):
        self.assertEqual(self.solution.minimumPlatform(arr= [1000, 935, 1100], dep = [1200, 1240, 1130]), 3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()