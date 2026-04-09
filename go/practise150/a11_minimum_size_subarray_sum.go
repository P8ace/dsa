package practise150

// You are given an array of positive integers nums and a positive integer target,
// return the minimal length of a subarray whose sum is greater than or equal to target.
// If there is no such subarray, return 0 instead.

func MinSubarraySum(nums []int, target int) int {
	i, j := 0, 0
	sum, length := 0, len(nums)+100

	for j < len(nums) {
		sum += nums[j]
		for sum >= target {
			length = min(length, j-i+1)
			sum -= nums[i]
			i++
		}
		j++
	}

	if length == len(nums)+100 {
		return 0
	}
	return length
}
