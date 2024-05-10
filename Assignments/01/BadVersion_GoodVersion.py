# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, 
# all the versions after a bad version are also bad. Suppose you have n version 
# and you want to find out the first bad one, which causes all the following ones 
# to be bad. Also, talk about the time complexity of your code.

# Test Cases:
# Input: [0,0,0,1,1,1,1,1,1]
# Output: 3
# Explanation: 0 indicates a good version and 1 indicates a bad version. So, 
# the index of the first 1 is at 3.
#  Thus, the output is 3


def GoodBadVersion(arr,i,j,x):
    while i<=j:
        mid = i + (j-i) // 2

        if arr[mid] == x:
            if arr[mid-1] != x:
                return mid
            else:
                return GoodBadVersion(arr,i,mid-1,x)
        elif arr[mid] != x:
            if arr[mid+1] == 1:
                return mid+1
            else:
                return GoodBadVersion(arr,mid+1,j,x)
    return -1

#driver code 
arr = [0,0,0,0,1,1,1,1,1,1]
j = len(arr) - 1
x = 1
i = 0

result = GoodBadVersion(arr,i,j,x)
print("The index of Fist Bad Version :" , result)
