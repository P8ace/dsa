package practise150

// Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

// Note: A subarray is a contiguous part of any given array.

func MaxSumofsubarray(nums []int, k int) int {
	i, j := 0, k-1
	maxSum := 0
	for j < len(nums) {
		sum := 0
		l := i
		for l <= j {
			sum += nums[l]
			l++
		}
		maxSum = max(maxSum, sum)
		i++
		j++
	}
	return maxSum
}
func MaxSumofsubarray2(nums []int, k int) int {
	i, j := 0, 0
	maxSum := 0
	sum := 0

	for j < k {
		sum += nums[j]
		j++
	}
	maxSum = sum

	for j < len(nums) {
		sum = sum - nums[i] + nums[j]
		maxSum = max(sum, maxSum)
		i++
		j++
	}
	return maxSum
}
