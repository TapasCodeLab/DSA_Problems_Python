import unittest
from Leetcode_1910_Remove_All_Occurrences_of_a_Substring import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
         self.assertEqual("dab", self.solution.removeOccurrences("daabcbaabcbc","abc"))

    def test_case2(self):
         self.assertEqual("ab", self.solution.removeOccurrences("axxxxyyyyb","xy"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()