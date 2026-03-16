'''
You are given an integer array heights where heights[i] represents the height of the ithith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.
Eg:
    Input: height = [1,7,2,5,4,7,3,6]  
    Output: 36    
    Here distance between 7(i=1) and 6(i=7) is 6. and min between the two is 6, so the answer is 6*6
'''
class Solution:
    def maxArea(self, heights):
        '''
        time: O(n)
        space: O(1)
        '''
        maxArea = 0

        i, j = 0, len(heights)-1

        while i < j:
            currentArea = (j-i) * min(heights[i], heights[j])
            maxArea = max(currentArea, maxArea)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i +=1
        return maxArea