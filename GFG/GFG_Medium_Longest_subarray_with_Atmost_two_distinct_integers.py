# https://www.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1

class Solution:
    def totalElements(self, arr):
        # Code here
        start, end, result = 0, 0, 0
        frequency = {}
        while end < len(arr):
            frequency[arr[end]] = frequency.get(arr[end], 0) + 1
            while len(frequency) > 2:
                frequency[arr[start]] = frequency.get(arr[start]) - 1
                if frequency[arr[start]] == 0:
                    del frequency[arr[start]]
                start += 1
            result = max(result, end - start + 1)
            end += 1

        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.totalElements([2, 1, 2]),3)

    def testcase4(self):
        self.assertEqual(self.solution.totalElements([3, 1, 2, 2, 2, 2]),5)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()