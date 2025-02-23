# https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1
# User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''


class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        def mergeTwoLists(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            dummy = Node(0)
            head = dummy
            while list1 and list2:
                if list1.data < list2.data:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
                head.next = None
            if list1:
                head.next = list1
            if list2:
                head.next = list2
            return dummy.next

        while len(arr) > 1:
            new_arr = []
            for i in range(0, len(arr), 2):
                list1 = arr[i]
                list2 = arr[i + 1] if i + 1 < len(arr) else None
                new_arr.append(mergeTwoLists(list1, list2))
            arr = new_arr[:]

        return arr[0]


# {
# Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = 1 # int(input())
    for _ in range(t):
        n = int(input("Enter number of linked lists : "))
        lists = []
        for _ in range(n):
            values = list(map(int, input("Enter link list elements: ").split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends