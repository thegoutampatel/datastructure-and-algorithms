
def BubbleSort(arr):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#driver code 
arr = [70,50,20,30,90,5,15]
result = BubbleSort(arr)
print(result)