# https://www.geeksforgeeks.org/problems/word-break1352/1

class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        n = len(s)
        dp = [-1] * n
        words = {}
        for word in dictionary:
            if word[0] in words:
                words[word[0]].append(word)
            else:
                words[word[0]] = [word]

        def helper(i, n):
            if i == n:
                return True
            elif s[i] not in words:
                return False
            elif dp[i] == -1:
                flag, letter = False, s[i]
                for word in words[letter]:
                    if len(word) <= n - i and s[i:i + len(word)] == word:
                        flag = flag or helper(i + len(word), n)
                dp[i] = flag
            return dp[i]

        return helper(0, len(s))

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.wordBreak(s = "ilike", dictionary = ["i", "like", "gfg"]))

    def testcase2(self):
        self.assertTrue(self.solution.wordBreak(s = "ilike", dictionary = ["i", "like", "gfg"]))

    def testcase3(self):
        self.assertFalse(self.solution.wordBreak(s = "ilikemangoes", dictionary = ["i", "like", "man", "india", "gfg"]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
