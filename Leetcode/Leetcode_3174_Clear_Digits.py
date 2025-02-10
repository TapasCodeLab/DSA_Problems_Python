class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ord('a')<=ord(ch)<=ord('z'):
                stack.append(ch)
            else:
                stack.pop()
        return ''.join(stack)