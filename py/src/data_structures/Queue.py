'''
A queue only allows items to be added to the tail of the queue and removed from the head of the queue.
'''
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        if self.size() == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        if self.size() == 0:
            return None
        item = self.items[-1]
        return item

    def size(self):
        return len(self.items)
        
    def matchmake(self, user):
        name, action = user
        if action == "leave":
            self.search_and_remove(name)
        if action == "join":
            self.push(name)  
        
        if self.size() < 4:
            return "No match found"
        if self.size() == 4:
            user1 = self.pop()
            user2 = self.pop()
            return f"{user1} matched {user2}!"
           
         
         
        
    '''
    Helper functions for matchmake method. Not to be associated with the queue implementation
    '''    
    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"