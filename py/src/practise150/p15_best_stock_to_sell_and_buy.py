"""
You are given an integer array prices where prices[i] is the price of stock on the ith day.
You may choose a single day to buy one stock and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Eg:
    Input: prices = [10,1,5,6,7,1]
    Output: 6
"""


class Solution:
    def max_profit(self, prices):
        maxProfit = 0

        for i in range(1, len(prices)):
            j = i - 1
            while j > -1:
                maxProfit = max(maxProfit, prices[i] - prices[j])
                j -= 1

        return maxProfit

    def max_profit2(self, prices):
        '''
        Two pointer algorithm
        time: O(n)
        space: O(1)
        '''
        maxProfit = 0

        i, j = 0, 1

        while j < len(prices):
            if prices[j] > prices[i]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
            else:
                i = j
            j += 1

        return maxProfit
