from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        from collections import Counter
        self.freq_num1 = Counter(nums1)
        self.freq_num2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        prev_val = self.nums2[index]
        self.freq_num2[prev_val] = self.freq_num2.get(prev_val) - 1
        self.freq_num2[prev_val+val] = self.freq_num2.get(prev_val+val, 0) + 1
        self.nums2[index] = prev_val+val

    def count(self, tot: int) -> int:
        res = 0
        for key, val in self.freq_num1.items():
            res += val * self.freq_num2.get(tot - key, 0)
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

import unittest

class TestFindSumPairs(unittest.TestCase):
    def setUp(self):
        self.obj = FindSumPairs([1,1,2,2,2,3],[1,4,5,2,5,4])

    def testcase1(self):
        result = []
        result.append(self.obj.count(7))
        result.append(self.obj.add(3,2))
        result.append(self.obj.count(8))
        result.append(self.obj.count(4))
        result.append(self.obj.add(0,1))
        result.append(self.obj.add(1,1))
        result.append(self.obj.count(7))
        self.assertEqual(result,[8,None,2,1,None,None,11])

    def testcase2(self):
        result = []
        result.append(self.obj.count(6))
        result.append(self.obj.add(3,1))
        result.append(self.obj.count(6))
        result.append(self.obj.count(4))
        result.append(self.obj.add(0,1))
        result.append(self.obj.add(1,1))
        result.append(self.obj.add(0, 1))
        result.append(self.obj.count(6))
        self.assertEqual(result,[10,None,11,3,None,None,None,11])

    def tearDown(self):
        del self.obj
