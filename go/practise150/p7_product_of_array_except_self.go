package practise150

// Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
// Eg: 
//     input       [1,2,3,4],
//     output      [24,12,8,6]

func product_of_array_except_self(nums []int) []int{
	prefix := 1
	postfix := 1
	
	result := make([]int, len(nums))
	for i, _ := range nums{
		result[i] = 1
	}
	
	for i:= 0; i < len(nums); i++ {
		result[i] = prefix
		prefix = prefix * nums[i]
	}
	
	for i := len(nums) - 1; i > -1; i-- {
		result[i] = postfix * result[i]
		postfix = postfix * nums[i]
	}
	
	return result
}