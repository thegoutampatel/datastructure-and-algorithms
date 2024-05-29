import heapq

def kth_Smallest(arr,k):
    heapq.heapify(arr)
    print(arr)

    for _ in range(k-1):
        heapq.heappop(arr)

    return heapq.heappop(arr)


#driver code 
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 50
result = kth_Smallest(arr,k)
print(result)