"""
Trees are a widely used data structure that simulate a hierarchical tree structure. 
They're typically drawn upside down - the "root" node is at the top, and the "leaves" are at the bottom.

    Each node has a value and may have a list of "children"
    Children can only have a single "parent"

Binary Search Trees:
Trees aren't particulary useful unless they are ordered.
One of the most common types of ordered tree is a Binary search tree(BST). (a preordered tree)
BST contstraints:
    1. Each node has at most 2 children
    2. The left child value < parent value
    3. The right child value > parent value
    4. No two nodes in the BST can have the same value
    
Binary search trees are ordered. where left node value < parent node value < righ node value. No duplicates.
Binary Search Trees have O(log n) complexity for searching, inserting and deleting a value. where as stack and queue have O(1) for insertion and deletion.
BST are used in databases, file systems, google search
The depth of the tree on average is equal to "log base 2" of the number of nodes in the tree. 4096 nodes = 12 levels deep = 12 steps for at worst.
"""

class BSTNode:
    '''
    BST Nodes themselves can act a BST. Where they do not have any context of their parent. Only reference to their children.
    Most of the methods that traverse the tree do it recursively.
    '''
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        
    def insert(self, val):
        '''
        Insert a node into the binary tree
        '''
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            self.val
            return
        if val < self.val: 
            if self.left is None:
                self.left = BSTNode(val)
            else: 
                self.left.insert(val) # recursively calling the insert until the given value is added to the node.
        if val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
            else: 
                self.right.insert(val)
                
    def get_min(self):
        if self.left is None:
            if self.val is None:
                return None
            return self.val
        return self.left.get_min() #Recursively checking the left branch for min value
        
    def get_max(self):
        if self.right is None:
            if self.val is None:
                return None
            return self.val
        return self.right.get_max() #Recursively checking the right branch for min value
        
    def delete(self,val):
        '''
        Check if the current node is empty (has no value). If it is, return None. This represents an empty tree or a leaf node where deletion has already occurred.
        If the value to delete is less than the current node's value:
        
            If there's a left child, recursively delete the value from the left subtree and update the left child reference with the result.
            Return the current node.
        
        If the value to delete is greater than the current node's value:
        
            If there's a right child, recursively delete the value from the right subtree and update the right child reference with the result.
            Return the current node.
        
        If the value to delete equals the current node's value, we've found the node to delete:
        
            If there is no right child, return the left child. This bypasses the current node, effectively deleting it.
            If there is no left child, return the right child, accomplishing the same thing.
            If there are both left and right children, we need to find the new "successor": the smallest node in the right subtree, which is the value next largest after the current node's value.
                Find the smallest node in the right subtree by walking down the current right child's left branches until reaching a node with no left child.
                Replace the current node's value with this successor's value.
                Delete the successor node from the right subtree by recursively calling delete, and update the right child reference with the result.
                Return the current node.
        

        '''
        if self.val is None:
            return None
        if val < self.val:
            if self.left is not None:
                self.left = self.delete(val)
                return self
        if val > self.val:
            if self.right is not None:
                self.right = self.delete(val)
                return self
        if val == self.val:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            if self.left is not None and self.right is not None:
                current = self.right.left
                while current:
                    current = current.left
                self.val = current
                self.right = self.delete(self.val)
                return self.val
    
    def preorder(self,visited:list):
        '''
            > 7
                > 6
        > 4
            > 2
                > 1
        Above tree will be visited as [4, 2, 1, 7, 6]
        
        If the current node actually contains a value (self.val is not None), visit it by appending its value to the visited array
        Recursively traverse the left subtree
        Recursively traverse the right subtree
        Return the array of visited nodes
        '''
        if self.val is not None:
            visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited
    
    def postorder(self,visited):
        '''
            > 7
                > 6
        > 4
            > 2
                > 1
                
        Above tree will be visited as [1, 2, 6, 7, 4]
        
        Recursively traverse the left subtree
        Recursively traverse the right subtree
        Visit the value of the current node by appending its value to the visited array
        Return array of visited nodes
        
        '''
        if self.left is not None:    
            self.left.postorder(visited)
        if self.right is not None:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited
    
    def inorder(self,visited):
        '''
            > 7
                > 6
        > 4
            > 2
                > 1
        The above tree will be traversed as [1, 2, 4, 6, 7]
        '''
        if self.left is not None:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited
        
    def exists(self,val):
        if self.val == val:
            return True
        if val < self.val and self.left is not None:
            self.left.exists(val)
        elif self.right is not None:
            self.right.exists(val)
        return False
    
    def height(self, height=0) -> int:
        if self.val is None:
            return 0
        height += 1
   
        lh,rh=0,0
        if self.left is not None:
            lh:int = self.left.height(height)
        if self.right is not None:
            rh:int = self.right.height(height)
        
        result = max(lh, rh)
        print(f"Left height: {lh} Right Height: {rh} Max:{result}")
        return result + 1
        
        
        
        