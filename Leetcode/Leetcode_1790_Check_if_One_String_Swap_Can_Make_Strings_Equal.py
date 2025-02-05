
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        elif s1==s2:
            return True
        else:
            first, second = -1, -1
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if first == -1:
                        first = i
                    else:
                        second = i
                    count += 1
            if count != 2:
                return False
            else:
                return s1[first]==s2[second] and s1[second]==s2[first]


if __name__ == '__main__':
    s = Solution()
    print(s.areAlmostEqual("abcdef", "abedcf"))
    print(s.areAlmostEqual("abcd", "abcd"))
    print(s.areAlmostEqual("abcde", "abcdf"))
    print(s.areAlmostEqual("abcd", "dabc"))

