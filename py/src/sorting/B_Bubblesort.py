"""
Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order.
It continues to loop over the slice until the whole list is completely sorted.

So what is the time complexity of Bubble sort?   O(n2) look for the worst scenario.
1. Best Case:   if the list is pre-sorted the bubble sort will be really fast. O(n)
2. Worst Case:  if the list is in reverse order, bubble sort can become really slow. O(n2)
Bubble sort is one of the slowest algorithmsn.

Hint: The first for loop stores the highest element at the end of list. So for the next iteration, then length is decremented by 1.
PseudoCode:
    Set swapping to True
    Set end to the length of the input list
    While swapping is True:
        Set swapping to False
        For i from the 2nd element to end:
            If the (i-1)th element of the input list is greater than the ith element:
                Swap the (i-1)th element and the ith element
                Set swapping to True
        Decrement end by one
    Return the sorted list
"""


def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums
