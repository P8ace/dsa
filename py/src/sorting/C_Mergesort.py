"""
The algorithm consists of two separate functions, merge_sort() and merge().
1.  merge_sort() divides the input array into two halves, calls itself on each half, and then merges the two sorted halves back together in order.
2.  The merge() function merges two already sorted lists back into a single sorted list.
    At the lowest level of recursion, the two "sorted" lists will each only have one element.
    Those single element lists will be merged into a sorted list of length two, and we can build from there.

In other words, all the "real" sorting happens in the merge() function.

Hint: Use two indexes to track the two slices that were split from the original.

merge_sort() pseudocode
Input: A, an unsorted list of integers
    If the length of A is less than 2, it's already sorted so return it
    Split the input array into two halves down the middle
    Call merge_sort() twice, once on each half
    Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls

merge() pseudocode
Inputs: A and B. Two sorted lists of integers
    Create a new final list of integers.
    Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
    Use a loop to compare the current elements of A and B.
    If an element in A is less than or equal to its respective element in B, add it to the final list and increment i.
    Otherwise, add the item in B to the final list and increment j. Continue until all items from one of the lists have been added.
    After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
    Return the final list.
"""


def merge_sort(nums):
    arr_length = len(nums)
    if arr_length < 2:
        return nums
    median = len(nums) // 2
    print(f"length : {arr_length}  median_index : {median}")
    left_arr = nums[0:median]
    right_arr = nums[median:arr_length]
    left_sorted_arr = merge_sort(left_arr)
    right_sorted_arr = merge_sort(right_arr)
    return merge(left_sorted_arr, right_sorted_arr)


def merge(first, second):
    final_list = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final_list.append(first[i])
            i += 1
        else:
            final_list.append(second[j])
            j += 1
    while i < len(first):
        final_list.append(first[i])
        i += 1
    while j < len(second):
        final_list.append(second[j])
        j += 1

    return final_list
