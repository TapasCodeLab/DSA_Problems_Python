# function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""


class Solution:
    def reverseList(self, head):
        # Code here
        reversed_head = None
        while head:
            temp = head
            head = head.next
            temp.next = reversed_head
            reversed_head = temp

        return reversed_head


# {
# Driver Code Starts
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()

if __name__ == '__main__':
    #for i in range(int(input())):
    for i in range(1):
        #arr = [int(x) for x in input().split()]
        arr = [1, 2, 3, 4]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().reverseList(lis.head)
        printList(newHead)
        print("~")

# } Driver Code Ends