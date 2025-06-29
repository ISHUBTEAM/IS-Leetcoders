# prices = [7,1,5,3,6,4] #5
# prices = [7,6,4,3,1] #0
prices = [1] #0

''' this method for the first two cases worked but for one array not working'''
# lowest = min(prices)
# smallest = prices[0]
# for i in range(1, len(prices)):
#     if i < smallest:
#         smallest = i
        
# max = prices[0]
# for j in range(prices[smallest], len(prices)):
#     if max < j:
#         max = j        
# print(max)

# ============= The Answer ==================

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minProfit = float('inf')
        maxProfit = 0

        for i in prices:
            minProfit = min(i, minProfit)
            maxProfit = max(maxProfit, i - minProfit)
            
        return maxProfit