# https://www.geeksforgeeks.org/problems/construct-tree-1/1

# User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''


# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        d = {val: ind for ind, val in enumerate(inorder)}

        def helper(in_start, in_end, pre_start, pre_end):
            if in_end < in_start:
                return None
            node = Node(preorder[pre_start])
            i = d[preorder[pre_start]]
            p = i - in_start
            node.left = helper(in_start, i - 1, pre_start + 1, pre_start + p)
            node.right = helper(i + 1, in_end, pre_start + p + 1, pre_end)
            return node

        root = helper(0, len(inorder) - 1, 0, len(preorder) - 1)
        return root


# {
# Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        inorder = [int(x) for x in input("Enter inorder tree nodes (N for null): ").split()]
        preorder = [int(x) for x in input("Enter preorder tree nodes (N for null): ").split()]

        root = Solution().buildTree(inorder, preorder)
        print("Post order is :")
        printPostorder(root)
        print()

# } Driver Code Ends