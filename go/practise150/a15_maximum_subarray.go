package practise150

// Given an array of integers nums, find the subarray with the largest sum and return the sum.

func MaximumSubarray(nums []int) int {
	sum := 0
	maxsum := -1001

	for _, n := range nums {
		sum += n
		maxsum = max(sum, maxsum)
		if sum < 0 {
			sum = 0
		}
	}
	return maxsum
}
