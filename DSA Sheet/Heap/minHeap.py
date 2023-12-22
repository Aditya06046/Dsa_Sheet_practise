from heapq import heapify ,heappop,heappush
# heapify ,heappop,heappush,heapreplace
class minheap:
    
    def __init__(self) -> None:
        self.heap = []
    def parent(self, i):
        return (i-1)//2
    def lChild(self, i):
        return 2*i+1
    def rChild(self,i):
        return 2*i+2
    def decreseKey(self,i):
        self.heap[i] = float('-inf')
        while i!= 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)] , self.heap[i]
    def deleteKey(self, i):
        self.decreseKey(i)
        heappop(self.heap)
        self.heap.pop(0)
    def InsertNode(self, key):
        heappush(self.heap , key)
    def display(self):
        print(self.heap)
h = minheap()
h.InsertNode(1)        
h.InsertNode(3)        
h.InsertNode(5)        
h.InsertNode(7)        
h.InsertNode(12)
h.display()        
print(h.deleteKey(3))
h.display()
    