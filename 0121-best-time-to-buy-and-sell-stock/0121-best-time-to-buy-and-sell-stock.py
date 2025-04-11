class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -float("inf")
        min_buy = float("inf")

        n = len(prices)
        for x in range(1,n):
            min_buy = min(min_buy, prices[x-1])
            max_profit = max(max_profit, prices[x]-min_buy)

        if max_profit > 0:
            return max_profit
        return 0
            

        