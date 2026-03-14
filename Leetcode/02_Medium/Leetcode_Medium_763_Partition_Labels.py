from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import Counter
        total_freq = Counter(s)
        start, res = 0, []
        freq = {}
        for index,letter in enumerate(s):
            freq[letter] = freq.get(letter,0)+1
            if freq[letter] == total_freq[letter]:
                del freq[letter]
            if len(freq)==0:
                res.append(index-start+1)
                start = index+1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.partitionLabels("ababcbacadefegdehijhklij"),[9,7,8])

    def testcase2(self):
        self.assertEqual(self.solution.partitionLabels("eccbbbbdec"),[10])

    def testcase3(self):
        self.assertEqual(self.solution.partitionLabels("ababababcddeefe"),[8,1,2,4])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()