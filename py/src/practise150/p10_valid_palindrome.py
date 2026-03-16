"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Eg:
    Input: s = "Was it a car or a cat I saw?"

    Output: true
"""


class Solution:
    def isAlphaNum(self, char):
        return (
            ord("A") <= ord(char) <= ord("Z")
            or ord("a") <= ord(char) <= ord("z")
            or ord("0") <= ord(char) <= ord("9")
        )

    def valid_palindrome(self, s):

        i = 0
        j = len(s) - 1

        while i <= j:
            while i < j and not self.isAlphaNum(s[i]):
                i += 1
            while j > i and not self.isAlphaNum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
