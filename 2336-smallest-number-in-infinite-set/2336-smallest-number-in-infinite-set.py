import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.next_num =  1
        self.heap = []
        self.added = set()

    def popSmallest(self):
        if self.heap:
            num = heapq.heappop(self.heap)
            self.added.remove(num)
            return num

        num = self.next_num
        self.next_num += 1
        return num

    def addBack(self, num):
        if num < self.next_num and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)