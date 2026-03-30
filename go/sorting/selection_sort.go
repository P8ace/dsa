package sorting

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
