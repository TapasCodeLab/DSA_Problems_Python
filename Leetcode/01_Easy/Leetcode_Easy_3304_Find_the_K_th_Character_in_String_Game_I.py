class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        count = 0
        while True:
            first = 0
            ans = []
            while first < len(word):
                ch = chr(ord('a') + ((ord(word[first]) - ord('a') + 1) % 26))
                ans.append(ch)
                first += 1
                count += 1
            word.extend(ans)
            if count >= k:
                return word[k - 1]

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.kthCharacter(1),'a')

    def testcase2(self):
        self.assertEqual(self.solution.kthCharacter(5),'b')

    def testcase3(self):
        self.assertEqual(self.solution.kthCharacter(10),'c')

    def testcase4(self):
        self.assertEqual(self.solution.kthCharacter(439),'g')

    def testcase5(self):
        self.assertEqual(self.solution.kthCharacter(500),'h')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()