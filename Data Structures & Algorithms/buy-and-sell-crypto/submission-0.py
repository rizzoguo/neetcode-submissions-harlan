class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_price = prices[0]
        for i in prices:
            if cur_price > i:
                cur_price = i 
            else:
                res = max(res, i - cur_price)
        
        return res