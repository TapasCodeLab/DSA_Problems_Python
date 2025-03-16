import math
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(minute):
            res = 0
            for rank in ranks:
                res += int(math.sqrt(minute//rank))
            return res

        low, high, ans = 1, max(ranks)*cars*cars, 0
        while low <= high:
            mid = (low+high)//2
            if check(mid)>=cars:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.repairCars([4,2,3,1],10),16)

    def testcase2(self):
        self.assertEqual(self.solution.repairCars([5,1,8],6),16)

    def testcase3(self):
        self.assertEqual(self.solution.repairCars([40,20,30,10,5,23,25,22,31,42,44],100000),1687950030)

    def testcase4(self):
        self.assertEqual(self.solution.repairCars([1],1),1)

    def testcase5(self):
        self.assertEqual(self.solution.repairCars([1],10),100)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()