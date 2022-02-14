class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        if n == 1:
            return 0
        last_buy = -prices[0]
        last_sold = 0
        for i in range(n):
            current_buy = max(last_buy, last_sold - prices[i])
            current_sold = max(last_sold, last_buy + prices[i]-fee)
            last_buy = current_buy
            last_sold = current_sold
        return last_sold