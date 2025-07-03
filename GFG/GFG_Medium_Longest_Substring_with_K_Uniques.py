# https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

class Solution:
    def longestKSubstr(self, s, k):
        # code here
        start, end, result, frequency = 0, 0, -1, {}
        while end < len(s):
            frequency[s[end]] = frequency.get(s[end], 0) + 1
            while len(frequency) > k:
                frequency[s[start]] = frequency.get(s[start]) - 1
                if frequency[s[start]] == 0:
                    del frequency[s[start]]
                start += 1
            if len(frequency) == k:
                result = max(result, end - start + 1)
            end += 1

        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.longestKSubstr(s = "aabacbebebe", k = 3),7)

    def testcase2(self):
        self.assertEqual(self.solution.longestKSubstr(s = "aaaa", k = 2),-1)

    def testcase3(self):
        self.assertEqual(self.solution.longestKSubstr(s = "aabaaab", k = 2),7)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()