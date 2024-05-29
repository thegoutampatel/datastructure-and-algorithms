
def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


#driver code 
arr = [70,50,20,30,90,5,15] 
result = SelectionSort(arr)  
print("The Arry after Selection sort : ",result)