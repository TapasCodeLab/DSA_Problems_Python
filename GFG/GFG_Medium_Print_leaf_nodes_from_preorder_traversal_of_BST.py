# https://www.geeksforgeeks.org/problems/print-leaf-nodes-from-preorder-traversal-of-bst2657/1
class Solution:
    def leafNodes(self, preorder):
        # code here
        self.leaf = []
        def helper(start ,end):
            if start >end:
                return
            if start==end:
                self.leaf.append(preorder[start])
                return
            else:
                node = preorder[start]
                s1 ,s2 ,e2 = start +1 ,start +1 ,end
                while s2<=e2 and preorder[s2]<node:
                    s2 += 1
                helper(s1 ,s2-1)
                helper(s2 ,e2)

        helper(0 ,len(preorder ) -1)
        return self.leaf


import unittest

class TestClass(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.leafNodes([5, 2, 10]),[2, 10])

    def testcase2(self):
        self.assertEqual(self.solution.leafNodes([5]),[5])

    def testcase3(self):
        self.assertEqual(self.solution.leafNodes([8, 2, 5, 10, 12]),[5, 12])

    def testcase4(self):
        self.assertEqual(self.solution.leafNodes([4, 2, 1, 3, 6, 5]),[1,3,5])

    def testcase5(self):
        self.assertEqual(self.solution.leafNodes([1, 2, 3, 4]),[4])

    def testcase6(self):
        self.assertEqual(self.solution.leafNodes([4, 3, 2, 1]),[1])

    def tearDown(self):
        pass
