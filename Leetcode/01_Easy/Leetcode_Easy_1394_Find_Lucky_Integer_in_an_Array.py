from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        frequency = Counter(arr)
        answer = -1
        for key, val in sorted(frequency.items()):
            if key==val:
                answer= key

        return answer

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.findLucky([2,2,3,4]),2)

    def testcase1(self):
        self.assertEqual(self.solution.findLucky([1,2,2,3,3,3]),3)

    def testcase1(self):
        self.assertEqual(self.solution.findLucky([2,2,2,3,3]),-1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()