"""
find the max num for a given list.
The complexity of this alogrithm is O(n)
"""


def max(num):
    max = num[0]
    for item in num:
        if item > max:
            max = item
    return max
