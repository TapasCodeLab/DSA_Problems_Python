class Solution:
    def longestPalindrome(self, s):
        # code here
        res = ''
        for i in range(len(s)):
            count, left, right = 1, i, i
            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                count += 2
                left -= 1
                right += 1
            if count > len(res):
                res = s[left:right + 1]
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count, left, right = 2, i, i + 1
                while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                    count += 2
                    left -= 1
                    right += 1
                if count > len(res):
                    res = s[left:right + 1]

        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.longestPalindrome('forgeeksskeegfor'),'geeksskeeg')

    def testcase2(self):
        self.assertEqual(self.solution.longestPalindrome('Geeks'),'ee')

    def testcase3(self):
        self.assertEqual(self.solution.longestPalindrome('abc'),'a')

    def testcase4(self):
        self.assertEqual(self.solution.longestPalindrome('xabac'),'aba')

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
