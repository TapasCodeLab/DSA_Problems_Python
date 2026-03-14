import unittest

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        @staticmethod
        def isPrime(x):
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        @staticmethod
        def countSetBits(x):
            res = 0
            while x:
                res += 1
                x = x & (x - 1)
            return res

        # Create cache of prime numbers
        prime_numbers = set([x for x in range(2, 33) if isPrime(x)])
        prime_setbits = [x for x in range(left, right + 1) if countSetBits(x) in prime_numbers]
        return len(prime_setbits)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countPrimeSetBits(6,10),4)

    def testcase2(self):
        self.assertEqual(self.solution.countPrimeSetBits(10, 15),5)

    def tearDown(self):
        pass
