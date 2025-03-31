# https://www.geeksforgeeks.org/problems/maximize-partitions-in-a-string/1
class Solution:
    def maxPartitions(self , s):
        # code here
        from collections import Counter
        total_freq = Counter(s)
        res = 0
        freq = {}
        for index,letter in enumerate(s):
            freq[letter] = freq.get(letter,0)+1
            if freq[letter] == total_freq[letter]:
                del freq[letter]
            if len(freq)==0:
                res += 1
        return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maxPartitions("acbbcc"),2)

    def testcase2(self):
        self.assertEqual(self.solution.maxPartitions("ababcbacadefegdehijhklij"),3)

    def testcase3(self):
        self.assertEqual(self.solution.maxPartitions("aaa"),1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()