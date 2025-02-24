# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        # write code here
        stack = [[float('inf'), -1]]
        res = []
        for ind, val in enumerate(arr):
            while val >= stack[-1][0]:  # while stack not required as val < float('inf')
                stack.pop()
            res.append(ind - stack[-1][1])
            stack.append([val, ind])

        return res


# {
# Driver Code Starts.
# Initial Template for Python 3

if __name__ == "__main__":
    t = 1
    while t > 0:
        arr = list(map(int, input("Enter array elements: ").split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends