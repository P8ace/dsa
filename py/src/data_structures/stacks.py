'''
A stack is a data structure that stores ordered items.
It's like a list, but its design is more restrictive. 
It only allows items to be added or removed from the top of the stack:
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.size() == 0:
            return None
        return self.items[-1]

    def pop(self):
        if self.size() == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item
    
    def is_balanced(self,input):
        if len(input) % 2 != 0:
            return False
            
        for item in input:
            if item == "(":
                self.push(item)
            else:
                _ = self.pop()
        return not self.items