import unittest

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.letters = ['a','b','c']

        def helper(prev, remaining_pos, remaining_count):
            if remaining_pos==0:
                return ''
            else:
                available_letters = self.letters[:]
                if prev in self.letters:
                    available_letters.remove(prev)
                available_letters.sort()
                for letter in available_letters:
                    if remaining_count>2**(remaining_pos-1):
                        remaining_count -= 2**(remaining_pos - 1)
                    else:
                        st = helper(letter, remaining_pos-1,remaining_count)
                        return letter+st


        if k>3*(2**(n-1)):
            return ''
        else:
            return helper('',n,k)

# Intuition : Total number of happy strings will allways be 3*(2^(n-1))
# Because for the first place there can be 3 letters but next all positions there is only 2 possibilities
# using the same logic we can determine for any letter in any position how many combinations can be generated
# and compare it with k to determine if we should create the happy string with that letter in that position or
# go for the next letter.

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.getHappyString(n = 1, k = 3),'c')

    def testcase2(self):
        self.assertEqual(self.solution.getHappyString(n = 1, k = 4),'')

    def testcase3(self):
        self.assertEqual(self.solution.getHappyString(n = 3, k = 9),'cab')

    def testcase4(self):
        self.assertEqual(self.solution.getHappyString(n = 3, k = 1),'aba')

    def testcase5(self):
        self.assertEqual(self.solution.getHappyString(n = 10, k = 100),"abacbabacb")

    def testcase6(self):
        self.assertEqual(self.solution.getHappyString(n = 5, k = 100),'')

    def testcase7(self):
        self.assertEqual(self.solution.getHappyString(n = 5, k = 22),'bacac')

    def tearDown(self):
        pass