'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example:
    Input: nums = [1, 2, 3, 3]
    
    Output: true
'''

class Solution:

    def contains_duplicate(self,nums):
        '''
        Has a time complexity of O(n)
        Has a space complexity of O(n)
        '''
        unvisited = set()
        
        for x in nums:
            unvisited.add(x)
            
        if len(unvisited) < len(nums):
            return True
        return False
    
    def contains_duplicate_2(self, nums):
        unvisited = set()
        
        for x in nums:
            if x in unvisited:
                return True
            unvisited.add(x)
            
        return False