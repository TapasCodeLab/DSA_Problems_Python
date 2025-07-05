# https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/1

# the theory behind this calculation is that the result will allways be
# the sum of 2 continuous array elements
# this can be proved by taking 2 numbers x and y and putting a number k between them
# if K is greater than both of them -> ans will be k+max(x,y)
# if K is less than both of them -> ans will be k+max(x,y)
# if value of K is between them -> ans will be k+max(x,y)
# Hence is all cases - k will be included in the answer, which means answer cannot lie
# in two indices separated from one another.


class Solution:
    def maxSum(self, arr):
        # code here
        result = 0
        for i in range(len(arr) - 1):
            result = max(result, arr[i] + arr[i + 1])

        return result


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.maxSum([4, 3, 5, 1]),8)

    def testcase2(self):
        self.assertEqual(self.solution.maxSum([1, 2, 3]),5)

    def testcase3(self):
        self.assertEqual(self.solution.maxSum([1, 2, 5, 4, 8, 6, 3, 2, 5, 7, 9, 5, 4, 2, 1, 3, 5, 8, 4, 5, 2, 1, 8, 7, 6, 5, 2, 15]),17)

    def testcase4(self):
        self.assertEqual(
            self.solution.maxSum([1, 2, 5, 4, 8, 6, 3, 2, 5, 7, 11, 5, 4, 2, 1, 3, 5, 8, 4, 5, 2, 1, 8, 7, 6, 5, 2, 15]),18)

    def testcase5(self):
        self.assertEqual(self.solution.maxSum([1,1,1,1,1,1,1]),2)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()