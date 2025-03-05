# https://www.geeksforgeeks.org/problems/longest-string-chain/1

class Solution:
    def longestStringChain(self, words):
        # Code here
        words.sort(key=lambda x: len(x))
        dp = {'': 0}

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                temp = word[:i] + word[i + 1:]
                if temp in dp:
                    dp[word] = max(dp[word], dp[temp] + 1)

        return max(list(dp.values()))


#Not optimum
# class Solution:
#     def longestStringChain(self, words):
#         # Code here
#         def checkCharDiff(word1, word2):
#             if len(word2) == len(word1) + 1:
#                 i, j, count = 0, 0, 0
#                 while i < len(word1) and j < len(word2):
#                     if word1[i] == word2[j]:
#                         i += 1
#                     else:
#                         count += 1
#                     j += 1
#                 count += len(word2)-j
#                 return count == 1
#             return False
#
#         words.sort(key=lambda x: len(x))
#
#         dp = [1] * len(words)
#         for i in range(1, len(words), 1):
#             temp = [0]
#             for j in range(i):
#                 #print(words[j], words[i],checkCharDiff(words[j], words[i]))
#                 if checkCharDiff(words[j], words[i]):
#                     temp.append(dp[j])
#             dp[i] = max(temp) + 1
#         return max(dp)

    # {

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.longestStringChain(['ba','b','a','bca','bda','bdca']),4)

    def testcase2(self):
        self.assertEqual(self.solution.longestStringChain(['abcd', 'dbqca']),1)

    def testcase3(self):
        self.assertEqual(self.solution.longestStringChain(['a','x','ab','abc','cad','cab','abcd','abcds','abecd','abfecd']),6)

    def testcase4(self):
        self.assertEqual(self.solution.longestStringChain(['a','x','b','c','d']),1)

    def testcase5(self):
        self.assertEqual(self.solution.longestStringChain(['a','xy','b','ab','xyz','cxyz']),3)


    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()