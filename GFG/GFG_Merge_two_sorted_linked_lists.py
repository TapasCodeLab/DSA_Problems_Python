# https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1

# User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        head = None
        tail = None
        temp = None
        while head1 and head2:
            if head1.data <= head2.data:
                temp = head1
                head1 = head1.next
                temp.next = None
            else:
                temp = head2
                head2 = head2.next
                temp.next = None

            if not head:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return head


# {
# Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input("Enter number of test cases: "))
    for _ in range(T):
        input1 = list(map(int, input("Enter first shorted list:").split()))
        input2 = list(map(int, input("Enter second shorted list:").split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends