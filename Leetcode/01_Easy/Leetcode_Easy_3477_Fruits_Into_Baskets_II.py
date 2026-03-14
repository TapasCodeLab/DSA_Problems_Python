from typing import List

class Solution:
    def numOfUnplacedFruits(self,fruits: List[int], baskets: List[int]) -> int:
        result = 0
        for fruit in fruits:
            for index,basket in enumerate(baskets):
                if basket>=fruit:
                    baskets[index] = 0
                    break
            else:
                result += 1
        return result

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]),1)

    def testcase2(self):
        self.assertEqual(self.solution.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]),0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()