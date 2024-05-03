num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

n = len(num)

for i in range(0,n):
    if num[i] == 10:
        print("found on index" , i)
        break
    else:
        print("Not Found")