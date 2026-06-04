class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        res = 0
        while right <= len(prices) - 1:
             
            comp = prices[right] - prices[left]
            if comp > res:
                res = comp
            if prices[left] > prices[right]:
                left = right
            
            right +=1
        return res