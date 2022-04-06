"""
Zach Fechko
This file is for the implementation of a linked list so the main .ipynb file doesn't get too clogged
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LL:
    def __init__(self):
        """
        Singly linked list constructor
        """
        self.head = None
        self.size = 0

    def __len__(self):
        """
        Helps the interpreter know what to do when it encounters len(LL)
        """
        return self.size

    def __str__(self):
        """
        String representation of the linked list
        """
        list_str = ""
        cur = self.head
        while cur is not None:
            list_str += str(cur.data) + " <--> "
            cur = cur.next
        return list_str

    def __contains__(self, value):
        return self.search(value) != -1

    def is_empty(self) -> bool:
        return self.head == None

    def add(self, data):
        """
        Inserts data at the head of the linked list
        """
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, data):
        """
        Inserts data at the end of the linked list
        """
        new_node = Node(data)
        self.size += 1
        if not self.is_empty(): #if the list is not empty
            cur = self.head
            while cur.next is not None: #traverse the list until we reach the last node in the list
                cur = cur.next 
            cur.next = new_node
        else:
            self.head = new_node

    def pop(self, index=None):
        """
        Removes a node at a specified index, if index is not given it deletes the end node
        """
        cur = self.head
        if index is None:
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
        else:
            position = 0
            prev = None
            if index == 0:
                self.head = cur.next
                cur.next = None
                return
            while position < index:
                prev = cur
                cur = cur.next
            prev.next = cur.next
            cur.next = None
        self.size -= 1

    def remove(self, data):
        """
        Removes a node in the linked list with a given data value
        """
        cur = self.head 
        prev = None
        while cur is not None:
            if cur.data == data:
                if cur is self.head: #if the node to be deleted is the head of the list
                    self.head = cur.next #move the head reference to the next node in the list
                    cur.next = None #unlink the former head
                    self.size -= 1 #decrement the size value
                    return
                else:
                    prev.next = cur.next 
                    cur.next = None
                    self.size -= 1
                    return 
            prev = cur 
            cur = cur.next
        
            
    def search(self, value) -> int:
        """
        Searches the list for a node with a given value and returns the position if it exists, 
        otherwise it returns -1
        """
        position = 0
        cur = self.head 
        while cur is not None:
            if cur.data == value:
                return position
            position += 1
            cur = cur.next
        return -1
          
    def at(self, position):
        """
        Returns the value at that position in the linked list
        """
        cur = self.head
        index = 0
        
