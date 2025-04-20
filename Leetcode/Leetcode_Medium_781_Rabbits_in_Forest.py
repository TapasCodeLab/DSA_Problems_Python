from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        res = 0
        for answer in answers:
            if answer + 1 not in freq:
                freq[answer + 1] = 1
            else:
                freq[answer + 1] += 1
            if freq[answer + 1] == answer + 1:
                res += answer + 1
                del freq[answer + 1]

        for key in freq.keys():
            res += key

        return res


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.numRabbits([1,1,2]),5)

    def testcase2(self):
        self.assertEqual(self.solution.numRabbits([10,10,10]),11)

    def testcase3(self):
        self.assertEqual(self.solution.numRabbits([1,1,1,1,1,1]),6)

    def testcase4(self):
        self.assertEqual(self.solution.numRabbits([1,0,1,0,0]),5)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()