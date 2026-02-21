"""
Binary search algoritm
O(logn)

Binary search works on a pre-sorted list of numbers

For a list of n elements
1. Set low = 0 and high = n - 1.
2. While low <= high:
    a. Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
       ** Floor division: round down to nearest interger for (low + high) / 2
    b. If list[median] == target, return True
    c. Else if list[median] < target, set low to median + 1
    d. Otherwise set high to median - 1
3. Return False
"""


def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False
