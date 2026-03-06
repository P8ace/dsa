'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
Eg:
    Input: nums = [1,2,2,3,3,3], k = 2
    
    Output: [2,3]
    
    Input: nums = [7,7], k = 1
    
    Output: [7]
    
    Input: nums = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
    Output: [5, 11, 7, 10]
    Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, and frequency of rest is 1  but 10 is largest .
'''

import heapq

class Solution:
    
    def topK_frequent(self, nums, k):
        '''
        brute force
        time: O(n + nlogn)
        '''
        map = {}
        
        for n in nums:
            map[n] = 1+ map.get(n,0)
            
        freq = list(map.items())
        freq.sort(key=lambda x: ((x[1], x[0])), reverse=True)
        
        res = []
        for i in range(k):
            res.append(freq[i][0])
            
        return res
        
    def topK_frequent2(self, nums, k):
        '''
        Uses priority queue
        
        time: O(nlogk) log due to priority queue
        '''
        map = {}
        
        for n in nums:
            map[n] = 1 + map.get(n,0)

            
        final_list = []
        for key,val in map.items():
            heapq.heappush(final_list, (val,key))
            if len(final_list) > k:
                heapq.heappop(final_list)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(final_list)[1])
        
        return res
        
    def topK_frequent3(self, nums, k):
        '''
        Uses bucket sort
        
        time: O(n + n + n) O(n)
        
        '''
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n,0)
            
        freq = [[] for x in range(len(nums) + 1)] #The number here is +1 because the indexes represent the frequency, not just the length

        for key,val in map.items():
            freq[val].append(key)
        
        res = []
        
        print(f"freq: {freq}" )
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            