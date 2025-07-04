from typing import List
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def next_char(ch):
            return chr((ord(ch)-ord('a')+1)%26 + ord('a'))

        def helper(step, position):
            if step == 0:
                return 'a'
            half_total_char = 2**(step-1)
            if position<=half_total_char:
                return helper(step-1, position)
            elif operations[step-1] == 0:
                return helper(step-1, position-half_total_char)
            else:
                return next_char(helper(step-1, position-half_total_char))

        return helper(len(operations),k)
    #'abab'


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.kthCharacter(5,[0,0,0]),'a')

    def testcase2(self):
        self.assertEqual(self.solution.kthCharacter(10,[0,1,0,1]),'b')

    def testcase3(self):
        self.assertEqual(self.solution.kthCharacter(103,[0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0]),'c')

    def testcase4(self):
        self.assertEqual(self.solution.kthCharacter(103058091758,[0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0]),'n')

    def testcase5(self):
        self.assertEqual(self.solution.kthCharacter(1,[0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0]),'a')

    def testcase6(self):
        self.assertEqual(self.solution.kthCharacter(1,[0]),'a')

    def testcase7(self):
        self.assertEqual(self.solution.kthCharacter(4,[1,0]),'b')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

