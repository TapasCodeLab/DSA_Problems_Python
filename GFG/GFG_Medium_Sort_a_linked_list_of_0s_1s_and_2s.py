# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''


class Solution:
    def segregate(self, head):
        # code here
        zero_start, zero_end = None, None
        one_start, one_end = None, None
        two_start, two_end = None, None

        while head:
            if head.data == 0:
                if zero_end:
                    zero_end.next = head
                    zero_end = zero_end.next
                else:
                    zero_start = head
                    zero_end = head
            elif head.data == 1:
                if one_end:
                    one_end.next = head
                    one_end = one_end.next
                else:
                    one_start = head
                    one_end = head
            elif head.data == 2:
                if two_end:
                    two_end.next = head
                    two_end = two_end.next
                else:
                    two_start = head
                    two_end = head
            head = head.next

        head, tail = None, None
        if zero_start:
            head = zero_start
            tail = zero_end
        elif one_start:
            head = one_start
            tail = one_end
            one_start = None
        elif two_start:
            head = two_start
            tail = two_end
            two_start = None

        if one_start:
            tail.next = one_start
            tail = one_end
        elif two_start:
            tail.next = two_start
            tail = two_end
            two_start = None

        if two_start:
            tail.next = two_start
            tail = two_end

        tail.next = None

        return head


# {
# Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = 1
    for _ in range(t):
        arr = [1,2,1,1,2,0,0,0,1,0]
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))
        print("~")

# } Driver Code Ends