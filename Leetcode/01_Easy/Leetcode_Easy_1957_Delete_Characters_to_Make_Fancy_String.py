class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_char, count = '', 0
        res = []
        for ch in s:
            if ch == prev_char and count == 2:
                continue
            elif ch != prev_char:
                count = 1
            else:
                count += 1
            res.append(ch)
            prev_char = ch

        return ''.join(res)


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.makeFancyString("leeetcode"),"leetcode")

    def testcase2(self):
        self.assertEqual(self.solution.makeFancyString("aaabaaaa"),"aabaa")

    def testcase3(self):
        self.assertEqual(self.solution.makeFancyString("aab"),"aab")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
