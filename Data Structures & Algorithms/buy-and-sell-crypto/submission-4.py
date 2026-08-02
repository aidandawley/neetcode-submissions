class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        res = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            res = max(profit, res)

            if prices[left] > prices[right]:
                left = right
            
            right += 1
        return res