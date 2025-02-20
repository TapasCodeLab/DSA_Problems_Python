from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.nums = set(nums)
        self.res = ''

        def backtrack(current, length):
            if self.res != '':
                return
            if len(current) == length:
                if ''.join(current) not in self.nums:
                    self.res = ''.join(current)
                return
            else:
                for i in ['0','1']:
                    current.append(i)
                    backtrack(current[:], length)
                    current.pop()

        backtrack([],len(nums))
        return self.res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_solution1(self):
        self.assertIn(self.s.findDifferentBinaryString(["00", "01"]), ["00", "11"])

    def test_solution2(self):
        self.assertIn(self.s.findDifferentBinaryString(["00","01"]),["10","11"])

    def tearDown(self):
        pass

if __name__ =="__main__":
    unittest.main()



