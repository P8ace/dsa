'''
Binary Search Trees have on average O(log(n)) complexity for lookups, insertions and deletions.
However, if sorted data is inserted, the BST will be very deep. Looks like a single brach of a tree as the data is mostly sorted.
This can sometimes cause the complexity to fall to O(n)

A RED_BLACK Tree is a Binary search tree, that contains extra logic (A FIX STEP by performing a rotation) 
    to ensure that as nodes are inserted/deleted the tree remains relatively balanced.
    i.e., That the tree remains more wide than deep. Keeping the complexity to O(log(n))
    
The rules to form a RB tree.
1. Each node is either RED or BLACK.
2. The root is BlACK.
3. All nill leaf nodes are BLACK.
4. If a node is RED, then both its children must be BLACK.
5. All paths from a node, to any of its descendant NILL BLACK nodes (Bottom of the tree), must go through the same no.of BLACK nodes.

Each node in an RB tree stores an extra property color. The 'color' property ensures that the tree remains relatively balanced during
insertions and deletions. When the tree is modified(insertions/deletions), the tree is rearranged and repainted to restore the coloring
properties.

RB Trees are mostly balanced, with each operation.
'''


class RBNode:
    def __init__(self, val):
        '''
        RB node has two extra properties compared to an BST node. color and parent.
        '''
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        '''
        The property self.nil containes values we'll use to designate all the nil(empty) leaf nodes,
        which are used for rebalancing the tree.
        
        Keep in mind this is different to a BST node where each node can be its own BST tree. 
        When it comes to RB Tree, nodes themselves cannot be RB trees.
        '''
        self.nil = RBNode(None) #Empty leaf nodes. Used during rotations.
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        '''
        Create the new_node:
        
            Create a new RBNode from the given input value
            The new_node shouldn't have a parent yet
            The new_node's left and right children should be nil
            The new_node is red. (new_node.red = True)
        
        Find the parent of the new_node if there will be one:
        
            Initialize a parent variable to None
            Initialize a current variable to the root node of the tree
            While current isn't a nil node:
                Set parent to the current
                If the new_node's value is less than the current node's, set current to its own left child. If new_node's value is greater, set current to its own right child. 
                If the values are equal, just return because this value is a duplicate.
            If you followed the steps correctly, parent will be a reference to the node that will become the parent of the new_node
        
        Insert the new_node by setting the parent's child:
        
            Set the new_node's parent to the parent we just found
            If the parent is None, we are dealing with a new root, so set the tree's root data member to the new_node
            Otherwise, compare the values of the parent and new_node and set the parent's left or right child based on the results
        
        
        '''
        # Initializing the RB node
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True
        # Find the parent of the node
        parent = None
        current = self.root
        while current != self.nil:              
            parent = current                    #parent to be after rotating the tree. (pivot)
            if new_node.val < current.val:
               current = current.left
            if new_node.val > current.val:
               current = current.right 
            if new_node.val == current.val:
                return
        #Insert the new node by setting the parent's child
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.fix_insert(new_node)
            
    def fix_insert(self, new_node):
        '''
        Complete the insert method to call our balancing method after inserting a new node.
        Complete the fix_insert method that maintains red-black tree properties, starting with the newly inserted node as the current node:
        
            While the current node is not the root and has a red parent:
                Identify the "parent", "grandparent", and "uncle" nodes of the newly inserted node
                If the parent is a right child of the grandparent:
                    If the uncle is red:
                        Recolor the uncle and parent to black
                        Recolor the grandparent to red
                        Move up the tree by making the current node the grandparent
                    If the uncle is black:
                        If the current node is the left child of the parent:
                            Move up the tree by making the current node the parent
                            Rotate right around the current node
                            Set the parent to be the current node's parent
                        Recolor the parent to black
                        Recolor the grandparent to red
                        Rotate left around the grandparent
                If the parent is a left child of the grandparent:
                    If the uncle is red:
                        Recolor the uncle and parent to black
                        Recolor the grandparent to red
                        Move up the tree by making the current node the grandparent
                    If the uncle is black:
                        If the current node is the right child of the parent:
                            Move up the tree by making the current node the parent
                            Rotate left around the current node
                            Set the parent to be the current node's parent
                        Recolor the parent to black
                        Recolor the grandparent to red
                        Rotate right around the grandparent
            Recolor the root to black
        '''
        current = new_node
        while current != self.root and current.parent:
            grand_parent = current.parent.parent
            parent = current.parent
            if parent == grand_parent.right:
                if grand_parent.left.red:
                    grand_parent.left.red = False
                    parent.red = False
                    grand_parent.red = True
                    grand_parent = current
                if not grand_parent.right.red:
                    if current == parent.left:
                        parent = current
                        self.rotate_right(current)
                        parent = current.parent
                    parent.red = False
                    grand_parent.red = True
                    self.rotate_left(grand_parent)
            if parent == grand_parent.left:
                if grand_parent.left.red:
                    grand_parent.left.red = False
                    parent.red = False
                    grand_parent.red = True
                    grand_parent = current
                if not grand_parent.left.red:
                    if current == parent.right:
                        parent = current
                        self.rotate_left(current)
                        parent = current.parent
                    parent.red = False
                    grand_parent.red = True
                    self.rotate_right(grand_parent)
        self.root.red = False
            
    def rotate_left(self, pivot_parent):
        '''
        # Rotation of a tree is O(1) operation
        Rotating left:
            The "pivot" node's initial parent becomes its left child
            The "pivot" node's old left child becomes its initial parent's new right child
        
        # Steps: Input passed is the pivot parent
        If pivot_parent is nil or pivot_parent's right child is nil, return. Nothing to do here.
        Let pivot be pivot_parent's right child.
        Set pivot_parent's right child to be pivot's left child.
        If pivot's left child isn't a nil leaf node, set pivot's left child's parent to pivot_parent.
        Set pivot's parent to pivot_parent's parent.
        If pivot_parent is the root, set the root to pivot.
        
            Otherwise, if pivot_parent is its parent's left child, set pivot_parent's parent's left child to pivot.
            Otherwise, if pivot_parent is its parent's right child, set pivot_parent's parent's right child to pivot.
        
        Set pivot's left child to be pivot_parent.
        Set pivot_parent's parent to be pivot.
        '''
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return                                                          # Break point
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
            
        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        if pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.riht!= self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        if pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot
        