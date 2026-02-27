"""
Hashmap is a datastructure that maps keys to values.

The lookup, insertion and deletion operations of a hashmap have an average complexity of O(1).

#Implementation:
Hashmaps are built on top of arrays.
They use a hash function to convert a hashable key into an index.
# The hash function;
1. Takes a key and returns an integer.                  #The returned integer is the index.
2. Always return the same integer for the same key
3. Always return a valid index in the array (non-negative, not greater than the array size)
"""


class HashMap:
    def __init__(self, size):
        self.backingarray = [None for i in range(size)]

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.backingarray):
            if v is not None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final

    def hash_function(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % len(self.backingarray)

    def insert(self, key, value):
        self.resize()
        index = self.hash_function(key)
        self.backingarray[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        try:
            return self.backingarray[index][1]
        except Exception as e:
            raise Exception("sorry, key not found")

    def resize(self):
        """
        Our hashmap has a lot of collisions. This is because we are using a fixed size for our hashmap.
        When resizing, we create a new hashmap with a larger number of slots.
        Then, we re-insert all the key-value pairs from the old hashmap into the new hashmap.

        If the length of the underlying hashmap is 0, make the length 1 (by just adding a None entry) and return.
        Get the current load. If it's less than 5%, do nothing, we have plenty of space
        Otherwise, we need to resize the hashmap.

            Store the current hashmap in a temporary variable
            Create a new empty hashmap that's 10x the size of the current one and assign it to self.hashmap.
            Re-insert all the key-value pairs from the temporary variable into self.hashmap.


        """
        if len(self.backingarray) == 0:
            self.backingarray.append(None)
            return
        current_load = self.current_load()
        if current_load * 100 < 5:
            return
        temp = self.backingarray
        self.backingarray = [None for i in range(10 * len(temp))]
        for item in temp:
            if item is not None:
                self.insert(item[0], item[1])

    def current_load(self):
        """
        If the length of the underlying list is zero, return 1.
        Otherwise, divide the number of filled buckets by the length of the underlying list and return it.
        """
        if len(self.backingarray) == 0:
            return 1
        count = 0
        for item in self.backingarray:
            if item is not None:
                count += 1

        return count / len(self.backingarray)
        
    
    def insert_with_linear_probing(self,key,value):
        '''
        Collisions happen when two different keys have the same index after applying the key_to_index function. 
        To handle collisions, we can use a technique called linear probing.
        
        Linear probing works by finding the next available slot after the collision index and placing the new key*value pair there.
        '''
        
        index=self.hash_function(key)
        
        original_index = index
        first_iteration=True
        
        item = self.backingarray[index]

        while item is not None and item[0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index += 1
            index %= len(self.backingarray)
            first_iteration = False
            
        self.backingarray[index] = (key,value)
            

    def get_with_linear_probing(self,key):
        index=self.hash_function(key)
        
        original_index = index
        first_iteration=True
        
        item = self.backingarray[index]

        while item is not None:
            (c_key,c_val) = self.backingarray[index]
            if c_key == key:
                return c_val

            if not first_iteration and index == original_index:
                raise Exception("Sorry, key not found")
            index += 1
            index %= len(self.backingarray)
            first_iteration = False
            
        raise Exception("Sorry, key not found")