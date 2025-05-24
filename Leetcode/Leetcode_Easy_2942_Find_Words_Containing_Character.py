from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = [i for i in range(len(words)) if x in words[i]]
        return res


import unittest

class TestClass(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.findWordsContaining(["leet","code"],'e'),[0,1])

    def testcase2(self):
        self.assertEqual(self.solution.findWordsContaining(["abc","bcd","aaaa","cbc"], 'a'),[0,2])

    def testcase3(self):
        self.assertEqual(self.solution.findWordsContaining(["abc","bcd","aaaa","cbc"], 'z'),[])

    def tearDown(self):
        pass