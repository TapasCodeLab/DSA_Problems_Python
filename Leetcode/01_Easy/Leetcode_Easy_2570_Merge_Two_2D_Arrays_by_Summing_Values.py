from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i+= 1
                j+= 1
            elif nums1[i][0] < nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]])
                i+=1
            else:
                res.append([nums2[j][0], nums2[j][1]])
                j+=1

        while i < len(nums1):
            res.append([nums1[i][0], nums1[i][1]])
            i+= 1

        while j < len(nums2):
            res.append([nums2[j][0], nums2[j][1]])
            j+=1

        return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]),[[1,6],[2,3],[3,2],[4,6]])

    def testcase2(self):
        self.assertEqual(self.solution.mergeArrays([[2,4],[3,6],[5,5]],[[1,3],[4,3]]),[[1,3],[2,4],[3,6],[4,3],[5,5]])

    def testcase3(self):
        self.assertEqual(self.solution.mergeArrays([[2,4]],[[1,3],[4,3]]),[[1,3],[2,4],[4,3]])

    def testcase4(self):
        self.assertEqual(self.solution.mergeArrays([[2,4],[3,6],[5,5]],[[2,4]]),[[2,8],[3,6],[5,5]])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()