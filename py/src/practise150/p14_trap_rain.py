'''
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
'''

class Solution:
    def trap(self, height):
        if len(height) == 0:
            return 0
            
        i, j = 0 , len(height) -1
        leftMax, rightMax, result = 0, 0 ,0
        
        while i < j:
            if height[i] < height[j]:
                leftMax = max(leftMax, height[i])
                result += leftMax - height[i]
                i += 1
            else:
                rightMax = max(rightMax, height[j])
                result += rightMax - height[j]
                j -= 1
            
        return result