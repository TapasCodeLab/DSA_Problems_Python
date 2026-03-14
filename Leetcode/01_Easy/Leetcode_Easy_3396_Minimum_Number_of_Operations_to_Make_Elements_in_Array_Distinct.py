from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        distinct = set(nums)
        length = len(nums)
        i, count = 0, 0
        while i < length and len(distinct) != length - i:
            count += 1
            for _ in range(3):
                if i < length:
                    x = nums[i]
                    i += 1
                    freq[x] -= 1
                    if freq[x] == 0:
                        distinct.remove(x)

        return count

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minimumOperations([1,2,3,4,2,3,3,5,7]),2)

    def testcase2(self):
        self.assertEqual(self.solution.minimumOperations([4,5,6,4,4]),2)

    def testcase3(self):
        self.assertEqual(self.solution.minimumOperations([6,7,8,9]),0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()