import unittest

class Solution:
    def minOperations(self, s: str) -> int:
        def helper(s, flag):
            if s == '':
                return 0
            elif (flag == True and s[0] == '1') or (flag == False and s[0] == '0'):
                return helper(s[1:], not flag)
            else:
                return 1 + helper(s[1:], not flag)

        return min(helper(s, True), helper(s, False))

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minOperations("0100"),1)

    def testcase2(self):
        self.assertEqual(self.solution.minOperations("10"),0)

    def testcase3(self):
        self.assertEqual(self.solution.minOperations("1111"),2)

    def tearDown(self):
        pass
