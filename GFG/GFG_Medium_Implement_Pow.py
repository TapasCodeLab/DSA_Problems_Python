# https://www.geeksforgeeks.org/problems/powx-n/1

class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e == 0:
            return 1
        elif e ==1:
            return b
        elif e<0:
            return 1/self.power(b,-e)
        else:
            p = self.power(b,e//2)
            if e%2==0:
                return p*p
            else:
                return p*p*b


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.power(b = 3.00000, e = 5),243.00000)

    def testcase2(self):
        self.assertEqual(round(self.solution.power(b = 0.55000, e = 3),5),0.16638)

    def testcase3(self):
        self.assertEqual(round(self.solution.power(b = -0.67000, e = -7),5),-16.49971)

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()