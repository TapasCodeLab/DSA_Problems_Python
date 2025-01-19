# https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1

# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        n = 1
        last = head
        while last.next:
            last = last.next
            n += 1

        k = k % n
        if k == 0:
            return head
        temp = head
        while k - 1:
            temp = temp.next
            k -= 1
        new_head = temp.next
        temp.next = None
        last.next = head
        return new_head


# {
# Driver Code Starts
# Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


# Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys

    # input = sys.stdin.read
    # data = input().splitlines()

    t = 1  # int(data[0].strip())
    idx = 1

    while t > 0:
        arr = [10, 20, 30, 40, 50]  # list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = 3  # int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        print("~")
        t -= 1

# } Driver Code Ends
