package practise150

// You are given an array arr[] of non-negative integers. 
// You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. 
// The operation must be performed in place, meaning you should not use extra space for another array.

func MoveZeroes(nums []int){
	l, r:= 0,0
	
	for r < len(nums) {
		if nums[r] != 0 {
			nums[l], nums[r] = nums[r], nums[l]
			l++
		}
		r++
	}
}