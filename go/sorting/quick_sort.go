package sorting

func quickSort(nums []int, low, high int) {
	if low < high {
		median := partition(nums, low, high)

		quickSort(nums, low, median-1)
		quickSort(nums, median+1, high)

	}
}

func partition(nums []int, low, high int) int {
	pivot := nums[high]
	i := low - 1

	for j := low; j < high; j++ {
		if nums[j] <= pivot {
			i++
			nums[j], nums[i] = nums[i], nums[j]
		}
	}
	nums[i+1], nums[high] = nums[high], nums[i+1]
	return i + 1
}

func quickSort2(nums []int, left, right int) {
	if right <= left+1 {
		if right == left+1 && nums[right] < nums[left] {
			nums[left], nums[right] = nums[right], nums[left]
		}
		return
	}

	median := partition2(nums, left, right)
	quickSort2(nums, left, median-1)
	quickSort2(nums, median+1, right)
}

func partition2(nums []int, left, right int) int {
	mid := (left + right) >> 1
	nums[mid], nums[left+1] = nums[left+1], nums[mid]

	if nums[left] > nums[right] {
		nums[left], nums[right] = nums[right], nums[left]
	}
	if nums[left+1] > nums[right] {
		nums[left+1], nums[right] = nums[right], nums[left+1]
	}
	if nums[left] > nums[left+1] {
		nums[left], nums[left+1] = nums[left+1], nums[left]
	}

	pivot := nums[left+1]
	i := left + 1
	j := right

	for {
		for i++; nums[i] < pivot; i++ {
		}
		for j--; nums[j] > pivot; j-- {
		}
		if i > j {
			break
		}
		nums[i], nums[j] = nums[j], nums[i]
	}

	nums[left+1], nums[j] = nums[j], nums[left+1]
	return j
}
