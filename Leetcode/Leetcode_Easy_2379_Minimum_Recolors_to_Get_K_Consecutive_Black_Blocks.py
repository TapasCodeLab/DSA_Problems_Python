class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black = blocks[:k].count('B')
        max_black = black

        for i in range(k, len(blocks)):
            if blocks[i] == 'B':
                black += 1
            if blocks[i - k] == 'B':
                black -= 1
            max_black = max(max_black, black)

        return k - max_black

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minimumRecolors("WBBWWBBWBW",7),3)

    def testcase2(self):
        self.assertEqual(self.solution.minimumRecolors("WBWBBBW",2),0)

    def testcase3(self):
        self.assertEqual(self.solution.minimumRecolors("WWWWWWWWWWWW",7),7)

    def testcase4(self):
        self.assertEqual(self.solution.minimumRecolors("BBBBBBBBBBBB",7),0)

    def testcase5(self):
        self.assertEqual(self.solution.minimumRecolors("BWBWBWBWBWBWBWBW",7),3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

