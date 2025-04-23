#https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1
class Solution:
    def singleNum(self, arr):
        # Code here
        temp = 0
        for a in arr:
            temp = temp ^ a

        i = 1
        while temp & i == 0:
            i = i << 1

        ans1, ans2 = 0, 0
        for a in arr:
            if a & i == 0:
                ans1 ^= a
            else:
                ans2 ^= a
        res = [ans1, ans2]

        return sorted(res)

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.singleNum([1, 2, 3, 2, 1, 4]),[3,4])

    def testcase2(self):
        self.assertEqual(self.solution.singleNum([2, 1, 3, 2]),[1,3])

    def testcase3(self):
        self.assertEqual(self.solution.singleNum([2, 1, 3, 3]),[1,2])

    def testcase4(self):
        self.assertEqual(self.solution.singleNum([1, 2]),[1,2])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()