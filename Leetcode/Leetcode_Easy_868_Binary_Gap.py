import unittest

class Solution:
    def binaryGap(self, n: int) -> int:
        res, prev, bit_position = 0, -1, -1
        while n:
            bit_position +=1
            digit = n%2
            n = n//2
            if digit == 1:
                if prev !=-1:
                    res = max(res, bit_position-prev)
                prev = bit_position
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.binaryGap(22),2)

    def testcase2(self):
        self.assertEqual(self.solution.binaryGap(8),0)

    def testcase3(self):
        self.assertEqual(self.solution.binaryGap(5),2)

    def testcase4(self):
        self.assertEqual(self.solution.binaryGap(65),6)

    def testcase5(self):
        self.assertEqual(self.solution.binaryGap(128),0)

    def testcase6(self):
        self.assertEqual(self.solution.binaryGap(129),7)

    def testcase7(self):
        self.assertEqual(self.solution.binaryGap(0),0)

    def tearDown(self):
        pass



