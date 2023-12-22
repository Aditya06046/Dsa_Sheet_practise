# heap tree-based ds
# two types:  minheap maxheap
#  time complexity - O(log(n)) -- insertion() ,deletion() , heapify() 
# stored in array i th childs are in 2*i+1 and 2*i+2 positions
""" applications : priority queue , Binomial heap , Fibonacci heap """
class heap :
    arr = []
    maxSize = 0
    heapSize = 0
    def __init__(self, size) -> None:
        self.maxSize = size
        self.arr = [None]*self.maxSize
        self.heapSize = 0

    def parent(self,i):
        return (i-1)//2
    
    def lChild(self,i):
        return (2*i)+1
    def rChild(self,i):
        return (2*i)+2
    
    def Heapify(self, i):
        l = self.lChild(i) 
        r = self.rChild(i)
        largest = i
        if l < self.heapSize and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.Heapify(largest)

    def increaseKey(self, i):
        self.arr[i] = float("inf")
        while i != 0 and self.arr[self.parent(i)] < self.arr[i] :
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
    
    def deleteKey(self , key):
        
        if self.heapSize == 0:
            return "None"
        if self.heapSize == 1:
            self.heapSize -=1
            return self.arr[0]
        self.increaseKey(key)
        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize-1]
        self.arr[self.heapSize-1] = None  
        self.heapSize -= 1
        self.Heapify(0)
        return root
    
    def InsertNode(self ,val):
        #base case
        if self.heapSize == self.maxSize :
            print("Overflow ---heap")
            return 
        self.heapSize +=1
        i = self.heapSize -1
        self.arr[i] = val
        while i!= 0 and self.arr[self.parent(i)] < self.arr[i] :
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
    def display(self):
        for i in range(self.heapSize):
            print(self.arr[i],end=" ")
    
h = heap(5)
h.InsertNode(1)        
h.InsertNode(3)        
h.InsertNode(5)        
h.InsertNode(7)        
h.InsertNode(12)
h.display()        
print(h.deleteKey(3))
h.display()