class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        start, end = prices[0], prices[0]
        i = 1
        max_profit = 0

        while i < len(prices):
            next_ele = prices[i]

            if next_ele < start:
                start = next_ele
                end = next_ele
            elif next_ele > end:
                end = next_ele

            max_profit = max(max_profit, end-start)
            i+=1

        return max_profit
        