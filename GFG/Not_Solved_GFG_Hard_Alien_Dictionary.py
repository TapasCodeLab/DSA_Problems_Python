# https://www.geeksforgeeks.org/problems/alien-dictionary/1
# User function Template for python3
class Solution:
    def findOrder(words):
        # code here
        from collections import deque
        def compare(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] == word2[i]:
                    continue
                else:
                    return [word1[i], word2[i]]
            return [None, None]

        letters = set()
        for word in words:
            for ch in word:
                letters.add(ch)

        indegree = {letter: 0 for letter in letters}
        adj = {letter: [] for letter in letters}
        queue = deque([])
        total = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                ch1, ch2 = compare(words[i], words[j])
                if ch1:
                    indegree[ch2] += 1
                    adj[ch1].append(ch2)
                    total += 1

        for k, v in indegree.items():
            if v == 0:
                queue.append(k)

        res = ''
        while queue:
            ch = queue.popleft()
            res = res + ch
            for nxt in adj[ch]:
                indegree[nxt] -= 1
                total -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        if total == 0:
            return res
        else:
            return ""

    print(findOrder(["baa", "abcd", "abca", "cab", "cad"]))
    print(findOrder(["caa", "aaa", "aab"]))
    print(findOrder(["ab", "cd", "ef", "ad"]))
