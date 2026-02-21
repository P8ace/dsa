'''
Use two indexes i and j to sort the list.
1. For each index in the input list, starting with the second element:
    a. Set a j variable to the current index
    b. While j is greater than 0 and the element at index j-1 is greater than the element at index j:
       i. Swap the elements at indices j and j-1
       ii.  Decrement j by 1
2. Return the list

BigO: O(n^2)
The outerloop of insertion sort will always loop for n times.
While inner loop depends on the input. so the worst case scenario is n times. Hence n^2.
Best case is if the array is pre-sorted then O(n)

Best used for small inputs.
'''

def insertion_sort(nums):
    for i in range (1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums