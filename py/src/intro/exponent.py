"""
Given a list of numbers, calculate the result of the following expression
average of items in the list * (no.of items in the list ^ 1.2)
"""


def exponent(nums):
    if len(nums) == 0:
        return 0
    sum = 0
    for num in nums:
        sum += num
    avg = sum / len(nums)

    return avg * (len(nums) ** 1.2)
