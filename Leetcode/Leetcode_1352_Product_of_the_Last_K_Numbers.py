class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.size = 0
        self.lastzero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.products.append(self.products[-1] * 1)
            self.lastzero = self.size
        else:
            self.products.append(self.products[-1] * num)
        self.size += 1

    def getProduct(self, k: int) -> int:
        if self.size - k <= self.lastzero:
            return 0
        return self.products[-1] // self.products[self.size - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

