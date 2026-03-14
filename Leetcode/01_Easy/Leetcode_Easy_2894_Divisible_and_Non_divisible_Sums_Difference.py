class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(1,n+1):
            if i%m==0:
                num2 += i
            else:
                num1 += i

        return num1-num2


import unittest

class TestClass(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.differenceOfSums(10, 3),19)

    def testcase2(self):
        self.assertEqual(self.solution.differenceOfSums(5,6),15)

    def testcase3(self):
        self.assertEqual(self.solution.differenceOfSums(5, 1),-15)

    def tearDown(self):
        pass