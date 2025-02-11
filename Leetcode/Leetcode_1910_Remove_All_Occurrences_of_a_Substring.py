class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for ch in s:
            stack.append(ch)
            if len(stack)>=n and ''.join(stack[-n:]) == part:
                stack = stack[:-n]

        return ''.join(stack)
