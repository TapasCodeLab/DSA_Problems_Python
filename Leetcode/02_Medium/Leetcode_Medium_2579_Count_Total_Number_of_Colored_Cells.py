class Solution:
    def coloredCells(self, n: int) -> int:
        import sys
        sys.setrecursionlimit(10 ** 6)
        if n == 1:
            return 1
        else:
            return 4 + (n - 2) * 4 + self.coloredCells(n - 1)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.coloredCells(1),1)

    def testcase2(self):
        self.assertEqual(self.solution.coloredCells(2), 5)

    def testcase3(self):
        self.assertEqual(self.solution.coloredCells(3),13)

    def testcase4(self):
        self.assertEqual(self.solution.coloredCells(5),41)

    def testcase5(self):
        self.assertEqual(self.solution.coloredCells(15),421)

    def testcase6(self):
        self.assertEqual(self.solution.coloredCells(95555),18261324941)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()