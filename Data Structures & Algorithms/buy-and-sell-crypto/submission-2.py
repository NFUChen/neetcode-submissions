class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell must greater than buy
        max_p = 0
        buy_day = 0
        for sell_day in range(len(prices)):
            profit = prices[sell_day] - prices[buy_day]
            if profit > 0: # has profit
                max_p = max(max_p, profit)
            else:
                buy_day = sell_day
        
        return max_p
