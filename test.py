class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = set([])
        self.freq = {}

        def backtracking(current, available, length):
            if len(current) == length:
                self.res.add(''.join(current))
            else:
                candidate_list = [key for key, val in available.items() if val>0]
                for candidate in candidate_list:
                    available[candidate] = available.get(candidate)-1
                    current.append(candidate)
                    backtracking(current[:],available,length)
                    current.pop()
                    available[candidate] = available.get(candidate,0)+1

        for tile in tiles:
            self.freq[tile] = self.freq.get(tile,0)+1

        for i in range(1,len(tiles)+1):
            backtracking([], self.freq, i)

        print(self.res)
        return len(self.res)



if __name__ == '__main__':
    s = Solution()
    print(s.numTilePossibilities("AAABBC"))