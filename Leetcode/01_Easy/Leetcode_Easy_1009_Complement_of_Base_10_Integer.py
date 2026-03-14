import unittest

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = 0
        for bit in range(len(bin(n))-3,-1,-1):
            x = (n>>bit)&1
            res = (res*2) + (0 if x==1 else 1)
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.bitwiseComplement(5),2)

    def testcase2(self):
        self.assertEqual(self.solution.bitwiseComplement(7), 0)

    def testcase3(self):
        self.assertEqual(self.solution.bitwiseComplement(10), 5)

    def testcase4(self):
        self.assertEqual(self.solution.bitwiseComplement(11), 4)

    def tearDown(self):
        pass
