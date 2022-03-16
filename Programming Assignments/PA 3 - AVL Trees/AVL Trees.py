"""
Title: Programming Assignment 3, AVL Trees
Author: Zach Fechko
Version: 1.0
Last Updated: Mar 14, 2022

Description: Implementation of an AVL tree, inserts sample values and deletes one of the values, 
and then visualizes the tree with graphviz
"""
import BST as tree
from graphviz import Graph
import pydot

class AVLTree(tree.BST):
    def __init__(self):
        """
        AVL Tree constructor
        """
        super(AVLTree, self).__init__()
        self.graph = None
   
    def __len__(self):
        return self.size 
    
    def __iter__(self):
        return self.root.__iter__()
    
    def __setitem__(self, v):
        self.insert(v)
   
    def __getitem__(self, value):
        return self.search(value)
    
    def __delitem__(self, value):
        self.delete(value)
        
    def __contains__(self, value):
        if self._search(value, self.root):
            return True
        else:
            return False
        
        
    def rotate_left(self, rot_root):
        """
        Performs left rotation on a given node
        new root of the subtree is the right child of previous root
        right child of root is replaced with the left child of the new root
        adjust the parent references
        1. if new root has a left child then the new parent of the left child becomes the old root
        2. if the old root was the root of the entire tree then we set the root of the tree to point to the new root
           else if the old root is a left child then we change the parent of the left child to point to the new root
                else we change the parent of the right child to point to the new root
        3. set the parent of the old root to be the new root
        """
        new_root = rot_root.right
        rot_root.right_child = new_root.left
        if new_root.left != None:
            new_root.left.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left = new_root
            else:
                rot_root.parent.right = new_root
        new_root.left = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)
        
    def rotate_right(self, rot_root):
        """
        Performs right rotation on a given node
        new root of the subtree is the right child of previous root
        right child of root is replaced with the left child of the new root
        adjust the parent references
        1. if new root has a left child then the new parent of the left child becomes the old root
        2. if the old root was the root of the entire tree then we set the root of the tree to point to the new root
           else if the old root is a left child then we change the parent of the left child to point to the new root
                else we change the parent of the right child to point to the new root
        3. set the parent of the old root to be the new root
        """
        new_root = rot_root.left
        rot_root.left = new_root.right
        if new_root.right != None:
            new_root.right.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right = new_root
            else:
                rot_root.parent.left_ = new_root
        new_root.right = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(rot_root.balance_factor, 0)


    def rebalance(self, node):
        """
        Fixes a height violation by performing rotations depending on what case it is
        Case 1: Inserting into the right subtree of the right child (left rotation)
        Case 2: Inserting into the left subtree of the left child (right rotation)
        Case 3: Inserting into the right subtree of the left child (left right rotation)
        Case 4: Inserting into the left subtree of the right child (right left rotation)
        """
        if node.balance_factor < 0:
            if node.right.balance_factor > 0:
                #CASE 4
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                #CASE 1
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left.balance_factor < 0:
                #CASE 3
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                #CASE 2
                self.rotate_right(node)
    
    def update_balance_insert(self, node):
        if node.balance_factor == 0:
            return 
        elif node.balance_factor == +1:
            if node.is_left_child():
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parent)
            elif node.is_right_child():
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)
        elif node.balance_factor == -1:
            if node.is_left_child():
                node.parent.balance_factor += 1
                self.update_balance_insert(node.parent)
            elif node.is_right_child():
                node.parent.balance_factor -= 1
                self.update_balance_insert(node.parent)
        elif node.balance_factor == -2:
            if node.right.balance_factor == -1:
                self.rotate_left(node)
            else:
                self.rotate_right(node.right)
                self.rotate_left(node)
        elif node.balance_factor == +2:
            if node.left.balance_factor == +1:
                self.rotate_right(node)
            else:
                self.rotate_left(node.left)
                self.rotate_right(node)
        else:
            raise Exception("Unhandled case - Balance factor out of range")
    
    def update_balance(self, node):
        """
        Recursively rebalances a tree by calling rebalance() and 
        updating a node's balance factor
        """
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
                
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)
                
    def _insert(self, data, node):
        """
        Recursive insertion helper function that inserts a node
        and then rebalances the tree
        """
        if data == node.data:
            return 
        elif data < node.data:
            if node.left is None:
                node.left = tree.BSTNode(data, parent=node)
                self.size += 1
                node.balance_factor += 1
                self.update_balance_insert(node)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = tree.BSTNode(data, parent=node)
                self.size += 1
                node.balance_factor -= 1
                self.update_balance_insert(node)
            else:
                self._insert(data, node.right)

                
    def insert(self, data):
        """
        Wrapper insert function to insert data into an AVL tree
        """
        if self.root is None:
            self.root = tree.BSTNode(data)
            self.size += 1
        else:
            self._insert(data, self.root)
            
    def remove(self, node):
        """
        Actually does the deleting of a given node, deletes the node and then at the
        end of each deletion case, the tree gets rebalanced
        """
        if (node.left is None) and (node.right is None): #case 1
            if node is node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            self.update_balance(node.parent)
        elif node.left is not None and node.right is None: #case 2 for the left node
            if node.parent is not None:
                if node.parent.left is node: #if node is left child
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
                self.update_balance(node.parent)
            else:
                self.root = node.left
                node.left.parent = None
                self.update_balance(self.root)
        elif node.left is None and node.right is not None: #case 2 for right node
            if node.parent is not None:
                if node.parent.left is node: #if node is left child
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                self.update_balance(node.parent)
            else: #root node
                self.root = node.right
                node.right.parent = None
                self.update_balance(self.root)
        else: #case 3
            successor = tree.find_successor(node.right)
            self.remove(successor)
            successor.parent = node.parent
            if node.parent:
                if node.parent.left is node:
                    node.parent.left = successor
                else:
                    node.parent.right = successor
                self.update_balance(node.parent)
            else:
                self.root = successor
            successor.left = node.left
            if node.left:
                node.left.parent = successor
            successor.right = node.right
            if node.right:
                node.right.parent = successor
            self.update_balance(successor)
                
    def delete(self, data):
        """
        Wrapper function for deleting a value from the tree
        """
        if self.size == 1 and self.root.data == data:
            self.root = None
            self.size -= 1
        elif self.size > 1:
            node_to_remove = self._search(data, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
                return True
                
            else:
                return False
        else:
            return False
            
    def visualize(self):
        self.graph = Graph("Courses")
        self.visualize_helper(self.root)
        self.graph.render(view=True)
        
    
    def visualize_helper(self, node):
        if node is not None:
            self.graph.node(str(node.data))
            if node.has_left_child():
                self.graph.edge(str(node.data), str(node.left.data))
            if node.has_right_child():
                self.graph.edge(str(node.data), str(node.right.data))
            self.visualize_helper(node.left)
            self.visualize_helper(node.right)
                
            

def main():
    
    testTree = AVLTree()
    
    testTree.insert(131)
    testTree.insert(121)
    testTree.insert(122)
    testTree.insert(132)
    testTree.insert(115)
    testTree.insert(415)
    #testTree.insert(321)
    #testTree.insert(315)
    #testTree.insert(111)
    
    print("Pre-order:", end=' ')
    #testTree.pre_order_traversal()
    print('\n')
    
    print("Level order:", end=' ')
    testTree.level_order_traversal()
    
    print("Balance Factors of the tree's nodes:", end=' ')
    testTree.level_order_balance()
    
    #testTree.visualize()
    
    del testTree[122]
    
    print("Pre order after deleting 122:", end=' ')
    testTree.pre_order_traversal()
    print('\n')
    
    print("Level order after deleting 122:", end=' ')
    testTree.level_order_traversal()
    
    print("Balance factors of all the nodes in the tree:", end=' ')
    testTree.level_order_balance()
    
    

    
main()