# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d_pre = {val: ind for ind, val in enumerate(preorder)}
        d_post = {val: ind for ind, val in enumerate(postorder)}

        def helper(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            elif pre_start == pre_end:
                return TreeNode(preorder[pre_start])
            else:
                node = TreeNode(preorder[pre_start])
                node.left = helper(pre_start + 1, d_pre[postorder[post_end - 1]] - 1, post_start,
                                   d_post[preorder[pre_start + 1]])
                node.right = helper(d_pre[postorder[post_end - 1]], pre_end, d_post[preorder[pre_start + 1]] + 1,
                                    post_end - 1)
                return node

        return helper(0, len(preorder) - 1, 0, len(postorder) - 1)

