'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
'''

class Solution:
    def three_sum(self, nums):
        '''
        nums[i] + nums [j] + nums[k] = 0
        nums[i] = - (nums[j] + nums[k])

        '''
        result = []
        nums = sorted(nums)
        for i,n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum < -n:
                    j += 1
                elif sum > -n:
                    k -= 1
                else:
                    result.append([n,nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:   # skip duplicates for j
                        j +=1
        return result