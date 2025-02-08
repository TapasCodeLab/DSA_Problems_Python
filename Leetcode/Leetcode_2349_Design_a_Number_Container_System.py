import heapq

class NumberContainers:

    def __init__(self):
        self.index_map = {}
        self.data_map = {}

    def change(self, index: int, number: int) -> None:
        self.index_map[index] = number
        if number not in self.data_map:
            self.data_map[number] = []
        heapq.heappush(self.data_map[number], index)

    def find(self, number: int) -> int:
        if number not in self.data_map:
            return -1
        else:
            while self.data_map[number]:
                x = self.data_map[number][0]
                if self.index_map[x] == number:
                    return x
                heapq.heappop(self.data_map[number])
            return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)