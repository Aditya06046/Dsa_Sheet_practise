import heapq
def kthLargest(l ,k):
    pq = []
    heapq.heapify(pq)
    for i in l:
        heapq.heappush(pq,i)
        if len(pq) > k:
            heapq.heappop(pq)
    return pq[0]
# input
l = [1,3,54,6,64,634,434,66,4,43]
k = int(input())
print(f"{k}th maximum of list is:",kthLargest(l,k))        
