class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Function to count set bits in a number
        def countSetBits(num):
            ans = 0
            while num > 0:
                if num & 1 == 1:
                    ans += 1
                num = num >> 1
            return ans

        n2 = countSetBits(num2)
        res_bin, res = [0] * 32, 0

        for i in range(31, -1, -1):
            if n2 == 0:
                break
            if (num1 >> i) & 1 == 1:
                res_bin[31 - i] = 1
                n2 -= 1

        for i in range(31, -1, -1):
            if n2 == 0:
                break
            if res_bin[i] == 0:
                res_bin[i] = 1
                n2 -= 1
        for a in res_bin:
            res *= 2
            res += a
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.minimizeXor(3,5)==3)
    print(s.minimizeXor(1, 12) == 3)
    print(s.minimizeXor(8, 12) == 9)
    print(s.minimizeXor(9, 1) == 8)

