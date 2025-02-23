# https://www.geeksforgeeks.org/problems/longest-valid-parentheses5657/1

class Solution:
    def maxLength(self, s):
        # code here
        stack = []
        res = 0
        for ind, ch in enumerate(s):
            if ch == '(':
                stack.append(['(', ind])
            elif ch == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                    if not stack:
                        res = max(res, ind + 1)
                    else:
                        res = max(res, ind - stack[-1][1])
                else:
                    stack.append([')', ind])

        return res

# Test

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.maxLength("((()"),2)

    def test_testcase2(self):
        self.assertEqual(self.solution.maxLength(")()())"),4)

    def test_testcase3(self):
        self.assertEqual(self.solution.maxLength("())()"),2)

    def test_testcase4(self):
        self.assertEqual(self.solution.maxLength("(()()()())"),10)

    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()



