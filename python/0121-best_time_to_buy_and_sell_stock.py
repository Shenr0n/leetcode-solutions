class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        length = len(prices) - 1
        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price > buy and (price-buy) >= maxProfit:
                maxProfit = price-buy
        return maxProfit
