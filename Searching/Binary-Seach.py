arr = [10,20,30,40,50,60,70,80,90,100]

x = 50
i = 0
j = len(arr)

def BinarySearch(arr,i,j,x):
    while i<=j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return BinarySearch(arr,mid-1,j,x)
        else:
            return BinarySearch(arr,i,mid+1,x)


Binary = BinarySearch(arr,i,j,x)

print("The value is Found on Index :", Binary)
