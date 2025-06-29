class Solution:
    def splitArray(self, arr, k):
        # code here
        def checkSubCnt(limit):
            count, total = 1, 0
            for a in arr:
                if total + a <= limit:
                    total += a
                else:
                    count += 1
                    total = a
            return count

        checkSubCnt(18)

        low, high = max(arr), sum(arr)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if checkSubCnt(mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.splitArray([1,2,3,4],3),4)

    def testcase2(self):
        self.assertEqual(self.solution.splitArray([1,1,2],2),2)

    def testcase3(self):
        self.assertEqual(self.solution.splitArray([1,1,1,1,1,1,5],7),5)

    def testcase4(self):
        self.assertEqual(self.solution.splitArray([12, 12, 6, 2, 16, 5, 13, 1, 3, 5, 1, 13],7),18)

    def tearDown(self):
        pass
