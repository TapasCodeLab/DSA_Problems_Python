# https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
class Solution:

    def __init__(self):
        # code here
        self.stack = []

    # Add an element to the top of Stack
    def push(self, x):
        # code here
        if not self.stack:
            self.stack.append([x, x])
        else:
            self.stack.append([x, min(x, self.stack[-1][1])])

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if self.stack:
            x, y = self.stack.pop()
            return x

    # Returns top element of Stack
    def peek(self):
        # code here
        if self.stack:
            return self.stack[-1][0]
        return -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        if self.stack:
            return self.stack[-1][1]
        return -1


# {
# Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = 1 #int(input())  # Number of test cases

    for _ in range(t):
        q = int(input("Number of queries: "))  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input("Enter the query: ").split()))

            """
            1 x : Push x onto the stack.
            2 : Pop the top element from the stack.
            3: Return the top element from the stack. If the stack is empty, return -1.
            4: Return the minimum element from the stack.
            """

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends