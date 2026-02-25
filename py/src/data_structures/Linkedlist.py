"""
Linked list is a collection of ordered items. Each element in a Linked list has a reference to the next.
Each element has a value and a reference to the next element.

Pros:
    1. Inserting: elements in the middle of the chain : O(1) when compared to lists O(n)
Cons:
    1. Find an element: O(n). Iterating through all the nodes by following the next references.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #Added this to keep track of the tail for O(1) additions the tail of the linked list.

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
        # nodes = []
        # current = self.head
        # while current and hasattr(current,"val"):
        #     nodes.append(current)
        #     current= current.next
        # return "->".join(nodes)
        #

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        if last_node is not None:
            last_node.set_next(node)

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        self.head = node
        self.head.set_next(current)
        
    def add_to_tail_O1(self, node):
        '''
        An implementation of O(1) adds to the linked list.
        '''
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        if self.tail is not None:
            self.tail.set_next(node)
        self.tail = node
        
    def add_to_head_O1(self,node):
        '''
        An implementation of O(1) adds to the linked list.
        '''
        if self.head is None:
            self.head = node
            self.tail = node
            return
        current = self.head
        self.head = node
        self.head.set_next(current)


class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None #Added this to keep track of the tail for O(1) additions the tail of the linked list.

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <-".join(nodes)
        # nodes = []
        # current = self.head
        # while current and hasattr(current,"val"):
        #     nodes.append(current)
        #     current= current.next
        # return "->".join(nodes)
        #

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        if last_node is not None:
            last_node.set_next(node)
        
    def add_to_tail_O1(self, node):
        '''
        An implementation of O(1) adds to the linked list.
        '''
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        if self.tail is not None:
            self.tail.set_next(node) # set the last node's next to the given node
        self.tail = node        # sest the tail field of the llqueue to the given node

    def remove_from_head_O1(self):
        if self.head is None:
            return None
        
        temp =  self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        temp.next = None
        return temp
