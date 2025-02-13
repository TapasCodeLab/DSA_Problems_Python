import unittest

from Leetcode_3066_Minimum_Operations_to_Exceed_Threshold_Value_II import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testCase1(self):
        self.assertEqual(self.solution.minOperations(nums = [2,11,10,1,3], k = 10),2)

    def testCase2(self):
        self.assertEqual(self.solution.minOperations(nums = [1,1,2,4,9], k = 20),4)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()