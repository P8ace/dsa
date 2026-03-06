"""
Given an array of strings, group all anagrams together into sublists. You may return the output in any order.

Eg:
    Input: strs = ["act","pots","tops","cat","stop","hat"]

    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    Input: strs = ["x"]

    Output: [["x"]]
"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        alphabet_frequency = [0 for x in range(26)]

        for i in range(len(s)):
            alphabet_frequency[ord(s[i]) - ord("a")] += 1
            alphabet_frequency[ord(t[i]) - ord("a")] -= 1
        for x in alphabet_frequency:
            if x != 0:
                return False
        return True

    def group_anagrams(self, strs):
        '''
        time: O(n*m)
        '''
        if len(strs) <= 1:
            return [strs]

        mapofanagrams = defaultdict(list)

        for s in strs:
            frequency = [0] * 26
            for i in range(len(s)):
                frequency[ord(s[i]) - ord("a")] += 1

            mapofanagrams[tuple(frequency)].append(s)

        return list(mapofanagrams.values())
