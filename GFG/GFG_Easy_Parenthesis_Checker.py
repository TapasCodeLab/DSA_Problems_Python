# https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1

class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            elif stack and ch == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and ch == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and ch == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return not stack


# {
# Driver Code Starts
# Initial Template for Python 3



if __name__ == '__main__':
    test_cases = 1 # int(input())
    for cases in range(test_cases):
        s = str(input("Enter the parentheses: "))
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends