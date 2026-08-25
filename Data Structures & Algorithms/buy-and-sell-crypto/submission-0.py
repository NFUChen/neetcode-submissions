class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy = 0
        sell = 0
        while (sell < len(prices)):
            if prices[sell] > prices[buy]:
                p = prices[sell] - prices[buy]
                max_p = max(p, max_p)
            else:
                buy = sell
            sell += 1
        
        return max_p
            