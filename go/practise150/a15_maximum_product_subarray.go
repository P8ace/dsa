package practise150

func MaximumProductSubarray(nums []int) int {
	prefix, suffix := 1, 1
	maxproduct := nums[0]

	for i, _ := range nums {
		prefix *= nums[i]
		suffix *= nums[len(nums)-i-1]

		maxproduct = max(maxproduct, max(prefix, suffix))
		if prefix == 0 {
			prefix = 1
		}
		if suffix == 0 {
			suffix = 1
		}
	}
	return maxproduct
}
