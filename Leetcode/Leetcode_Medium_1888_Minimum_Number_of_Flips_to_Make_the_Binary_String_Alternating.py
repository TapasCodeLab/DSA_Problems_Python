import unittest

class Solution:
    def minFlips(self, s: str) -> int:
        def count_odd_even(s):
            odd1, even1, odd0, even0 = 0, 0, 0, 0
            for i in range(len(s)):
                if i%2 == 1: #even
                    if s[i]=='1':
                        even1 +=1
                    else:
                        even0 +=1
                else:  #odd
                    if s[i]=='1':
                        odd1 +=1
                    else:
                        odd0 +=1
            return odd1, even1, odd0, even0

        odd1, even1, odd0, even0 = count_odd_even(s)
        result = min((odd1+even0),(odd0+even1))
        lengthflag = (len(s)%2)==0  #True if length of the string is even

        for i in range(len(s)):
            if s[i]=='1':
                odd1 -=1
                odd1, even1, odd0, even0 = even1, odd1, even0, odd0
                if lengthflag:
                    even1 += 1
                else:
                    odd1 += 1
            else:
                odd0 -=1
                odd1, even1, odd0, even0 = even1, odd1, even0, odd0
                if lengthflag:
                    even0 += 1
                else:
                    odd0 += 1
            result = min(result, (odd1 + even0), (odd0 + even1))
        return result

#Analysis  how to count min change required
#for any string what is the min change required
#example "1101010" -> 1
# odd1 -1 , even1 -3 , odd0-3 even0 - 0
# comb1- final = odd0+even1 => change required in (odd1+even0) bits= (1+0) = 1
# comb2- final = odd1+even0 => change required in (odd0+even1) bits= (3+3) = 6
# min of this => 1 is the ans
#example after 1 shift "1010101"
# odd1 -4 , even1 -0 , odd0-0 even0 - 3

#example "010" -> 0
# odd1 -0 , even1 -1 , odd0-2 even0 - 0
# comb1- final = odd0+even1 => change required in (odd1+even0) bits= (0+0) = 0
# comb2- final = odd1+even0 => change required in (odd0+even1) bits= (2+1) = 3
# min of this => 0 is the ans

#example "1110" -> 0
# odd1 -2 , even1 -1 , odd0-0 even0 - 1
# comb1- final = odd0+even1 => change required in (odd1+even0) bits= (2+1) = 3
# comb2- final = odd1+even0 => change required in (odd0+even1) bits= (0+1) = 1
# min of this => 1 is the ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.minFlips("111000"),2)

    def testcase2(self):
        self.assertEqual(self.solution.minFlips("010"),0)

    def testcase3(self):
        self.assertEqual(self.solution.minFlips("1110"),1)

    def testcase4(self):
        self.assertEqual(self.solution.minFlips("1101010"),0)

    def testcase5(self):
        self.assertEqual(self.solution.minFlips("01001001101"),2)

    def tearDown(self):
        pass
