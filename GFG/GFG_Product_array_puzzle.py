class Solution:
    def productExceptSelf(self, arr):
        # code here
        res = []
        total = 1
        for i in range(len(arr)):
            res.append(total)
            total *= arr[i]
        total = 1
        for i in range(len(arr) - 1, -1, -1):
            res[i] *= total
            total *= arr[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([10, 3, 5, 6, 2])==[180, 600, 360, 300, 900])
    print(s.productExceptSelf([12, 0]) == [0, 12])

