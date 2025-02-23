# https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        stack = []
        res = []
        for a in arr[::-1]:
            while stack and stack[-1] <= a:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(a)

        return res[::-1]

# Test

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.nextLargerElement([1, 3, 2, 4]), [3, 4, 4, -1])

    def test_testcase2(self):
        self.assertEqual(self.solution.nextLargerElement([6, 8, 0, 1, 3]), [8, -1, 1, 3, -1])

    def test_testcase3(self):
        self.assertEqual(self.solution.nextLargerElement([10, 20, 30, 50]), [20, 30, 50, -1])

    def test_testcase4(self):
        self.assertEqual(self.solution.nextLargerElement([50, 40, 30, 10]), [-1, -1, -1, -1])

    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()


