import unittest

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = 0 if n%2==1 else 1
        while n:
            last_digit = n%2
            n = n//2
            if last_digit == prev_bit:
                return False
            prev_bit = last_digit
        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.hasAlternatingBits(5))

    def testcase2(self):
        self.assertFalse(self.solution.hasAlternatingBits(7))

    def testcase3(self):
        self.assertFalse(self.solution.hasAlternatingBits(11))

    def testcase4(self):
        self.assertTrue(self.solution.hasAlternatingBits(10))

    def testcase5(self):
        self.assertTrue(self.solution.hasAlternatingBits(1))

    def testcase6(self):
        self.assertFalse(self.solution.hasAlternatingBits(2147483647))

    def tearDown(self):
        pass