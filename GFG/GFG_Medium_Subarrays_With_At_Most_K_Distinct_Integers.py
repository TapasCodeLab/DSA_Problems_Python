# https://www.geeksforgeeks.org/problems/subarrays-with-at-most-k-distinct-integers/1

class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        start, result = 0, 0
        frequency = {}
        for end in range(len(arr)):
            frequency[arr[end]] = frequency.get(arr[end], 0) + 1
            while len(frequency) > k:
                frequency[arr[start]] = frequency.get(arr[start]) - 1
                if frequency[arr[start]] == 0:
                    del frequency[arr[start]]
                start += 1

            result += end - start + 1
        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countAtMostK([1, 2, 2, 3], 2),9)

    def testcase2(self):
        self.assertEqual(self.solution.countAtMostK([1, 1, 1], 1),6)

    def testcase3(self):
        self.assertEqual(self.solution.countAtMostK([1, 2, 1, 1, 3, 3, 4, 2, 1], 2),24)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

