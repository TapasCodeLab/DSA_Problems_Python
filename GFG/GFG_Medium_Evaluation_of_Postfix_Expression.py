#https://www.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1

# {
# Driver Code Starts
# Initial Template for Python 3


# } Driver Code Ends


class Solution:
    def evaluate(self, arr):
        # code here
        stack = []

        for ch in arr:
            if ch == '+':
                y = stack.pop()
                x = stack.pop()
                stack.append(x + y)
            elif ch == '-':
                y = stack.pop()
                x = stack.pop()
                stack.append(x - y)
            elif ch == '*':
                y = stack.pop()
                x = stack.pop()
                stack.append(x * y)
            elif ch == '/':
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x / y))
            else:
                stack.append(int(ch))

        return stack[0]


# {
# Driver Code Starts.

if __name__ == "__main__":
    t = 1 # int(input())
    for _ in range(t):
        arr = input("Enter postfix expression:").split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends