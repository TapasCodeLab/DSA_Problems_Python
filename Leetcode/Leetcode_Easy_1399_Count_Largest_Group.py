class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumDigits(val):
            res = 0
            while val:
                res += val%10
                val = val//10
            return res

        from collections import Counter
        freq = Counter()
        for i in range(1, n+1):
            s = sumDigits(i)
            freq[s] = freq.get(s,0)+1

        mx = max([val for val in freq.values()])
        res = sum([1 if val==mx else 0 for val in freq.values()])
        return res

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countLargestGroup(1),1)

    def testcase2(self):
        self.assertEqual(self.solution.countLargestGroup(2),2)

    def testcase3(self):
        self.assertEqual(self.solution.countLargestGroup(13),4)

    def testcase4(self):
        self.assertEqual(self.solution.countLargestGroup(10000),1)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()