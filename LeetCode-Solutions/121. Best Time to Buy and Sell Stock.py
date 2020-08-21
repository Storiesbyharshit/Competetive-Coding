class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == [] or len(prices) == 0:
            return 0
        else:
            minval = prices[0]
            maxdiff = 0
            
            for i in prices :
                minval = min(i,minval)
                localdiff =  i - minval
                maxdiff = max(localdiff,maxdiff)
                
        return maxdiff
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0
        buy = math.inf
        sell = 0
        days = len(prices)
        for i in range(days):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > Max:
                Max = prices[i] - buy
        return Max     
