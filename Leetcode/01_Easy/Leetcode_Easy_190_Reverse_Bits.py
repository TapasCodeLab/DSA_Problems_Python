class Solution:
    def reverseBits(self, n: int) -> int:
        bit_array = [0]*32
        i = 0
        while n:
            reminder = n%2
            n = n//2
            bit_array[i] += reminder
            i += 1

        result = 0
        for bit in bit_array:
            result = result*2 + bit

        return result


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.reverseBits(43261596),964176192)

    def testcase2(self):
        self.assertEqual(self.solution.reverseBits(2147483644),1073741822)

    def testcase3(self):
        self.assertEqual(self.solution.reverseBits(0),0)

    def testcase4(self):
        self.assertEqual(self.solution.reverseBits(21474),1204420608)

    def testcase5(self):
        self.assertEqual(self.solution.reverseBits(2),1073741824)

    def tearDown(self):
        pass
