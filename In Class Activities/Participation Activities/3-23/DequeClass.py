##################################################################
# Title: Double-Ended Queue Implementation
# Author: Zach Fechko
# Version: 1.0
# Description: A class implementing Double-Ended Queue ADT using 
#              Python List
##################################################################

class Deque:
    '''
    A class representing a doubly-ended queue (deque).
    '''
    
    def __init__(self):
        '''
        Creates a new deque that is empty. It needs no parameters and returns an empty deque.
        '''
        self.items = []
        
    def __str__(self):
        '''
        Creates a String representation of the deque. It takes no parameters and returns a String object.
        '''
        temp_str = "Front: "
        for item in self.items:
            temp_str += str(item) + " "
        return temp_str + ":Rear"

    def is_empty(self) -> bool:
        '''
        Tests to see whether the deque is empty. It needs no parameters and returns a boolean value.          
        '''
        return self.items == []

    def add_front(self, item):
        '''
        Adds a new item to the front of the deque. It needs the item and returns nothing.          
        '''
        self.items.insert(0, item)

    def add_rear(self, item):
        '''
        Adds a new item to the rear of the deque. It needs the item and returns nothing.        
        '''
        self.items.append(item)

    def remove_front(self):
        '''
        Removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.          
        '''
        return self.items.pop(0)

    def remove_rear(self):
        '''
        Removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.        
        '''
        return self.items.pop()

    def size(self) -> int:
        '''
        Returns the number of items in the deque. It needs no parameters and returns an integer.         
        '''
        return len(self.items)

