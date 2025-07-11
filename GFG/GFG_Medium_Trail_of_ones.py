# https://www.geeksforgeeks.org/problems/trail-of-ones3242/1

class Solution:
    def countConsec(self, n: int) -> int:
        # code here
        dp =[[-1 ] *2 for _ in range( n +1)]

        def helper(length, current):
            if length==n:
                return 1
            if dp[length][current] == -1:
                dp[length][current] = helper(length +1 ,0)
                if current==0:
                    dp[length][current] += helper(length +1 ,1)
            return dp[length][current]

        no_cons_one = helper(1 ,0 ) +helper(1 ,1)
        return 2** n - no_cons_one

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(self.sol.countConsec(n = 2),1)

    def testcase2(self):
        self.assertEqual(self.sol.countConsec(n = 3),3)

    def testcase3(self):
        self.assertEqual(self.sol.countConsec(n = 5),19)

    def testcase4(self):
        self.assertEqual(self.sol.countConsec(n = 30),1071563515)


    def tearDown(self):
        pass


if __name__=='__main__':
    unittest.main()
