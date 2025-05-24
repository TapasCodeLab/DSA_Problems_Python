# https://www.geeksforgeeks.org/problems/sum-of-all-substrings-of-a-number-1587115621/1
class Solution:
    def sumSubstrings(self, s):
        # code here
        # One pass - contribution method
        res = 0
        n = len(s)
        multiplier = 1
        for i in range(n - 1, -1, -1):
            digit = int(s[i])
            res += digit * multiplier * (i + 1)
            multiplier = multiplier * 10 + 1

        return res

        # #Brute-Force but accepted
        # res = 0
        # for end in range(1,len(s)+1):
        #     for start in range(end):
        #         res += int(s[start:end])
        # return res


import unittest

class TestClass(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.sumSubstrings("6759"),8421)

    def testcase2(self):
        self.assertEqual(self.solution.sumSubstrings("421"),491)

    def testcase3(self):
        self.assertEqual(self.solution.sumSubstrings("1234"),1670)

    def testcase4(self):
        self.assertEqual(self.solution.sumSubstrings("123456789"),167657325)

    def testcase5(self):
        self.assertEqual(self.solution.sumSubstrings("0002354"),10911)

    def tearDown(self):
        pass
