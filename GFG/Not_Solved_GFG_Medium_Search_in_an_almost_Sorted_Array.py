# https://www.geeksforgeeks.org/problems/search-in-an-almost-sorted-array/1

class Solution:
    def findTarget(self, arr, target):
        # code here
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif mid - 1 >= 0 and arr[mid - 1] == target:
                return mid - 1
            elif mid - 1 >= 0 and arr[mid - 1] < target < arr[mid] or target < min(arr[mid - 1], arr[mid]):
                high = mid - 1
            elif mid + 1 <= len(arr) - 1 and arr[mid + 1] == target:
                return mid + 1
            elif mid + 1 <= len(arr) - 1 and arr[mid] > target > arr[mid + 1] or target > max(arr[mid + 1], arr[mid]):
                low = mid + 1

        return -1

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def testcase1(self):
    #     self.assertEqual(self.solution.findTarget([10, 3, 40, 20, 50, 80, 70],40),2)
    #
    # def testcase2(self):
    #     self.assertEqual(self.solution.findTarget([10, 3, 40, 20, 50, 80, 70],10),0)

    def testcase3(self):
        self.assertEqual(self.solution.findTarget([10, 3, 40, 20, 50, 80, 70],70),6)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()