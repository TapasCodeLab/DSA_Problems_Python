# https://www.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1

'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''


class Solution:
    def sumOfLongRootToLeafPath(self, root):
        # code here
        def helper(node):
            if not node:
                return 0, 0
            else:
                left_len, left_sum = helper(node.left)
                right_len, right_sum = helper(node.right)
                if left_len > right_len:
                    return left_len + 1, left_sum + node.data
                elif left_len < right_len:
                    return right_len + 1, right_sum + node.data
                else:
                    return right_len + 1, max(right_sum, left_sum) + node.data

        return helper(root)[1]