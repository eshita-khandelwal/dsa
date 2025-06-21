class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPrice = prices[0]

        for i in range(1,len(prices)):
            if prices[i]<lowestPrice:
                lowestPrice = prices[i]
            if maxProfit < prices[i]-lowestPrice:
                maxProfit = prices[i]-lowestPrice
        return maxProfit