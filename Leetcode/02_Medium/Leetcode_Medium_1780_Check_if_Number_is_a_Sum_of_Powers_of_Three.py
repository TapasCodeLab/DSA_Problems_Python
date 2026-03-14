class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n%3 == 2:
                return False
            else:
                n = n//3
        return True

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertTrue(self.solution.checkPowersOfThree(12))

    def testcase2(self):
        self.assertTrue(self.solution.checkPowersOfThree(91))

    def testcase3(self):
        self.assertFalse(self.solution.checkPowersOfThree(21))

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()