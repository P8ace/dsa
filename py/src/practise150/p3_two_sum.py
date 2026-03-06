'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Eg:
    nums = [3,4,5,6], target = 7
    
    Output: [0,1]

'''
class Solution:
    def two_sum(self,nums, target:int):
        '''
        time = n* (n-1)  -> O(n^2)
        space = O(1)
        '''
        
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i!=j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
        return []
        
    def two_sum2(self,nums, target):
        '''
        Use HashMap
        
        time: O(n)
        space: O(n)
        '''
        
        unvisited = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in unvisited:
                return [unvisited[diff],i]
            unvisited[n]=i
        return []