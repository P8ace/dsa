'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

Eg:
    Input: nums = [2,20,4,10,3,4,5]
    Output: 4
'''

class Solution:
    def longest_consecutive_sequence(self, nums):
        
        seen = set()
        
        longest_sequence = 0
        
        for n in nums:
            seen.add(n)

                
        for n in seen:
            if n-1 not in seen:
                length = 1
                while n + length in seen:
                    length += 1
            longest_sequence = max(length, longest_sequence)
            
        return longest_sequence