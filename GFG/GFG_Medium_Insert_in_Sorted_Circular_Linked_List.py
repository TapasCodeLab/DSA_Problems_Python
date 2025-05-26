# https://www.geeksforgeeks.org/problems/sorted-insert-for-circular-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortedInsert(self, head, data):
        # code here
        new_node = Node(data)
        temp = head
        if data < head.data:
            while temp.next != head:
                temp = temp.next
            head = new_node
        else:
            while temp.data <= data and temp.next.data <= data and temp.next != head:
                temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        return head

