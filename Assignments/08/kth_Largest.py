import heapq

def kth_Largest(arr,k):
    max_heap = [-num for num in arr]
    heapq.heapify(max_heap)
    print(max_heap)

    for _ in range(k-1):
        heapq.heappop(max_heap)

    return -heapq.heappop(max_heap)


#driver code 
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = kth_Largest(arr,k)
print(result)