'''
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters.
Eg:
    Input: s1 = "abc", s2 = "lecabee"
    Output: true
'''

class Solution:
    def check_permutation(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        left = 0
        right = len(s1) - 1
        
        s1Map = {}
        for s in s1:
            s1Map[s] = 1 + s1Map.get(s,0)
            
        while right < len(s2):
            k = left
            temp = {}
            while k <= right:
                temp[s2[k]] = 1 + temp.get(s2[k],0)
                k += 1
            if temp == s1Map:
                return True
            left += 1
            right += 1
        return False