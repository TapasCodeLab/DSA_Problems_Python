from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        tree = {i: [] for i in range(n)}
        for s, d in edges:
            tree[s].append(d)
            tree[d].append(s)
        # print(tree)

        # path from bob to root
        def dfsrt(bob, path):
            if self.visited[bob] == 0:
                path.append(bob)
                self.visited[bob] = 1
                if bob == 0:
                    return path[:]
                elif not tree[bob]:
                    return
                else:
                    for node in tree[bob]:
                        lst = dfsrt(node, path[:])
                        if lst:
                            return lst

        def dfs(node, step, total):
            if self.visited[node] == 0:
                self.visited[node] = 1
                if node in self.path and self.path.index(node) > step:
                    total += amount[node]
                elif node in self.path and self.path.index(node) == step:
                    total += amount[node] // 2
                elif node in self.path and self.path.index(node) < step:
                    total += 0
                else:
                    total += amount[node]
                if len(tree[node]) == 1:
                    self.res = max(self.res, total)
                    return
                else:
                    for nxt in tree[node]:
                        dfs(nxt, step + 1, total)

        self.res = -float('inf')
        self.visited = [0 for _ in range(n)]
        self.path = dfsrt(bob,[])
        print(self.path)
        self.visited = [0 for _ in range(n)]
        dfs(0,0,0)
        return self.res


s = Solution()
print(s.mostProfitablePath([[0,2],[0,4],[1,3],[1,2]],1,[3958,-9854,-8334,-9388,3410]))