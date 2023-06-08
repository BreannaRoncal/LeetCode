"""
Best Time to Buy and Sell Stocks

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 0:
            return max_profit
        else:
            for i in range(1, len(prices)):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit
