from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1]*n
        parent = [i for i in range(n)]
        nums.sort()
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    parent[i] = j

        end = dp.index(max(dp))
        res = []
        while parent[end] != end:
            res.append(nums[end])
            end = parent[end]

        res.append(nums[end])
        res = res[::-1]
        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.largestDivisibleSubset([1,2,3]),[1,2])

    def testcase2(self):
        self.assertEqual(self.solution.largestDivisibleSubset([1,2,4,8]),[1,2,4,8])

    def testcase3(self):
        self.assertEqual(self.solution.largestDivisibleSubset([2, 5, 4, 3, 120]),[2,4,120])

    def testcase4(self):
        self.assertEqual(self.solution.largestDivisibleSubset([2, 5, 3, 120, 4]),[2,4,120])

    def testcase5(self):
        self.assertEqual(self.solution.largestDivisibleSubset([3]),[3])

    def testcase6(self):
        self.assertEqual(self.solution.largestDivisibleSubset([1,3,8,4,6,7,9,10,12,15,18,17,2,66,106,69,517]),[1,2,4,8])

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()

