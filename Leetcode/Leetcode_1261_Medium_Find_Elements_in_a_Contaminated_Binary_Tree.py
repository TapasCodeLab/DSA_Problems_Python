# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class FindElements:

    def dfs(self, node, val):
        if node:
            self.hashset.add(val)
            self.dfs(node.left, 2 * val + 1)
            self.dfs(node.right, 2 * val + 2)
        else:
            return

    def __init__(self, root: Optional[TreeNode]):
        self.hashset = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.hashset

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


