def isPerfectSquare(num):
    if num<=2:
        return True
    
    left,right = 2,num // 2

    while left<=right:
        mid = left + (right-left)//2
        square = mid*mid

        if square == num:
            return True
        elif num<square:
            right = mid-1
        else:
            left = mid+1

    return False


#Driver Code 
num = int(input("Enter Number :"))
result = isPerfectSquare(num)
print(result)