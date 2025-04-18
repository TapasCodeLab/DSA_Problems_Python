# https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1

# {
# Driver Code Starts
# Initial Template for Python 3

from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


# } Driver Code Ends
# User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    # Return the kth smallest element in the given BST
    def kthSmallest(self, root, k):
        # code here.
        self.position = 0
        self.res = -1

        def helper(node):
            if not node:
                return
            helper(node.left)
            if self.position >= k:
                return
            self.position += 1
            if self.position == k:
                self.res = node.data
                return
            helper(node.right)

        helper(root)
        return self.res


# {
# Driver Code Starts.
# if __name__ == "__main__":
#     t = int(input())
#     for _ in range(0, t):
#         s = input()
#         root = buildTree(s)
#         k1 = int(input())
#         print(Solution().kthSmallest(root, k1))
#
#         print("~")
# } Driver Code Ends

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        root = buildTree('2 1 3')
        k = 2
        self.assertEqual(2,self.solution.kthSmallest(root,k))

    def testcase2(self):
        root = buildTree('2 1 3')
        k = 5
        self.assertEqual(-1,self.solution.kthSmallest(root,k))

    def testcase3(self):
        root = buildTree('20 8 22 4 12 N N N N 10 14')
        k = 3
        self.assertEqual(10, self.solution.kthSmallest(root, k))

    def tearDown(self):
        pass

if __name__ == '__manin__':
    unittest.main()