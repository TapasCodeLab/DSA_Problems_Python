from math import ceil
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seive = [True for _ in range(int(pow(right,0.5))+1)]
        primes =[]
        i = 2
        while i*i<=right:
            if seive[i]:
                primes.append(i)
                for x in range(2*i,len(seive),i):
                    seive[x] = False
            i+=1

        seive = [True for _ in range(right - left + 1)]
        for p in primes:
            if left<=p<=right:
                first = ((ceil(left/p)*p)-left)+p
            else:
                first = ((ceil(left / p) * p) - left)
            for i in range(first, right - left + 1, p):
                seive[i] = False

        primes = [i+left for i in range(right-left+1) if seive[i] and i+left!=1]

        res1, res2, prev, diff = -1, -1, -1, float('inf')
        for num in primes:
            if prev == -1:
                prev = num
            elif num - prev < diff:
                res1, res2, diff = prev, num, num - prev
                prev = num
            else:
                prev = num

        return [res1, res2]


# #Below brute force solution works but gives TLE
# class Solution:
#     def closestPrimes(self, left: int, right: int) -> List[int]:
#         def isPrime(x):
#             if x== 1:
#                 return False
#             i = 2
#             while (i * i <= x):
#                 if x % i == 0:
#                     return False
#                 i += 1
#             return True
#
#         res1, res2, prev, diff = -1, -1, -1, float('inf')
#         for num in range(left, right + 1):
#             if isPrime(num):
#                 if prev == -1:
#                     prev = num
#                 elif num - prev < diff:
#                     res1, res2, diff = prev, num, num - prev
#                     prev = num
#                 else:
#                     prev = num
#
#         return [res1, res2]
#

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.closestPrimes(10,19),[11,13])

    def testcase2(self):
        self.assertEqual(self.solution.closestPrimes(4,6),[-1,-1])

    def testcase3(self):
        self.assertEqual(self.solution.closestPrimes(10,10),[-1,-1])

    def testcase4(self):
        self.assertEqual(self.solution.closestPrimes(9,999999),[11,13])

    def testcase5(self):
        self.assertEqual(self.solution.closestPrimes(1,100000),[2,3])

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()