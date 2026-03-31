package sorting

// Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order.
// It continues to loop over the slice until the whole list is completely sorted.

// So what is the time complexity of Bubble sort?   O(n2) look for the worst scenario.
// 1. Best Case:   if the list is pre-sorted the bubble sort will be really fast. O(n)
// 2. Worst Case:  if the list is in reverse order, bubble sort can become really slow. O(n2)
// Bubble sort is one of the slowest algorithmsn.

func BubbleSort(nums []int) {
	n := len(nums)

	for i := 0; i < n-1; i++ {
		for j := 0; j < n-1-i; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
}
