###
# Binary Heap Implementation
# Author: Srini Badri
# Version: 1.0
###

import sys

class BinaryHeap:
    '''

    '''
    def __init__(self):
        '''
        heap_list[0] = 0 is a dummy value (not used)
        '''
        self.heap_list = [0]
        self.size = 0

    def __str__(self):
        '''
        string representation of the heap
        '''
        return str(self.heap_list)

    def __len__(self):
        '''
        how to use len(BinaryHeap())
        '''
        return self.size

    def __contains__(self, item):
        '''
        helps the compiler know how to handle 
        '''
        return item in self.heap_list

    def is_empty(self):
        '''
        compare the size attribute to 0
        '''
        return self.size == 0

    def find_min(self):
        '''
        the smallest item is at the root node (index 1)
        '''
        if self.size > 0:
            min_val = self.heap_list[1]
            return min_val
        return None

    def insert(self, item):
        '''
        append the item to the end of the list (maintains complete tree property)
        violates the heap order property
        call percolate up to move the new item up to restore the heap order property
        '''
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def del_min(self):
        '''
        min item in the tree is at the root
        replace the root with the last item in the list (maintains complete tree property)
        violates the heap order property
        call percolate down to move the new root down to restore the heap property
        '''
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size = self.size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_val

    def min_child(self, index):
        '''
        return the index of the smallest child
        if there is no right child, return the left child
        if there are two children, return the smallest of the two
        '''
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def build_heap(self, alist):
        '''
        build a heap from a list of keys to establish complete tree property
        starting with the first non leaf node
        percolate each node down to establish heap order property
        '''
        index = len(alist) // 2 # any nodes past the half way point are leaves
        self.size = len(alist)
        self.heap_list = [0] + alist[:]
        while (index > 0):
            self.percolate_down(index)
            index -= 1

    def percolate_up(self, index):
        '''
        compare the item at index with its parent
        if the item is less than its parent, swap!
        continue comparing until we hit the top of tree
        (can stop once an item is swapped into a position where it is greater than its parent)
        '''
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index //= 2

    def percolate_down(self, index):
        '''
        compare the item at index with its smallest child
        if the item is greater than its smallest child, swap!
        continue continue while there are children to compare with
        (can stop once an item is swapped into a position where it is less than both children)
        '''
        while (index * 2) <= self.size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc

    def remove(self, item):
        '''
        remove an item from the heap. The item may not be at the root of the heap.
        '''
        if self.is_empty():
            return None 
        elif item not in self.heap_list:
            return None
        else:
            item_index = -1
            for n in self.heap_list:
                if n == item:
                    item_index = self.heap_list.index(n)
                    break
            if item_index != -1:
                self.heap_list[item_index] = -sys.maxsize-1
                self.percolate_up(item_index)
                self.del_min()
                
        
