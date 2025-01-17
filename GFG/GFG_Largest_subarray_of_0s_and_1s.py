class Solution:
    def maxLen(self, arr):
        # code here
        d = {(0, 0): -1}
        res = 0
        total = [0, 0]
        for i in range(len(arr)):
            a = arr[i]
            if a == 0:
                if total[1] > 0:
                    total[1] -= 1
                else:
                    total[0] += 1
            else:
                if total[0] > 0:
                    total[0] -= 1
                else:
                    total[1] += 1

            if (total[0], total[1]) in d:
                res = max(res, i - d[(total[0], total[1])])
            else:
                d[(total[0], total[1])] = i

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxLen([1, 0, 1, 1, 1, 0, 0])==6)
    print(s.maxLen([0, 0, 1, 1, 0]) == 4)
    print(s.maxLen([0]) == 0)
    print(s.maxLen([1,1,1]) == 0)
