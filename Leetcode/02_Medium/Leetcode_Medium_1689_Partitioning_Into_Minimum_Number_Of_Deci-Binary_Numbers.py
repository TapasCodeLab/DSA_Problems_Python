import unittest

class Solution:
    def minPartitions(self, n: str) -> int:
        result = max(int(x) for x in n)
        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minPartitions("32"),3)

    def testcase2(self):
        self.assertEqual(self.solution.minPartitions("82734"),8)

    def testcase3(self):
        self.assertEqual(self.solution.minPartitions("27346209830709182346"),9)

    def testcase4(self):
        self.assertEqual(self.solution.minPartitions("200"),2)

    def testcase5(self):
        self.assertEqual(self.solution.minPartitions("3209"),9)

    def testcase6(self):
        self.assertEqual(self.solution.minPartitions("100034"),4)

    def tearDown(self):
        pass