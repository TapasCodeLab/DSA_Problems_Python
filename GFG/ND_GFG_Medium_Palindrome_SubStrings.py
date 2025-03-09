# https://www.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1
class Solution:
    def isPalin(self, s):
        pass



# # Below brute force approach works but gives TLE
# class Solution:
#     def isPalin(self, s):
#         i, j = 0, len(s ) -1
#         while i< j:
#             if s[i] == s[j]:
#                 i += 1
#                 j -= 1
#             else:
#                 return False
#         return True
#
#     def countPS(self, s):
#         # code here
#         res = 0
#         for i in range(len(s) - 1):
#             for j in range(i + 2, len(s) + 1):
#                 if self.isPalin(s[i:j]):
#                     res += 1
#         return res
