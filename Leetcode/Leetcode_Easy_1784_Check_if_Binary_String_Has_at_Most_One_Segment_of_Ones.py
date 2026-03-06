import unittest

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag, prev = True, True  # without leading zeros
        for ch in s[1:]:
            if ch == '1':
                if not prev:
                    return False
            else:  # ch==0
                prev = False

        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertFalse(self.solution.checkOnesSegment("1001"))

    def testcase2(self):
        self.assertFalse(self.solution.checkOnesSegment("100100110"))

    def testcase3(self):
        self.assertTrue(self.solution.checkOnesSegment("110"))

    def testcase4(self):
        self.assertTrue(self.solution.checkOnesSegment("100000"))

    def testcase5(self):
        self.assertTrue(self.solution.checkOnesSegment("111111"))

    def tearDown(self):
        pass
