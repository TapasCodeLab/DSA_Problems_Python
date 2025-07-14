# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        dec = 0
        while head.next:
            dec = (dec * 2) + head.val
            head = head.next
        dec = (dec * 2) + head.val
        return dec


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        a = ListNode(1)
        b = ListNode(0,a)
        self.head = ListNode(1,b)
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.getDecimalValue(self.head), 5)

    def testcase2(self):
        self.head = ListNode(0)
        self.assertEqual(self.solution.getDecimalValue(self.head), 0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

