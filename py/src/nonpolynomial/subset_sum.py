"""
given a list of numbers and a target,
find the subset of the list, whose sum is equal to the sum
"""


def subset_sum(nums, target):
    last_index = len(nums)
    print(nums)
    return find_subset_sum(nums, target, last_index)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index == 0:
        return False

    if nums[index-1] > target:
        return find_subset_sum(nums, target, index - 1)

    return (find_subset_sum(nums, target, index - 1) or 
        find_subset_sum(nums, target - nums[index-1], index - 1))
