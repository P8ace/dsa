"""

For each index:
    Set smallest_idx to the current index (of the outer loop)
    For each index from i + 1 to the end of the list:
        If the number at the inner loop index is smaller than the number at smallest_idx, set smallest_idx to the inner loop index
    Swap the number at the outer loop index with the number at smallest_idx
Return the sorted list

"""


def selection_sort(nums):
    for i in range(len(nums)-1):
        small_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[small_idx]:
                small_idx = j
        nums[i], nums[small_idx] = nums[small_idx], nums[i]
    return nums
