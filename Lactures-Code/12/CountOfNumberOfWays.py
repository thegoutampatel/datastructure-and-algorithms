def PossibleWays(n):
    if n==2:
        return 2
    elif n == 1:
        return 1
    else:
        return PossibleWays(n-1) + PossibleWays(n-2)


#driver code 

n = int(input("Enter Number :"))
result = PossibleWays(n)
print("Total Number Ways Possible :", PossibleWays(n))

