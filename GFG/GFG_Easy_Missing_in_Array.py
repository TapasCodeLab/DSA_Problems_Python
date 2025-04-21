class Solution:
    def missingNum(self, arr):
        # code here
        from functools import reduce
        n = len(arr) + 2
        res = reduce(lambda a, b: a ^ b, arr)
        for i in range(1, n):
            res = res ^ i

        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.missingNum([1, 2, 3, 5]),4)

    def testcase2(self):
        self.assertEqual(self.solution.missingNum([8, 2, 4, 5, 3, 7, 1]),6)

    def testcase3(self):
        self.assertEqual(self.solution.missingNum([1]),2)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()