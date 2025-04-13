class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def expow(n, p, mod):
            if p == 0:
                return 1 % mod
            else:
                part = expow(n, p // 2, mod)
                if p % 2 == 1:
                    return (part * part * n) % mod
                else:
                    return (part * part) % mod

        # for every even indices we have 5 choices and for every odd indices we hav 4 choices
        mod = 10 ** 9 + 7
        even = (n // 2) + (n % 2)
        odd = (n // 2)
        res = (expow(5, even, mod) * expow(4, odd, mod)) % mod
        return res

        # for every even indices we have 5 choices and for every odd indices we hav 4 choices
        # right ans but TLE for given constraint 10**15
        # for i in range(n):
        #     if i%2==0:
        #         res = (res*5) % mod
        #     else:
        #         res = (res*4) % mod
        # return res



import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countGoodNumbers(1),5)

    def testcase2(self):
        self.assertEqual(self.solution.countGoodNumbers(4),400)

    def testcase3(self):
        self.assertEqual(self.solution.countGoodNumbers(50),564908303)

    def testcase4(self):
        self.assertEqual(self.solution.countGoodNumbers(1000000000000000), 711414395)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()