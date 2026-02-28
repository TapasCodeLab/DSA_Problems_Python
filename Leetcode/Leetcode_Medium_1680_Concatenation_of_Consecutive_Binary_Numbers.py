import unittest

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9+7
        output = 0
        # # Analysis  - TC: O(N∗Log(N))
        # for number in range(1,n+1):
        #     st = bin(number)[2:]
        #     for s in st:
        #         output = (output*2 + int(s))%mod
        # return output

        # # Analysis  - TC: O(N)
        bit = 0
        for number in range(1,n+1):
            if number & (number-1) == 0:   #number of bits changes only when number reaches 2^^x
                bit += 1
            output = ((output<<bit) + number)%mod
        return output


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.concatenatedBinary(1),1)

    def testcase2(self):
        self.assertEqual(self.solution.concatenatedBinary(3),27)

    def testcase3(self):
        self.assertEqual(self.solution.concatenatedBinary(12),505379714)

    def testcase4(self):
        self.assertEqual(self.solution.concatenatedBinary(10000),356435599)

    def testcase5(self):
        self.assertEqual(self.solution.concatenatedBinary(100000),757631812)

    def tearDown(self):
        pass

#
# Analysis  - TC: O(N∗Log(N))
#
#  for n == 3 ans is 27
#         mod 7
#         27 % 7 -> 6
# 1       (0*2 + 1) % 7 -> 1
# 1       (1*2 + 1) % 7 -> 3
# 0       (3*2 + 0) % 7 -> 6
# 1       (6*2 + 1) % 7 -> 6
# 1       (6*2 + 1) % 7 -> 6
#
#         mod 5
#         27 % 5 -> 2
# 1       (0*2 + 1) % 5 -> 1
# 1       (1*2 + 1) % 5 -> 3
# 0       (3*2 + 0) % 5 -> 1
# 1       (1*2 + 1) % 5 -> 3
# 1       (3*2 + 1) % 5 -> 2
#
# # Analysis  - TC: O(N)
#
# 1 -> 0<<2 + 1 -> 1
# 2 -> 1<<2 + 2 -> 6
# 3 -> 6<<2 + 3 -> 27
#
# 11011