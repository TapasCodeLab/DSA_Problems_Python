# https://www.geeksforgeeks.org/problems/next-greater-element/1

class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack = []
        for i in range(len(arr)-1,-1,-1):
            dig = arr[i]
            while stack and stack[-1]<dig:
                stack.pop()
            stack.append(dig)

        res = []
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[i]>=stack[-1]:
                stack.pop()
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(arr[i])
        return res[::-1]

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.nextLargerElement([1, 3, 2, 4]),[3, 4, 4, -1])

    def test_testcase2(self):
        self.assertEqual(self.solution.nextLargerElement([0, 2, 3, 1, 1]), [2, 3, -1, 2, 2])

    def test_testcase3(self):
        self.assertEqual(self.solution.nextLargerElement([1, 1, 2, 5, 2, 2, 5, 2, 3, 3, 3, 3, 5, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 6, 6, 6]),
                         [2, 2, 5, 6, 5, 5, 6, 3, 5, 5, 5, 5, 6, 6, 2, 6, 2, 6, 2, 2, 2, 6, 6, 6, -1, -1, -1])


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()