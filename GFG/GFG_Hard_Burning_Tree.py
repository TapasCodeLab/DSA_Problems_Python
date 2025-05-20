# https://www.geeksforgeeks.org/problems/burning-tree/1
from collections import deque

class Solution:
    def minTime(self, root, target):
        # code here
        nodes = set()
        queue = deque([root])
        adj = {}

        while queue:
            node = queue.popleft()
            nodes.add(node.data)
            if node.data not in adj:
                adj[node.data] = []

            if node.left:
                queue.append(node.left)
                if node.data in adj:
                    adj[node.data].append(node.left.data)
                else:
                    adj[node.data] = [node.left.data]
                if node.left.data in adj:
                    adj[node.left.data].append(node.data)
                else:
                    adj[node.left.data] = [node.data]

            if node.right:
                queue.append(node.right)
                if node.data in adj:
                    adj[node.data].append(node.right.data)
                else:
                    adj[node.data] = [node.right.data]
                if node.right.data in adj:
                    adj[node.right.data].append(node.data)
                else:
                    adj[node.right.data] = [node.data]

        time = -1
        queue.append(target)
        nodes.remove(target)
        while queue:
            time += 1
            # print(time, queue)
            for i in range(len(queue)):
                node = queue.popleft()
                for nxt in adj[node]:
                    if nxt in nodes:
                        nodes.remove(nxt)
                        queue.append(nxt)

        return time

