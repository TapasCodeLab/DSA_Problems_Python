# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.nodes = [0]
        self.index = 0

        def convert(traversal):
            if not traversal:
                return
            elif traversal[0] == '-':
                cnt = 0
                while traversal[cnt] == '-':
                    cnt += 1
                self.nodes.append(cnt)
                convert(traversal[cnt:])
            else:
                number, i = 0, 0
                while i < len(traversal) and traversal[i] != '-':
                    number = number * 10 + int(traversal[i])
                    i += 1
                self.nodes.append(number)
                convert(traversal[i:])

        def helper(level):
            if self.index >= len(self.nodes):
                return None
            lvl, val = self.nodes[self.index], self.nodes[self.index + 1]
            if lvl == level:
                node = TreeNode(val)
                self.index += 2
                node.left = helper(level + 1)
                if self.index < len(self.nodes):
                    node.right = helper(level + 1)
                return node
            return None

        convert(traversal)
        # print(self.nodes)
        root = helper(0)
        return root


