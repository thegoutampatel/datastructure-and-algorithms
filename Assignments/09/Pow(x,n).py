# Pow(x,n) (Facebook)
# 3. Implement pow(x,n) which calculates x raised to the power n (i.e. x^n)
# For example: x = 2.00000, n = -2 Output: 0.25000
# Explanation: 2^-2 =1⁄2^2 = 1⁄4 = 0.25

def Power(x,n):
    if n == 0:
        return 1
    elif x < 0:
        return 1 / x
    
    halfP = Power(x, n//2)
    
    if n % 2 == 0:
        return halfP * halfP
    else:
        return halfP * halfP * x 
    

#drivercode 
n = 15
x = 2

result = Power(x,n)
print(result)

