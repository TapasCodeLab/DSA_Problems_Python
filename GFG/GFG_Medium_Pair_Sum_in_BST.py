# https://www.geeksforgeeks.org/problems/find-a-pair-with-given-target-in-bst/1
'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

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

class Solution:
    def findTarget(self, root, target):
        # your code here.
        self.array = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            self.array.append(node.data)
            helper(node.right)

        helper(root)
        i, j = 0, len(self.array ) -1
        while i< j:
            if self.array[i] + self.array[j] == target:
                return True
            elif self.array[i] + self.array[j] > target:
                j -= 1
            else:
                i += 1

        return False


# your code here.

# {
# Driver Code Starts.
if __name__ == "__main__":
    t = 1
    for _ in range(0, t):
        s = input("Enter tree elements (N for None): ")
        summ = int(input("Enter sum value: "))
        root = buildTree(s)
        ans = Solution().findTarget(root, summ)
        if (ans == False):
            print(0)
        else:
            print(1)
        print("~")
# } Driver Code Ends