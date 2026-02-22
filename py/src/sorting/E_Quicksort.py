"""
Select a "pivot" element - We'll arbitrarily choose the last element in the list
Move through all the elements in the list and swap them around until all the numbers less than the pivot are on the left,
    and the numbers greater than the pivot are on the right
Move the pivot between the two sections where it belongs
Recursively repeat for both sections

Use two indices and a pivot point. The pivot point can be randomly picked. For this example lets choose to pick the last element in the list.

Algorithm:
    Complete quick_sort(nums, low, high):

        If low is less than high:
            Partition the input list using the partition function and store the returned "middle" index
            Recursively call quick_sort on the left side of the partition
            Recursively call quick_sort on the right side of the partition

    partition(nums, low, high):

        Set pivot to the element at index high
        Set i to the index before low
        For each index (j) from low to high - 1 (skip the pivot):
            If the element at index j is less than the pivot:
                Increment i by 1
                Swap the element at index i with the element at index j
        Swap the element at index i + 1 with the element at index high (the pivot's position)
        Return i + 1 (the pivot's new index)
"""


def quick_sort(nums, low, high):
    # low and high are the indices at start and end of list.
    # If not provided the low and high in the function signature, use the first and last indices of the list.

    # if high < 1:
    #     return nums
    # if high is None:
    #     high = len(nums - 1)

    if low < high:
        middle_index = partition(nums, low, high)
        quick_sort(nums, low, middle_index - 1)
        quick_sort(nums, middle_index + 1, high)

    return nums


def partition(nums, low, high):
    print(f"Before: {nums}")
    # sorting happens in place in partition function
    pivot = high  # choosing the last index to be the pivot point.
    i = low - 1  # starting at index -1
    for j in range(low, pivot):  # skip the pivot index(high)
        if nums[j] < nums[pivot]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]  # sorting happens here.
    nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1]  # sorting happens here.
    print(f"After:{nums}\n")
    return i + 1
