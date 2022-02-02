"""
Title: Programming Assignment 1, Linked Lists
Author: Zach Fechko
Version: 1.0
Last Updated: Jan 31, 2022

Description:
"""


class Node:
    def __init__(self, data):
        """
        Node constructor
        """
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        """
        Returns the data of the current node
        """
        return self.data
    
    def set_data(self, new_data):
        """
        Overwrites the current node's data
        """
        self.data = new_data

    def get_next(self):
        """
        Returns the next node in the list
        """
        return self.next

    def set_next(self, new_next):
        """
        Sets the next node of the current node to a new node
        """
        self.next = new_next

    def get_prev(self):
        """
        Returns the node before the current node
        """
        return self.prev

    def set_prev(self, new_prev):
        """
        Sets the previous pointer to the current node to a new one
        """
        self.prev = new_prev

    def __str__(self):
        """
        String representation of a node
        """
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """
        Returns true if the list is empty, false if it is not
        """
        return self.head is None
    
    def add(self, item):
        """
        Functions like insert at front, sets the item to the head node
        """
        new_node = Node(item)
        new_node.set_next(self.head)
        new_node.set_prev(None)

        if self.head is not None:
            self.head.set_prev(new_node)

        else:
            self.tail = new_node

        self.head = new_node
        

    def append(self, item):
        """
        Functions like insert at back, inserts a node to the tail of the list
        """
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.set_next(None)
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            
        
    def size(self):
        """
        Counts how many nodes are in the list and returns the amount
        """
        cur = self.head
        count = 0
        while cur is not None:
            count = count + 1
            cur = cur.get_next()
        return count

    def __str__(self):
        """
        How to print the list to the console
        """
        cur = self.head
        list_str = ""
        while cur is not None:
            list_str += str(cur.get_data()) + ' -> '
            cur = cur.get_next()
        cur = None
        return list_str

    def search(self, item):
        """
        Traverses through the list to check if item is in the list,
        returns true if the item is found, false if it is not
        """
        cur = self.head
        found = False
        while cur is not None:
            if cur.get_data() == item:
                found = True
                break
            else:
                cur = cur.get_next()
        return found

    def insert(self, item, index):
        """
        Inserts a node at a given index in the list if it exists
        """
        new_node = Node(item)
        cur = self.head
        if index == 1:
            self.add(new_node)
            return
        if index > self.size() or index < 1:
            print("Index does not exist")
            return
        else:
            for x in range(1, index - 1):
                if cur is not None:
                    cur = cur.get_next()
        new_node.set_next(cur.get_next())
        new_node.set_prev(cur)
        cur.set_next(new_node)
        if new_node.get_next() is not None:
            temp = Node(new_node.get_next())
            temp.set_prev(new_node)

    def remove(self, item):
        """
        Searches the list for an item and deletes it if that item is in the list
        """
        cur = self.head
        while cur is not None:
            if cur.get_data() == item:
                if cur == self.head:
                    self.head = cur.get_next()
            else:
                cur = cur.get_next()    




test = DoublyLinkedList()
test.add(75)
test.add(93)
test.add(102)
print(test)
test.insert(31, 1)
print(test)


    