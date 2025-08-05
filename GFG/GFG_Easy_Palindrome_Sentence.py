# https://www.geeksforgeeks.org/problems/string-palindromic-ignoring-spaces4723/1

class Solution:
    def isPalinSent(self, s):
        # code here
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

        if start < end and s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1

        return True


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.isPalinSent("Too hot to hoot"))

    def testcase2(self):
        self.assertTrue(self.solution.isPalinSent("Abc 012..## 10cbA"))

    def testcase3(self):
        self.assertFalse(self.solution.isPalinSent("ABC $. def01ASDF"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()