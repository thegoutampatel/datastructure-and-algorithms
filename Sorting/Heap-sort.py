# This is from scratch
#we can sort this directly by importing heapq
def buildHeap(arr,n):
    startIndex = n//2 - 1

    for i in range(startIndex,-1,-1):
        def heapify(arr,n,i):
            smallest = i
            l = 2*i+1
            r = 2*i+2
            if arr[l]<arr[smallest]:
                i = l
            elif arr[r]<arr[smallest]:
                i = r
            heapify(arr,n,smallest)

    return arr

arr = [40, 25, 68, 79, 52, 66, 89, 97]
n = len(arr)
result = buildHeap(arr,n)
print(result)