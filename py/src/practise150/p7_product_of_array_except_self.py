'''
    Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
    Eg: 
        input 
'''

class Solution:
    def product_except_self(self, nums):
        result = [1] * len(nums)
        
        prefix = 1
        postfix = 1
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
            
        for i in range(len(nums)-1, -1 , -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
            
        return result