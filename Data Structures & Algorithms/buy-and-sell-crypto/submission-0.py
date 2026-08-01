class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit=0

        for h in range(1,len(prices)):
            if prices[h] > prices[l]:
                currentP = prices[h]-prices[l]
                profit=max(profit,currentP)
            else:
                l=h
        return profit