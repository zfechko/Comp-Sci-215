"""
Zach Fechko
Participation Activity 4 - Singly Linked Lists
"""

class Node:
    def __init__(self, data):
        """
        Node constructor
        """
        self.data = data
        self.next = None

    def get_data(self):
        """
        Returns the data of the current node
        """
        return self.data

    def set_data(self, new_data):
        """
        Overwrites the current node's data with new data
        """
        self.data = new_data

    def get_next(self):
        """
        Returns the next node in the list
        """
        return self.next

    def set_next(self, new_next):
        """
        Overwrites the next node that the current node points to
        """
        self.next = new_next

    def __str__(self):
        """
        String Representation of a node
        """
        return str(self.data)


class SLL:
    def __init__(self):
        """
        Singly Linked List constructor
        """
        self.head = None

    def add(self, item):
        """
        Inserts a new node to the front of the list
        """
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node 

    def append(self, item):
        """
        Inserts a new node to the back of the list
        """
        new_node = Node(item)
        cur = self.head
        if self.head is None:
            self.head = new_node
            return
        while cur.get_next() is not None:
            cur = cur.get_next()
        cur.set_next(new_node)

    def insert(self, item, index):
        """
        Inserts an item at a given index if it exists
        """
        new_node = Node(item)
        cur = self.head
        if index == 1:
            self.add(new_node)
            return
        elif index < 1 or index > self.size():
            print("No such index exists")
            return
        else:
            for x in range(1, index - 1):
                cur = cur.get_next()
            new_node.set_next(cur.get_next())
            cur.set_next(new_node)

    def search(self, item):
        """
        Searches for an item in the list, returns True if the item is in the list,
        False if it is not
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

    def remove(self, item):
        """
        Deletes a node with a certain data value (item), from the list if it exists
        """
        cur = self.head
        prev = None
        found = False

        while cur is not None and found is False:
            if cur.get_data() == item:
                found = True
                break
            else:
                prev = cur
                cur = cur.get_next()
        if found:
            if prev is None:
                self.head = cur.get_next()
                cur.set_next(None)
            else:
                prev.set_next(cur.get_next())
                cur.set_next(None)
        cur = prev = None

    def pop(self, index = None):
        """
        Deletes an item from the list at a given index, if no index is specified the last node of the list is deleted
        """
        cur = self.head
        prev = None
        if index is None:
            while cur.get_next() is not None: # traverses to the last node in the list
                prev = cur
                cur = cur.get_next()
            prev.set_next(None)
        else:
            for x in range(1, index - 1): # traverses the list to the desired index
                prev = cur
                cur = cur.get_next()
            prev.set_next(cur.get_next())
            cur.set_next(None)

    def is_empty(self):
        """
        Returns True if the list is empty, returns False if it is not
        """
        return self.head is None

    def size(self):
        """
        Counts the number of nodes in the list and returns that amount
        """
        cur = self.head
        count = 0
        while cur is not None:
            count = count + 1
            cur = cur.get_next()
        return count

    def __str__(self):
        """
        Instructions to print the list to the terminal
        """
        cur = self.head
        list_str = ""
        while cur is not None:
            list_str += str(cur.get_data()) + ' -> '
            cur = cur.get_next()
        cur = None
        return list_str

def main():
    """
    Wrapper function that tests all of the linked list member functions
    """
    test = SLL()
    print("Appending numbers 1 - 5")
    for x in range(1, 6):   
        test.append(x)
    print(test)

    print("Adding numbers 5 - 2")
    for x in range(2, 6):
        test.add(x)
    print(test)

    print("the list is", test.size(), "elements long")

    print("Is the list empty:", test.is_empty())

    print("Deleting the 1 in the middle")
    test.remove(1)
    print(test)

    print("Is the one in the list?", test.search(1))

    print("putting the 1 back")
    test.insert(1, 5)
    print(test)

    print("Popping the last node in the list")
    test.pop()
    print(test)

main()