class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = 0
        pivot = prices[len(prices) - 1]
        for i in range (len(prices) - 2, -1, -1):
            max1 = max(max1,(pivot - prices[i]))
            pivot = max(pivot, prices[i])
        return max1


        