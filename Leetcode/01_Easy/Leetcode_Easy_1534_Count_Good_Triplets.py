from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res, n = 0, len(arr)
        for k in range(n):
            for j in range(k):
                if abs(arr[j] - arr[k]) <= b:
                    for i in range(j):
                        if abs(arr[i] - arr[j]) <= a and abs(arr[i] - arr[k]) <= c:
                            res += 1
        return res



import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3),4)

    def testcase2(self):
        self.assertEqual(self.solution.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1),0)



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()