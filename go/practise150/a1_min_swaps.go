package practise150

import (
	"slices"
)

func min_swaps(nums []int) int {
	reversed := make([]int, len(nums))
	_ = copy(reversed, nums)
	slices.SortFunc(reversed, func(a, b int) int {
		if a > b {
			return -1
		} else if a < b {
			return 1
		}
		return 0
	})

	position_map := make(map[int]int)
	for i, n := range reversed {
		position_map[n] = i
	}

	swaps := 0

	for i := 0; i < len(nums); i++ {
		if reversed[i] != nums[i] {

			ind := position_map[reversed[i]]
			nums[i], nums[ind] = nums[ind], nums[i]

			position_map[nums[i]] = i
			position_map[nums[ind]] = ind

			swaps++
		}
		// fmt.Println(i, nums, swaps)
	}
	return swaps

}
