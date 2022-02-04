"""
Title: Programming Assignment 1, Linked Lists
Author: Zach Fechko
Version: 1.0
Last Updated: Feb 3, 2022

Description: This program uses node and doubly linked list classes to demonstrate list functions
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

class LLIterator:
    def __init__(self, head):
        """
        Iterator constructor
        """
        self.cur = head
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is not None:
            item = self.cur.get_data()
            self.cur = self.cur.get_next()
            return item
        else:
            raise StopIteration

class DoublyLinkedList:
    def __init__(self):
        """
        Doubly linked list constructor
        """
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
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

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
            new_node.next = None
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
            list_str += str(cur.get_data()) + ' <--> '
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
        cur = None
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
            new_node.get_next().set_prev(new_node)
        cur = None


    def remove(self, item):
        """
        Searches the list for an item and deletes it if that item is in the list
        """
        cur = self.head
        prev = None
        found = False
        while cur is not None and not found:
            if cur.get_data() == item:
               found = True
               break
            else:
                prev = cur
                cur = cur.get_next()   
        if found and cur is not None:
            if prev == None:
                self.head = cur.get_next() 
                if cur.get_next() is not None:
                    cur.next.set_prev(None)
                cur.set_next(None)
            else:
                prev.set_next(cur.get_next())
                if cur.get_next() is not None:
                    cur.next.set_prev(prev)
                cur.set_next(None)
                cur.set_prev(None)
        cur = prev = None

    def pop(self, index = None):
        """
        Deletes a node from the list, if an index is given, the function will delete at that index,
        otherwise it deletes from the end
        """
        cur = self.head
        if index is None:
            while cur.get_next() is not None:
                cur = cur.get_next()
            self.tail = cur.get_prev()
            self.tail.set_next(None)
            cur.set_prev(None)
        else:
            if index == 1:
                self.head = self.head.get_next()
                cur.set_next(None)
                self.head.set_prev(None)
            else:
                for x in range(1, index):
                    cur = cur.get_next()
                cur.get_prev().set_next(cur.get_next())
                cur.get_next().set_prev(cur.get_prev())
                cur.set_next(None)
                cur.set_prev(None)
        cur = None

    def __iter__(self):
        """
        Iterator using an iterator object
        """
        return LLIterator(self.head)

def main():
    """
    Wrapper function that will demonstrate all of the doubly linked list functions
    """
    test = DoublyLinkedList()
    print("Adding 1 - 5 to the start of the list:")
    for x in range(5, 0, -1):
        test.add(x)
        print(test)
    print('\n')

    print("Appending 6 - 10 to the end of the list:")
    for x in range(6, 11):
        test.append(x)
        print(test)
    print('\n')

    print("Is this list empty?", test.is_empty())
    print('\n')

    print("The list is", test.size(), "nodes long.")
    print('\n')

    print("Removing the 5 in the middle of the list")
    test.remove(5)
    print(test)
    print('\n')

    print("Is the 5 in the list?", test.search(5))
    print('\n')
                
    print("Putting the 5 back in the middle")
    test.insert(5, 5)
    print(test)
    print("Is the 5 back in the list?", test.search(1))        
    print('\n')

    print("Popping the last element in the list")
    test.pop()
    print(test)
    print("Popping the first element in the list")
    test.pop(1)
    print(test)

    print("Printing the list using the iterator")
    for item in test:
        print(item, end=', ')
            
main()        


           

            
            


