package practise150

// You are given an array of integers nums and an integer k,
// return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

func Nosubarrayproductlessthank(nums []int, k int) int {
	i, j := 0, 0
	product := 1
	result := 0

	for j < len(nums) {
		product *= nums[j]
		for i <= j && product >= k {
			product /= nums[i]
			i++
		}
		result += j - i + 1
		j++
	}
	return result
}
