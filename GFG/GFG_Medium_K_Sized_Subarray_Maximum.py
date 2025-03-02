# https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1

class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        stack, res = [], []
        i = 0
        while i < k:
            a = arr[i]
            while stack and stack[-1][0] < a:
                stack.pop()
            stack.append([a, i])
            i += 1
        res.append(stack[0][0])

        while i < len(arr):
            a = arr[i]
            while stack and stack[0][1] <= i - k:
                stack.pop(0)
            while stack and stack[-1][0] < a:
                stack.pop()
            stack.append([a, i])
            i += 1
            res.append(stack[0][0])

        return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maxOfSubarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], 3),[3, 3, 4, 5, 5, 5, 6])

    def testcase2(self):
        self.assertEqual(self.solution.maxOfSubarrays([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4),[10, 10, 10, 15, 15, 90, 90])

    def testcase3(self):
        self.assertEqual(self.solution.maxOfSubarrays([5, 1, 3, 4, 2, 6], 1),[5, 1, 3, 4, 2, 6])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()