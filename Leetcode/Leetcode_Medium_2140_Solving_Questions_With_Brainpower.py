from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*n
        for i in range (n-1,-1,-1):
            x = 0 if questions[i][1]+i+1 >=n else dp[questions[i][1]+i+1]
            y = 0 if i+1 >=n else dp[i+1]
            dp[i] = max(y, questions[i][0]+x)
        #print(dp)
        return dp[0]

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.mostPoints([[3,2],[4,3],[4,4],[2,5]]),5)

    def testcase2(self):
        self.assertEqual(self.solution.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]),7)

    def testcase3(self):
        self.assertEqual(self.solution.mostPoints([[3,2],[4,3],[4,4],[2,5],[2,4],[5,7],[2,1],[100,3],[101,2],[11,1]]),107)

    def testcase4(self):
        self.assertEqual(self.solution.mostPoints([[3,2]]),3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()