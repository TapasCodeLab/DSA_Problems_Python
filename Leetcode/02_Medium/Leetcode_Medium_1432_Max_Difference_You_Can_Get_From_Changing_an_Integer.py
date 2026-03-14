class Solution:
    def maxDiff(self, num: int) -> int:
        prev, curr = 9, 9
        for n in str(num):
            if int(n) < 9:
                prev = int(n)
                break

        _max = 0
        for n in str(num):
            if int(n) == prev:
                _max = _max * 10 + curr
            else:
                _max = _max * 10 + int(n)

        if int(str(num)[0]) == 1:
            prev, curr = 0, 0
            for n in str(num):
                if int(n) > 1:
                    prev = int(n)
                    break
        else:
            prev, curr = int(str(num)[0]), 1

        _min = 0
        for n in str(num):
            if int(n) == prev:
                _min = _min * 10 + curr
            else:
                _min = _min * 10 + int(n)

        return _max - _min

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maxDiff(555),888)

    def testcase2(self):
        self.assertEqual(self.solution.maxDiff(9),8)

    def testcase3(self):
        self.assertEqual(self.solution.maxDiff(123),820)

    def testcase4(self):
        self.assertEqual(self.solution.maxDiff(921),870)

    def testcase5(self):
        self.assertEqual(self.solution.maxDiff(11445),88440)

    def tearDown(self):
        pass