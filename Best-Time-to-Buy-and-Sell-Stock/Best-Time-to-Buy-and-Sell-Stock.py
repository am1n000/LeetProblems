class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]

        for p in prices:
            if profit < p - lowest:
                profit = p - lowest
            if lowest > p:
                lowest = p
        return profit 