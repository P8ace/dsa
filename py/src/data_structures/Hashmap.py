'''
Hashmap is a datastructure that maps keys to values.

The lookup, insertion and deletion operations of a hashmap have an average complexity of O(1).

#Implementation:
Hashmaps are built on top of arrays.
They use a hash function to convert a hashable key into an index. 
# The hash function;
1. Takes a key and returns an integer.                  #The returned integer is the index.
2. Always return the same integer for the same key
3. Always return a valid index in the array (non-negative, not greater than the array size)
'''

class HashMap():
    def __init__(self,size):
        self.backingarray = [None for i in range(size)]
        
    def __repr__(self):
        final = ""
        for i, v in enumerate(self.backingarray):
            if v is not None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final
        
    def hash_function(self,key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum%len(self.backingarray)
    
    def insert(self, key, value):
        index = self.hash_function(key)
        self.backingarray[index] = (key,value)