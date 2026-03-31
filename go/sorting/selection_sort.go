package sorting

// For each index:
//     Set smallest_idx to the current index (of the outer loop)
//     For each index from i + 1 to the end of the list:
//         If the number at the inner loop index is smaller than the number at smallest_idx, set smallest_idx to the inner loop index
//     Swap the number at the outer loop index with the number at smallest_idx
// Return the sorted list

func SelectionSort(nums []int) {
	n := len(nums)

	for i := 0; i < n-1; i++ {
		min_index := i
		for j := i + 1; j < n; j++ {
			if nums[j] < nums[min_index] {
				min_index = j
			}
		}
		nums[i], nums[min_index] = nums[min_index], nums[i]
	}
}
