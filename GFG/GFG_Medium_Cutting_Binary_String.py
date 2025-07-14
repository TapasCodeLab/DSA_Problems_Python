# https://www.geeksforgeeks.org/problems/cutting-binary-string1342/1

class Solution:
    def cuts(self, s):
        # code here
        def convert_to_binary(num):
            res = ['0'] if num == 0 else []
            while num != 0:
                res.append(str(num % 2))
                num = num // 2
            return ''.join(res[::-1])

        power_5 = []
        i = 1
        for _ in range(13):
            power_5.append(convert_to_binary(i))
            i *= 5

        self.n = len(s)
        self.dp = {}

        def helper(start):
            res = float('inf')
            if start == self.n:
                return 0
            elif s[start] == '0':
                return res
            elif start not in self.dp:
                for curr in power_5:
                    if len(curr) > len(s[start:]):
                        continue
                    elif s[start:start + len(curr)] == curr:
                        res = min(res, 1 + helper(start + len(curr)))
                self.dp[start] = res
            return self.dp[start]

        answer = helper(0)
        return -1 if answer == float('inf') else answer

import unittest


class TestSolution(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.cuts("101101101"), 3)

    def testcase2(self):
        self.assertEqual(self.solution.cuts("1111101"), 1)

    def testcase3(self):
        self.assertEqual(self.solution.cuts("1011111101"), 2)

    def testcase4(self):
        self.assertEqual(self.solution.cuts("00000"), -1)

    def testcase5(self):
        self.assertEqual(self.solution.cuts("10101101"), -1)

if __name__ == '__main__':
    unittest.main()