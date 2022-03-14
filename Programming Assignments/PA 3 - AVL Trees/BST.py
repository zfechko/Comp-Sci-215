# -*- coding: utf-8 -*-
"""
This is just a seperate file for BST so the main py file isn't too big
"""
class BSTNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data 
        self.left = left 
        self.right = right 
        self.parent = parent 
        self.balance_factor = 0
    
    def __iter__(self):
        '''
        Yield freezes the state of the function so that the next time the function 
        is called it continues executing from the exact point it left off earlier.
        '''
        if self:
            if self.has_left_child():
                 for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                 for elem in self.right_child:
                    yield elem

    def is_left_child(self):
        """
        Checks if a node is the left child of its parent
        """
        return self.parent and self.parent.left == self 
    
    def is_right_child(self):
        """
        Checks if a node is the right child of its parent
        """
        return self.parent and self.parent.right == self
    
    def has_right_child(self):
        """
        Checks if a node has a right child
        """
        return self.right
    
    def has_left_child(self):
        """
        Checks if a node has a left child
        """
        return self.left
    
    def has_both_children(self):
        """
        Checks if a node has both children
        """
        return self.left and self.right
    
    def is_root(self):
        """
        Checks if the given node is the root of the tree
        """
        return not self.parent
    
           
    
    
class BST:
    def __init__(self):
        self.root = None 
        self.size = 0 
            
    def _search(self, data, node):
        """
        Recursive search helper function that doe all the legwork of searching for a node
        """
        if node is None:
            return None
        else:
            if data == node.data:
                return node
            elif data < node.data:
                return self._search(data, node.left)
            elif data > node.data:
                return self._search(data, node.right)
    
    def search(self, data):
        """
        Wrapper function that calls _search
        """
        if self.root is None:
            return None
        else:
            node = self._search(data, self.root)
            if node is not None:
                return node.data
            else:
                return None
            
    def post_order_helper(self, node):
        """
        Recursive helper function to perform post order traversal
        """
        if node is not None:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data, end=' ')

    def post_order_traversal(self):
        """
        Wrapper function that calls the above helper function
        """
        if self.root is None:
            print("empty tree")
            return
        self.post_order_helper(self.root)
        print('\n')

    def in_order_helper(self, node):
        """
        Recursive helper function to perform in order traversal
        """
        if node is not None:
            self.in_order_helper(node.left)
            print(node.data, end=' ')
            self.in_order_helper(node.right)
    
    def in_order_traversal(self):
        """
        Wrapper function that calls the in_order_helper function
        """
        if self.root is None:
            print("empty tree")
            return
        self.in_order_helper(self.root)
        print('\n')
        
    def level_order_helper(self, node_list):
        """
        Recursive helper function to perform level order traversal
        """
        if len(node_list) > 0: 
            node = node_list.pop(0) 
            print(node.data, end = " ") 
            if node.left is not None: 
                node_list.append(node.left) 
            if node.right is not None: 
                node_list.append(node.right) 
            self.level_order_helper(node_list)

    def level_order_traversal(self):
        """
        Wrapper that calls level_order_helper
        """
        if self.root is None:
            print("empty tree")
            return
        else:
            node_list = [self.root]
            self.level_order_helper(node_list)
            for node in node_list:
                print(node.data, end=' ')
            print('\n')
            
    def pre_order_helper(self, node):
        """
        Recursive helper to perform pre order traversal
        """
        if node is not None:
            print(node.data, end=' ')
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)
    
    def pre_order_traversal(self):
        """
        Wrapper function that performs pre order traversal by calling the recursive helper
        """
        if self.root is None:
            print("empty tree")
            return 
        self.pre_order_helper(self.root)
        print('\n')
        
   
    def find_successor(self, node):
       """
       Finds the successor of a node
       """
       successor = None
       if node.has_right_child():
           successor = self.find_min(node.right)
       else:
           if node.parent:
               successor = node.parent
           else:
               node.parent.right = None
               successor = self.find_successor(node.right)
               node.parent.right = node
       return successor
        
    def find_min(self, node):
        """
        Finds the smallest value in the subtree
        """
        if node.left is None:
            return node 
        else: return self.find_min(node.left)
        
    def level_order_balance(self):
        """
        Performs level order traversal but instead of printing the data, it prints the balance factor
        this helps check if the tree isn't balanced
        """
        if self.root is None:
            print("empty tree")
            return
        else:
            node_list = [self.root]
            self.level_balance_helper(node_list)
            for node in node_list:
                print(node.balance_factor, end=' ')
            print('\n')
            
    def level_balance_helper(self, node_list):
        """
        Helper for printing balance factors in level order
        """
        if len(node_list) > 0: 
            node = node_list.pop(0) 
            print(node.balance_factor, end = " ") 
            if node.left is not None: 
                node_list.append(node.left) 
            if node.right is not None: 
                node_list.append(node.right) 
            self.level_balance_helper(node_list)
        