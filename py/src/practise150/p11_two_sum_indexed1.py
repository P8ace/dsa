"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2.
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
"""


class Solution:
    def two_sum(self, nums, target):
        """
        time: O(n)
        space: O(n)
        """
        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff] + 1, i + 1]
            map[n] = i
        return []

    def two_sum2(self, nums, target):
        """
        time: O(n)
        space: O(1)
        """
        i, j = 0, len(nums) - 1

        while i < j:
            sum = nums[i] + nums[j]

            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            elif sum == target:
                return [i + 1, j + 1]

        return []
