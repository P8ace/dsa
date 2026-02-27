'''
Tries are often used in natural language processing. 
In python, these can be reprsented as nested dictionaries where each key is a character that maps to the next character in a word

{h: {e : {l :{l :{o:{*:True}}}}}} * indicates the end of the word.
A trie is also referred to as "prefix Tree", because it can be used to efficiently find all the words that start with a given prefix.
For words hello and hi, prefix 'h' should return both hello and hi.
'''
import json
class Node:
    def __int__(self):
        self.children={}
        
class Trie:
    def __init__(self):
        self.root = {}
        self.end_sybmol="*"
        
    def add(self,word):
        '''
        Keep track of your "current level" in the trie, starting at the root.
        Loop over each character in the word-to-add:
        
            If the character is not a key in the current level, add it and create a new nested level (dictionary) for it.
            Update your "current level" to the nested dictionary for this character (whether it was just created or already existed).
        
        Once you've ensured all the dictionaries exist, add an entry to the dictionary of the last character in the word with self.end_symbol 
            as the key and True as the value. This will indicate that this is a complete word and not just a prefix of another word.
        '''
        
        node = self.root
        for char in word:
            if char not in node.keys():
                node[char]={}
            node = node[char]
        node[self.end_sybmol] = True
        
    def exists(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        if self.end_sybmol in node:
            return True
        return False

    def search_level(self, current_level, current_prefix, words):
        if self.end_sybmol in current_level:
            print("**************************************************************************")
            words.append(current_prefix)
            print(f"Reached symbol here {current_level}")
            print(f"words {words}")
            print("_-------------------------------------------------------------------------")
        for item in sorted(current_level):
            print(f"current level: {sorted(current_level)}")
            print(f"len of current level: {len(current_level)}")
            print(f"item at current_level: {item}")
            print(f"prefix before update: {current_prefix}")
            if item != self.end_sybmol:
                print(f"Prefix after update: {current_prefix + item}                        -recursion back to search")
                self.search_level(current_level[item], current_prefix + item, words)
        return words
            

    def words_with_prefix(self, prefix):
        matching_words= []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            else:
                current_level = current_level[letter]
        return self.search_level(current_level, prefix, matching_words)
    

    def find_matches(self, document):
        result = []
        for i in range(len(document)):
            print("Outer loop----------------------------------------------------------------------")
            print(f"Outer char: {document[i]} outer index: {i}")
            current_level = self.root
            for j in range(i, len(document)):
                innerchar = document[j]
                if innerchar not in current_level:
                    print(f"Charachter: {innerchar} not in current level: {sorted(current_level)}")
                    break
                else:       
                    print(f"charachter {innerchar} in current level: {current_level}")
                    current_level = current_level[innerchar]
                if self.end_sybmol in current_level:
                    print(f"substring found: {document[i:j + 1]}. Pushing it to result")
                    result.append(document[i:j + 1])
                    print(f"result: {result}")
        return result

    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            keys = current.keys()
            if self.end_sybmol in keys:
                break
            if len(keys)==1:
                for key in keys:
                    prefix += key
                    current = current[key]
            else:
                break
        return prefix

    def advanced_find_matches(self, document, variations):
        result = []
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                innerchar = document[j]
                if innerchar in variations:
                    innerchar = variations[innerchar]
                if innerchar not in current_level:
                    break
                else:
                    current_level  = current_level[innerchar]
                if self.end_sybmol in current_level:
                    result.append(document[i:j+1])
        return result
                    
if __name__ == "__main__":
    word = "hello"
    trie = Trie()
    trie.add(word)
    print(json.dumps(trie.root, indent=2))