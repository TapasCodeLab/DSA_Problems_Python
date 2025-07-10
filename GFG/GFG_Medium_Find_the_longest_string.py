# https://www.geeksforgeeks.org/problems/find-the-longest-string--170645/1

class Solution():
    def longestString(self, arr):
        # code here
        arr.sort(key=lambda x: (len(x), tuple(-ord(ch) for ch in x)))
        set_arr = set(arr)
        set_arr.add('')
        for i in range(len(arr)-1,-1,-1):
            word = arr[i]
            for j in range(len(word)):
                if word[:j] not in set_arr:
                    break
            else:
                return word

        return arr[0] if len(arr[0])==1 else ''

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.longestString(["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]),"pros")

    def testcase2(self):
        self.assertEqual(self.solution.longestString(["a", "bb", "ccc", "bbbb", "ddd", "dd", "e", "f"]),"a")

    def testcase3(self):
        self.assertEqual(self.solution.longestString(["a", "aa", "aaa", "aaaa", "b", "bb", "bbb", "bbbb"]),"aaaa")

    def testcase4(self):
        self.assertEqual(self.solution.longestString(["ab", "a", "abc", "abd"]),"abc")

    def testcase5(self):
        self.assertEqual(self.solution.longestString(["ab", "aa", "abc", "abd"]),"")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
