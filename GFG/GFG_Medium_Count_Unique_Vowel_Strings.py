# https://www.geeksforgeeks.org/problems/count-unique-vowel-strings/1

class Solution:
    def vowelCount(self, s):
        # code here
        vowels = 'aeiou'
        freq = {}
        for ch in s:
            if ch in vowels:
                freq[ch] = freq.get(ch, 0) + 1

        if not freq:
            return 0
        else:
            res = 1
            for i in range(2, len(freq) + 1):
                res *= i

            for val in freq.values():
                res *= val

            return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.vowelCount("aeiou"), 120)

    def testcase2(self):
        self.assertEqual(self.solution.vowelCount("ae"), 2)

    def testcase3(self):
        self.assertEqual(self.solution.vowelCount("aacidf"), 4)

    def testcase4(self):
        self.assertEqual(self.solution.vowelCount("bcd"), 0)

    def testcase5(self):
        self.assertEqual(self.solution.vowelCount("aaaabbeeebsbi"), 72)

    def testcase6(self):
        self.assertEqual(self.solution.vowelCount("aeiouxaskmlkasodkjbacbncbnmvbzxaallaaraaauuiiioooeee"), 316800)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()