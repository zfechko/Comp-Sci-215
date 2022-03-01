class Node:
    def __init__(self, data):
        """
        Node constructor
        """
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        """
        String representation of a node
        """
        return str(self.data)
    
    
class DLL:
    def __init__(self):
        """
        Doubly linked list constructor
        """
        self.head = None
        self.tail = None
        self.swaps = 0 
        self.comparisons = 0
        
    def __str__(self):
         """
         How to print the list to the console
         """
         cur = self.head
         list_str = ""
         while cur is not None:
             list_str += str(cur.data)
             if cur != self.tail:
                 list_str += '<-->'
             cur = cur.next
         cur = None
         return list_str
        
    def is_empty(self):
        """
        Returns True if the list is empty, False if it is not
        """
        return self.head is None
    
    def size(self):
        """
        Returns the number of nodes in the list
        """
        cur = self.head
        count = 0
        while cur is not None:
            count = count + 1
            cur = cur.next
        return count
    
    def add(self, item):
        """
        Adds a new node to the front of the list
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
        Adds a new node to the end of the list
        """
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def merge(self, first, second):
        """
        Merges split lists back together
        """
        if first is None:
            return second
        if second is None:
            return first
        
        if first.data < second.data:
            self.comparisons += 1
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            self.swaps += 1
            return first
            
        else:
            self.comparisons += 1
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            self.swaps += 1
            return second
        
    def split(self, temp_head):
        """
        Splits the lists by using one fast pointer and one slow pointer
        """
        fast = slow = temp_head
        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp
    
    def merge_sort(self, temp_head):
        """
        wrapper function that performs merge sort
        """
        if temp_head is None:
            return temp_head
        if temp_head.next is None:
            return temp_head
        
        second = self.split(temp_head)
        temp_head = self.merge_sort(temp_head)
        second = self.merge_sort(second)
        
        return self.merge(temp_head, second)
   
    
    
        