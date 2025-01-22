#https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
# User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        # code here
        def reverse(head):
            rh = None
            while head:
                temp = head
                head = head.next
                temp.next = rh
                rh = temp
            return rh

        num1 = reverse(num1)
        num2 = reverse(num2)
        head, tail = None, None
        total, carry = 0, 0
        while num1 or num2:
            x = num1.data if num1 else 0
            y = num2.data if num2 else 0
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
            total = x + y + carry
            carry = total//10
            node = Node(total %10)
            if not head:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next

        if carry:
            node = Node(carry)
            tail.next = node

        head = reverse(head)

        while head.data == 0:
            head = head.next

        return head





# {
# Driver Code Starts
# Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input("Enter number of testcases: "))):

        arr1 = (int(x) for x in input("Enter the first list: ").split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input("Enter the second list: ").split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends