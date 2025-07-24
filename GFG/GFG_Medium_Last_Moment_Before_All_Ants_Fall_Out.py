# https://www.geeksforgeeks.org/problems/last-moment-before-all-ants-fall-out-of-a-plank/1

class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        result = 0
        for l in left:
            result = max(result, l)

        for r in right:
            result = max(result, n - r)

        return result


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.getLastMoment(n = 4, left = [2], right = [0, 1, 3]),4)

    def testcase2(self):
        self.assertEqual(self.solution.getLastMoment(n = 4, left = [], right = [0, 1, 2, 3, 4]),4)

    def testcase3(self):
        self.assertEqual(self.solution.getLastMoment(n = 3, left = [0], right = [3]),0)

    def testcase4(self):
        self.assertEqual(self.solution.getLastMoment(n = 3, left = [4, 3,7, 9], right = [1, 2, 5, 6, 8]),9)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
