########################################################################
# Title: Binary Search Tree implementation
# Author: Srini Badri
# Version: 1.0
########################################################################



class BSTNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        if self.left_child is not None:
            return True
        else:
            return False

    def has_right_child(self):
        if self.right_child is not None:
            return True
        else:
            return False

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k,v)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self,key):
        self.delete(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def put(self, key, val):
        if self.root is None:
            self.root = BSTNode(key, val)
            self.size += 1
        else:
            self._put(key, val, self.root)

    def _put(self, key, val, current_node):
        if key == current_node.key:
            current_node.value = val
            return
        if key < current_node.key:
            #we need to go left
            if current_node.left_child is None:
                #insert here
                current_node.left_child = BSTNode(key, val, parent=current_node)
                self.size += 1
            else:
                #check the left subtree
                self._put(key, val, current_node.left_child)
        elif key > current_node.key:
            #we need to go to the right
            if current_node.right_child is None:
                #insert here
                current_node.right_child = BSTNode(key, val, parent=current_node)
                self.size += 1
            else:
                #check the right subtree
                self._put(key, val, current_node.right_child)

    def get(self, key):
        if self.root is None:
            return None
        else:
            node = self._get(key, self.root)
            if node is not None:
                return node.value
            else:
                return None

    def _get(self, key, current_node):
        if current_node is None:
            return None
        else:
            if key == current_node.key:
                return current_node
            elif key < current_node.key:
                return self._get(key, current_node.left_child)
            elif key > current_node.key:
                return self._get(key, current_node.right_child)

    def delete(self, key):
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        elif self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, data not found')

    def find_successor(self, current_node):
        if current_node.left_child is None:
            return current_node
        else:
            return self.find_successor(current_node.left_child)

    def remove(self, current_node):
        if current_node.left_child is None and current_node.right_child is None:
            if current_node is current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None

        elif current_node.left_child is not None and current_node.right_child is None:
            if current_node.parent is not None:
                if current_node.parent.left_child is current_node:
                    current_node.parent.left_child = current_node.left
                else:
                    current_node.parent.right_child = current_node.right_child
                current_node.parent.right_child = current_node.parent
            else:
                self.root = current_node.left_child
                current_node.left_child.parent = None
        
        elif current_node.left_child is None and current_node.right_child is not None:
            if current_node.parent is not None:
                if current_node.parent.left_child is current_node:
                    current_node.parent.left_child = current_node.right_child
                else:
                    current_node.parent.right_child = current_node.right_child
            else:
                self.root = current_node.right_child
                current_node.right_child.parent = None
        
        else:
            successor = self.find_successor(current_node.right_child)
            self.remove(successor)
            successor.parent = current_node.parent
            if current_node.parent:
                if current_node.parent.left_child is current_node:
                    current_node.parent.left_child = successor
                else:
                    current_node.parent.right_child = successor
            else:
                self.root = successor 
            successor.left_child = current_node.left_child
            if current_node.left_child:
                current_node.left_child.parent = successor 
            successor.right_child = current_node.right_child
            if current_node.right_child:
                current_node.right_child.parent = successor



    def pre_order_traversal(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self.pre_order_traversal_helper(self.root)
            print()

    def pre_order_traversal_helper(self, node):
        if node is None:
            return
        print(str(node.key) + ':' + node.value, end=", ")
        self.pre_order_traversal_helper(node.left_child)
        self.pre_order_traversal_helper(node.right_child)

    def level_order_traversal(self):
        if self.root is None:
            print("Empty tree")
        else:
            node_list = [self.root]
            self.level_order_helper(node_list)
            print()

    def level_order_helper(self, node_list):
        if len(node_list) > 0:
            node = node_list.pop(0)
            print(str(node.key) + ':' + node.value, end = ", ")
            if node.left_child is not None:
                node_list.append(node.left_child)
            if node.right_child is not None:
                node_list.append(node.right_child)

            self.level_order_helper(node_list)

myTree = BinarySearchTree()
myTree[215] = "Data Structures and Algorithms"
myTree[122] = "C/C++ Data Structures"
myTree[132] = "Java Data Structures"
myTree[315] = "Intro to Data Mining"
myTree[415] = "Big Data"
myTree[111] = "Intro to Programming"
myTree[115] = "Intro to Data Analytics"
myTree[121] = "C Program Design"
myTree[131] = "Java Program Design"
myTree[131] = "Java Program Design"

print("pre-order traversal:")
myTree.pre_order_traversal()
print()

print("level order traversal:")
myTree.level_order_traversal()
print()

print("course information - 215:")
print(myTree[215])
print()

# check duplicate key handling
myTree[111] = "Intro to Computer Programming"
print("\nTree after addition/update of node '111' - level-order traversal:")
myTree.level_order_traversal()

print("delete course - 115")
del myTree[115]
print()

print("pre order traversal - After delete:")
myTree.pre_order_traversal()
print()

print("level order traversal - After delete:")
myTree.level_order_traversal()
print()

print("Tree data using iterator")
for key in myTree:
    print(key, end = " ")
print()
