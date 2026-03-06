'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.



'''

class Solution:

    def encode(self, strs):
        if len(strs) <=1:
            return strs[0]
        result = ""
        for s in strs:
            result += str(len(s))
            result += '#'
            result += s
        return result


    def decode(self, s):
        if s == "":
            return [""]
        final_list = []

        n = len(s)
        i=0
        while (i<n):
            if s[i] != "#":
                i += 1
                continue
            length = int(s[i-1])
            final_list.append(s[i+1: i+1+length])
            i += length

        return final_list