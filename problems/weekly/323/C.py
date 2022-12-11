class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.allocated = [0] * n
        

    def allocate(self, size: int, mID: int) -> int:
        if size > self.n:
            return -1

        s = sum(self.allocated[:size])
        if s == 0:
            self.allocated[:size] = [mID] * size
            return 0

        for i in range(1, self.n - size + 1):
            s -= self.allocated[i - 1]
            s += self.allocated[i + size - 1]
            # if sum(self.allocated[i:i+size]) == 0:
            if s == 0:
                self.allocated[i:i+size] = [mID] * size
                return i

        return -1
            
    def free(self, mID: int) -> int:
        num = 0
        for i in range(self.n):
            if self.allocated[i] == mID:
                self.allocated[i] = 0
                num += 1

        return num
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
