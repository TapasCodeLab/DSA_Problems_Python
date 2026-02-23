class Solution:

    @staticmethod
    def allPossibleNumbers(k):
        for i in range(2**k):
            yield str(bin(i))[2:].rjust(k,'0')

    def hasAllCodes(self, s: str, k: int) -> bool:
        gen = Solution.allPossibleNumbers(k)
        all_numbers = set([])
        for i in range(len(s)-k+1):
            all_numbers.add(s[i:i+k])

        for i in gen:
            if i not in all_numbers:
                return False
        return True


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.hasAllCodes(s = "00110110", k = 2))

    def testcase2(self):
        self.assertTrue(self.solution.hasAllCodes(s = "0110", k = 1))

    def testcase3(self):
        self.assertFalse(self.solution.hasAllCodes(s = "0110", k = 2))

    def testcase4(self):
        self.assertFalse(self.solution.hasAllCodes(s = "001101100101010101010101011100111001111110100100000000111111111010101010101010101010101010111", k = 15))

    def tearDown(self):
        pass

