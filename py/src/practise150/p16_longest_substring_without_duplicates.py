'''
Given a string s, find the length of the longest substring without duplicate characters.
'''

class Solution:
    def longestsubstring(self, s):
        length, left, right = 0,0,0
        
        setstring = set()
        while right < len(s):
            while s[right] in setstring:
                setstring.remove(s[left])
                left +=1
            setstring.add(s[right])
            length = max(length, right - left + 1)
            right += 1
        return length