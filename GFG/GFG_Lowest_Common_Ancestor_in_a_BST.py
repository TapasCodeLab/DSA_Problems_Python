'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    def LCA(self, root, n1, n2):
        def getPath(node, val):
            if not node:
                return []
            elif node.data == val.data:
                return [node]
            else:
                left = getPath(node.left, val)
                right = getPath(node.right, val)
                left.extend(right)
                if len(left) >= 1:
                    left.append(node)
                return left[:]

        path1 = getPath(root, n1)
        path2 = getPath(root, n2)

        path1 = path1[::-1]
        path2 = path2[::-1]
        LCA = None
        i = 0
        while i<len(path1) and i<len(path2):
            if path1[i] == path2[i]:
                LCA = path1[i]
            else:
                break
            i+=1

        return LCA



# your code here


# {
# Driver Code Starts
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
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    q = deque()

    # Push the root to the queue
    q.append(root)

    # Starting from the second element
    i = 1
    while len(q) > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
        i += 1
    return root


def searchBSTRecursive(root, num):
    if root is None or root.data == num:
        return root  # Found the node or reached a null node

    if num < root.data:
        return searchBSTRecursive(root.left, num)  # Search in left subtree
    else:
        return searchBSTRecursive(root.right, num)  # Search in right subtree


if __name__ == "__main__":
    t = 1 # int(input())
    ob = Solution()
    for _ in range(t):
        s = input("Enter tree elements (N for Nulls): ")
        root = buildTree(s)

        # Read n1 and n2 from two separate lines
        x = int(input("First node value: "))
        y = int(input("Second node value: "))
        n1 = searchBSTRecursive(root, x)
        n2 = searchBSTRecursive(root, y)
        print(ob.LCA(root, n1, n2).data)
        print("~")

# } Driver Code Ends