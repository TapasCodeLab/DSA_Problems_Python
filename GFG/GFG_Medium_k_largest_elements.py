# https://www.geeksforgeeks.org/problems/k-largest-elements4206/1

class Solution:
	def kLargest(self, arr, k):
		# Your code here
		arr.sort(reverse=True)
		return arr[:k]

# Test

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.kLargest([12, 5, 787, 1, 23], 2),[787, 23])

    def test_testcase2(self):
        self.assertEqual(self.solution.kLargest([1, 23, 12, 9, 30, 2, 50], 3),[50, 30, 23])

    def test_testcase3(self):
        self.assertEqual(self.solution.kLargest([12, 23], 1),[23])


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
