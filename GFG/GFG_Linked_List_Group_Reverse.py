# https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""


class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        def helper(node):
            pointer = Node(data=None)
            pointer.next = node
            counter = 0
            for i in range(k):
                if pointer.next:
                    pointer = pointer.next
                    counter += 1
                else:
                    break
            if counter == k:
                res_node = reverseList(node, helper(pointer.next))
                return res_node
            else:
                rh = None
                while node:
                    temp = node
                    node = node.next
                    temp.next = rh
                    rh = temp
                return rh
                # return node

        def reverseList(head, next_part):
            prev, curr = next_part, head
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        if not head:
            return None
        elif k == 1:
            return head
        else:
            dummy_head = Node(data=None)
            dummy_head.next = helper(head)
            return dummy_head.next

        # {


# Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input("Enter List Items :").split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input("Enter the value of K: "))  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends