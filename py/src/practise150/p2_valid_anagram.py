'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Eg;
    Input: s = "racecar", t = "carrace"
    
    Output: true
'''

class Solution:
    
    def isAnagram(self, s:str, t:str):
        '''
        Time : O(nlogn + mlogm)
        Space: O(n)
        '''
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        
    def isAnagram2(self, s, t):
        '''
        time: O(n+m)
        Using Hasmaps or dicts
        '''
        if len(s) != len(t):
            return False

        sMap, tMap = {},{}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i],0)
            tMap[t[i]] = 1 + tMap.get(t[i],0)

        return sMap == tMap
        
    def isAnagram3(self, s:str, t:str): 
        '''
        Using an array
        time: O(n+m)
        space: O(1)
        '''
        if len(s) != len(t):
            return False
            
        alphabet_frequency = [0 for x in range(26)]
        
        for i in range(len(s)):
            alphabet_frequency[ord(s[i]) - ord('a')] += 1  #ord returns the unicode codepoint of the character ord('a') -> 65
            alphabet_frequency[ord(t[i]) - ord('a')] -= 1
        
        for x in alphabet_frequency:
            if x != 0:
                return False

        return True