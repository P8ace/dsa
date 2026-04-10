package practise150

// You are given an array of integers nums, calculate the pivot index of this array.

// The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

// If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

// Return the leftmost pivot index. If no such index exists, return -1.

func PivotIndex(nums []int) int {
	total := 0
	for _, n := range nums {
		total += n
	}
	
	leftsum := 0
	for i, num := range nums {
		rightsum := total - leftsum - num
		if rightsum == leftsum {
			return i
		}
		leftsum += num
	}
	return -1
}