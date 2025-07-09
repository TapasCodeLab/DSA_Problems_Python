# https://www.geeksforgeeks.org/problems/sum-of-subarray-minimum/1
class Solution:
    def sumSubMins(self, arr):
        # Code here
        # prefix and suffix represents for the length this is the smallest number
        prefix, suffix, stack = [], [], []
        n = len(arr)
        for index, value in enumerate(arr):
            while stack and stack[-1][0] >= value:
                stack.pop()
            prev_index = stack[-1][1] if stack else -1
            prefix.append(index - prev_index)
            stack.append([value, index])

        stack = []
        for index in range(n - 1, -1, -1):
            while stack and stack[-1][0] > arr[index]:
                stack.pop()
            next_index = stack[-1][1] if stack else n
            suffix.append(next_index - index)
            stack.append([arr[index], index])

        suffix = suffix[::-1]

        # print(prefix, suffix)

        result = 0
        for index, value in enumerate(arr):
            result += value * prefix[index] * suffix[index]

        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testcase1(self):
        self.assertEqual(self.solution.sumSubMins([3, 1, 2, 4]),17)

    def test_testcase2(self):
        self.assertEqual(self.solution.sumSubMins([71, 55, 82, 55]),593)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()