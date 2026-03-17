'''
You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
'''

class Solution:
    def longest_substring(self, s, k):
        left = right = length = temp = 0
        
        countstring = {}
        
        while right < len(s):
            countstring[s[right]] = 1 + countstring.get(s[right], 0)
            temp = max(temp, countstring[s[right]])
            
            while right - left + 1 - temp > k:
                countstring[s[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
            right += 1
        
        return length