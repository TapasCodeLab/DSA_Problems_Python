# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
class Solution:
    def isSubsetSum(self, arr, sum):
        # code here
        dp = [[-1 for c in range(len(arr) + 1)] for r in range(sum + 1)]
        # As it is a subset zero is possible for all indexes
        for c in range(len(arr) + 1):
            dp[0][c] = True

        def helper(i, total):
            if total < 0 or i < 0:
                return False
            if dp[total][i] == -1:
                dp[total][i] = helper(i - 1, total) or helper(i - 1, total - arr[i - 1])
            return dp[total][i]

        return helper(len(arr), sum)

        # Below Solution will surely give TLE - 2^n tc backtracking
        # self.res = False

        # def backtrack(i,total):
        #     if total==sum:
        #         self.res=True
        #         return
        #     elif i>=len(arr) or total > sum:
        #         return
        #     else:
        #         backtrack(i+1,total)
        #         backtrack(i+1,total+arr[i])
        #         return

        # backtrack(0,0)
        # return self.res


import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.isSubsetSum([3, 34, 4, 12, 5, 2], 9 ))

    def testcase2(self):
        self.assertFalse(self.solution.isSubsetSum([3, 34, 4, 12, 5, 2], 30 ))

    def testcase3(self):
        self.assertTrue(self.solution.isSubsetSum([1,2,3], 6 ))

    def testcase4(self):
        self.assertFalse(self.solution.isSubsetSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200], 40000 ))

    def testcase5(self):
        self.assertTrue(self.solution.isSubsetSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200], 20000 ))



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
