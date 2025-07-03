# https://www.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1

class Solution:
    def substrCount(self, s, k):
        # code here
        freq = {}
        for i in range(k):
            freq[s[i]] = freq.get(s[i], 0) + 1

        res = 1 if len(freq) == k - 1 else 0

        for i in range(k, len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[s[i - k]] = freq.get(s[i - k]) - 1
            if freq[s[i - k]] == 0:
                del freq[s[i - k]]

            res += 1 if len(freq) == k - 1 else 0

        return res


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.substrCount(s = "abcc", k = 2),1)

    def testcase2(self):
        self.assertEqual(self.solution.substrCount("aabab", k = 3),3)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()