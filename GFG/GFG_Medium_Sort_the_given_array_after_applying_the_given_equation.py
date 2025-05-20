#https://www.geeksforgeeks.org/problems/sort-the-given-array-after-applying-the-given-equation0304/1
class Solution:
    def sortArray(self, arr, A, B, C):
        # Code here
        def func(x, a, b, c):
            return ((a * x * x) + (b * x) + c)

        res = [func(n, A, B, C) for n in arr]
        res.sort()
        return res


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        a = int(input())
        b = int(input())
        c = int(input())

        ob = Solution()
        ans = ob.sortArray(arr, a, b, c)
        print(' '.join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends