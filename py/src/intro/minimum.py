"""
find the mininum num for a list of numbers
"""


def find_minimum(nums):
    minimum = float("inf")
    if len(nums) == 0:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
