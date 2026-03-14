# Definition for a binary tree node.
import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def findSum(node, total):
            if not node:
                return
            total = (total*2)+node.val
            if node.left or node.right:
                if node.left:
                    findSum(node.left, total)
                if node.right:
                    findSum(node.right, total)
            else:
                self.res +=  total

        findSum(root, 0)
        return self.res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.node4 = TreeNode(0)
        self.node5 = TreeNode(1)
        self.node6 = TreeNode(0)
        self.node7 = TreeNode(1)
        self.node2 = TreeNode(0,self.node4,self.node5)
        self.node3 = TreeNode(1,self.node6,self.node7)
        self.node1 = TreeNode(1,self.node2,self.node3)

    def testcase1(self):
        ans = self.solution.sumRootToLeaf(root=self.node1)
        self.assertEqual(ans,22)

    def testcase2(self):
        node = TreeNode(0)
        ans = self.solution.sumRootToLeaf(root=node)
        self.assertEqual(ans,0)

    def testcase3(self):
        ans = self.solution.sumRootToLeaf(root=None)
        self.assertEqual(ans,0)

    def tearDown(self):
        pass

