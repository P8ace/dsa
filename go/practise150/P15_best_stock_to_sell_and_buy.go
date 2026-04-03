package practise150

// You are given an integer array prices where prices[i] is the price of stock on the ith day.
// You may choose a single day to buy one stock and choose a different day in the future to sell it.
// Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

// Eg:
//     Input: prices = [10,1,5,6,7,1]
//     Output: 6

func MaxProfit(prices []int) int {
	i := 0
	j := 1
	maxProfit := 0

	for j < len(prices) {
		if prices[j] > prices[i] {
			maxProfit = max(maxProfit, prices[j]-prices[i])
		} else {
			i = j
		}
		j++
	}
	return maxProfit
}
