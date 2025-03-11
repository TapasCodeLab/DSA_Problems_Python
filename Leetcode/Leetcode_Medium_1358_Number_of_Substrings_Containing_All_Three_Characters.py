class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, start, end, freq, n = 0,0,0,{}, len(s)
        while end<len(s):
            freq[s[end]] = freq.get(s[end],0)+1
            while len(freq)==3:
                res += n-end  # If a substr is valid all substr including it is also valid
                freq[s[start]] = freq.get(s[start])-1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
            end += 1
        return res


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.numberOfSubstrings("abcabc"),10)

    def testcase2(self):
        self.assertEqual(self.solution.numberOfSubstrings("aaacb"),3)

    def testcase3(self):
        self.assertEqual(self.solution.numberOfSubstrings("abc"),1)

    def testcase4(self):
        self.assertEqual(self.solution.numberOfSubstrings("aaacbaa"),11)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()

