"""
Zach Fechko
Version 1.0 
Last updated April 6, 2022 

Description: Implementation of a HashMap/HashTable to see how many times a word appears in a given text file
I collaborated on this assignment with Anthony Ghimpu
"""

import linkedlist
import re 

class HashMap:
    def __init__(self, size=11):
        """
        Constructor for a hashmap with default size 11
        """
        self.size = size
        self.total_count = 0
        #creates a linked list for every index in the list
        self.keys = [linkedlist.LL() for _ in range(size)] #keys stores the words
        self.values = [linkedlist.LL() for _ in range(size)] #values stores the number of times that that word appears in the text

    def __str__(self):
        """
        Returns a string representation of the key-value pairs in the map.
        Prints in the format
        slot # --> key:value -->
        """
        s = ""
        for i in range(len(self.keys)):
            s += str(i) + ' '
            pKey = self.keys[i].head
            pVal = self.values[i].head
            while pKey is not None:
                s += "-->" + ' '
                s+= str(pKey.data) + ":"+ str(pVal.data) + ' ' 
                pKey = pKey.next
                pVal = pVal.next
            s += '\n'
        return s

    def __len__(self):
        """
        returns the number of key-value pairs present in the hash map
        """
        count = 0
        for item in self.keys:
            if not item.is_empty():
                count += len(item)
        return count

    def __contains__(self, key):
        """
        checks if a key is present in the hashmap, returns true if found, false if not
        used for 'in' operator
        """
        return self.get(key) != -1

    def __getitem__(self, key):
        """
        calls the get(key) method and returns the value
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        calls the insert method
        """
        self.insert(key, value)

    def __delitem__(self, key):
        """
        calls the remove method
        """
        self.remove(key)
    
    def hash_function(self, item):
        """
        Applies a hash function on the key and returns its slot position
        """
        #return item % self.size
        key = 0
        for x in item:
            key += ord(x)
        return key % self.size
    

    def insert(self, key, value=1):
        """
        adds a key-value pair to the map and returns the corresponding value.
        If the key is not present in the map, -1 is returned
        """
        hashvalue = self.hash_function(key)
        slot_placed = -1
        if self.__contains__(key): #if the word already exists in the hashmap
            self.get(key).data += 1 #increment the key's value by 1
            self.total_count += 1 #increment total count

        else: #if the word doesn't exist in the map
            self.keys[hashvalue].append(key)
            slot_placed = hashvalue 
            if slot_placed != -1:
                self.values[slot_placed].append(value)
            self.total_count += 1
        return slot_placed

    def get(self, key):
        """
        checks if a key exists in the map and returns the corresponding node in the value list. 
        If the key is not present in the map, -1 is returned
        """
        slot = self.hash_function(key)
        if not self.keys[slot].is_empty() and not self.values[slot].is_empty():
            pKey = self.keys[slot].head
            pVal = self.values[slot].head
            while pKey is not None:
                if pKey.data == key:
                    self.keys[slot].search(key)
                    self.values[slot].search(pVal.data)
                    return pVal
                pKey = pKey.next
                pVal = pVal.next
        return -1

    def remove(self, key):
        """
        removes the key-value pair from the map and returns the slot position. 
        If the key is not found, -1 gets returned
        """
        slot = self.hash_function(key) #find the slot where the key is in the list
        if not self.keys[slot].is_empty() and not self.values[slot].is_empty(): #if the linked lists at the slots in the hashmap aren't empty
            pKey = self.keys[slot].head
            pVal = self.values[slot].head
            while pKey is not None: #using pKey here because we're looking for the string key, don't have to use pVal because parallel traversal
                if pKey.data == key:
                    self.keys[slot].remove(key) #use the linked list remove method to delete the items
                    self.values[slot].remove(pVal.data)
                    return slot
                pKey = pKey.next
                pVal = pVal.next
        return -1
    

def main():
    """
    Wrapper function to carry out assignment instructions
    """
    map = HashMap() 
    terminated = False #bool value to create a semi-infinte loop
    file_input = str(input("Enter the name of a file you would like to open: "))
    with open(file_input, "r") as file:
        for line in file:
            for word in line.split():
                s = re.sub(r"[-()\"#/@;:<>{}+=~|.!?,]", "", word.lower())
                map.insert(s)
    
    print("There are", map.total_count, "words in", file_input)

    while not terminated:
        user_input = str(input("Enter a word to search for, or enter 'Q' or 'q' to quit: "))
        if user_input == 'Q' or user_input == 'q':
            terminated = True
        else:
            if user_input not in map:
                print(user_input, "not found")
            else:
                print(user_input, "appears", map.get(user_input).data, "times")

def test_methods():
    """
    This is to test methods that aren't used in the main program, like remove.
    parses the bee movie script, prints the map, deletes "bee" and prints the map again
    """
    test = HashMap()
    with open('bee_movie.txt', "r") as file:
        for line in file:
            for word in line.split():
                s = re.sub(r"[-()\"#/@;:<>{}+=~|.!?,]", "", word.lower())
                test.insert(s)

    print(test)
    test.remove("bee")
    print()
    print(test)

main()
#test_methods() feel free to uncomment this and run it to see the functions