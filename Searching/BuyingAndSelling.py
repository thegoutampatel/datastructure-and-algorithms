prices = [7,1,5,3,6,4]

def BestTime(prices):
    maxProfit = 0
    minPrice = float("inf")

    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i]-minPrice
        
    return maxProfit

bestTime = BestTime(prices)
print(bestTime)            