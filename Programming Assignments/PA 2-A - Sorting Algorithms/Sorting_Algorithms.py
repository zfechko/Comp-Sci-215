"""
Title: Programming Assignment 2, Sorting Algorithms
Author: Zach Fechko
Version: 1.0
Last Updated: Feb 14, 2022

Description: This program uses doubly linked lists to test the efficiency of sorting algorithms
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from numpy import random

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
            
    def pop(self):
        """
        Removes the last node in the list
        """
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        self.tail = cur.prev
        self.tail.next = None
        cur.prev = None
        cur = None
        
    def __str__(self):
        """
        How to print the list to the console
        """
        cur = self.head
        list_str = ""
        while cur is not None:
            list_str += str(cur.data) + ' <--> '
            cur = cur.next
        cur = None
        return list_str
    
    def clear_list(self):
        """
        Deletes a list by popping every element
        """
        for x in range(self.size()):
            self.pop()
        
        
def swap_data(node_1, node_2):
    """
    Swaps the data of two nodes
    """
    value = node_1.data
    node_1.data = node_2.data
    node_2.data = value
        
def selection_sort(list, data_dict):
    """
    Performs selection sort on a doubly linked list
    What I still need to add:
        - Measure of time
        - Measure of # of swaps
        - Measure of # of comparisons
    """
    start = time.time()
    swaps = 0 
    comparisons = 0
    if list.is_empty() is True: #checks for empty list
        return

    cur_i = list.head
    while(cur_i is not None):
        cur_sm = cur_i
        cur_j = cur_i.next
        
        while cur_j is not None:
            if cur_j.data < cur_sm.data:
                comparisons = comparisons + 1
                cur_sm = cur_j
            cur_j = cur_j.next
            
        if cur_i is not cur_sm:
            swap_data(cur_i, cur_sm)
            temp = cur_i
            cur_i = cur_sm
            cur_sm = temp
            swaps = swaps + 1
        cur_i = cur_i.next
    end = time.time()
    runtime = end - start
    data_dict["Runtime_selection"].append(runtime)
    data_dict["Data Comparisons_selection"].append(comparisons)
    data_dict["Data Swaps_selection"].append(swaps)
    
    
def insertion_sort(list, data_dict):
    """
    Performs insertion sort on a doubly linked list
    What I still need to add:
        - Measure of time
        - Measure of # of swaps
        - Measure of # of comparisons
    """
    start = time.time()
    swaps = 0 
    comparisons = 0
    if list.is_empty() is True: #checks for empty list
        return
    
    front = list.head
    back = None
    while front != None:
        back = front.next
        while back != None and back.prev != None and back.data < back.prev.data:
            comparisons = comparisons + 1
            swap_data(back, back.prev)
            swaps = swaps + 1
            back = back.prev
        front = front.next
    end = time.time()
    runtime = end - start
    data_dict["Runtime_insertion"].append(runtime)
    data_dict["Data Swaps_insertion"].append(swaps)
    data_dict["Data Comparisons_insertion"].append(comparisons)
    
    
def bubble_sort(list, data_dict):
    """
    Performs bubble sort on a doubly linked list
    """
    start = time.time()
    comparisons = 0 
    swaps = 0 
    swapped = 0
    j = None
    
    if list.is_empty() is True: #checks for empty list
        return
    
    while True:
        swapped = 0 
        i = list.head
        while i.next != j:
            if i.data > i.next.data:
                comparisons += 1
                swap_data(i, i.next)
                swaps += 1
                swapped = 1 
            else:
                comparisons += 1
            i = i.next 
        j = i 
        if swapped == 0:
            break
    end = time.time()
    runtime = end - start
    data_dict["Runtime_bubble"].append(runtime)
    data_dict["Data Comparisons_bubble"].append(comparisons)
    data_dict["Data Swaps_bubble"].append(swaps)
    
    
def shell_sort(list):
    n = list.size() - 1 
    gap = n // 2
    
def measure_selection_sort(size, sorted_values, random_values, data_dict):
    """
    Runs all the tests on selection sort, making the lists, sorting, and adding to the dictionary
    """
    ascending_list = DLL()
    descending_list = DLL()
    random_list = DLL()
    
    for x in range(1, size + 1):
        ascending_list.append(sorted_values[x])
        descending_list.add(sorted_values[x])
        random_list.append(random_values[x])
        
    selection_sort(ascending_list, data_dict)
    data_dict["List Size"].append("Ascending Sorted " + str(ascending_list.size()))
    selection_sort(descending_list, data_dict)
    data_dict["List Size"].append("Descending Sorted " + str(descending_list.size()))
    selection_sort(random_list, data_dict)
    data_dict["List Size"].append("Random Order " + str(random_list.size()))

def measure_insertion_sort(size, sorted_values, random_values, data_dict):
    ascending_list = DLL()
    descending_list = DLL()
    random_list = DLL()
    
    for x in range(1, size + 1):
       ascending_list.append(sorted_values[x])
       descending_list.add(sorted_values[x])
       random_list.append(random_values[x]) 

    insertion_sort(ascending_list, data_dict)
    data_dict["List Size"].append("Ascending Sorted " + str(ascending_list.size()))
    insertion_sort(descending_list, data_dict)
    data_dict["List Size"].append("Descending Sorted " + str(descending_list.size()))
    insertion_sort(random_list, data_dict)
    data_dict["List Size"].append("Random Order " + str(random_list.size()))

def measure_bubble_sort(size, sorted_values, random_values, data_dict):
    ascending_list = DLL()
    descending_list = DLL()
    random_list = DLL()
    
    for x in range(1, size + 1):
       ascending_list.append(sorted_values[x])
       descending_list.add(sorted_values[x])
       random_list.append(random_values[x]) 

    bubble_sort(ascending_list, data_dict)
    data_dict["List Size"].append("Ascending Sorted " + str(ascending_list.size()))
    bubble_sort(descending_list, data_dict)
    data_dict["List Size"].append("Descending Sorted " + str(descending_list.size()))
    bubble_sort(random_list, data_dict)
    data_dict["List Size"].append("Random Order " + str(random_list.size()))

def main():
    """
    Wrapper function that performs the program flow per the instructions
    """
       
    selection_data = {
            "List Size": [],
            "Runtime_selection": [],
            "Data Comparisons_selection": [],
            "Data Swaps_selection": []
            }
    insertion_data = {
        "List Size": [],
        "Runtime_insertion": [],
        "Data Comparisons_insertion": [],
        "Data Swaps_insertion": []
            }
    bubble_data = {
        "List Size": [],
        "Runtime_bubble": [],
        "Data Comparisons_bubble": [],
        "Data Swaps_bubble": []
            }
    shell_data = {
        "List Size" :[],
        "Runtime": [],
        "Data Comparisons": [],
        "Data Swaps": []
            }
   
    sample_size = [250, 500, 1000] #determining the size to be added to the list
    sorted_values = np.arange(1001) #using the max size just to have an array of all values
    random_values = random.randint(1000, size=(1001)) #numpy array of 1500 random numbers from 0-1500
    for value in sample_size:
        measure_bubble_sort(value, sorted_values, random_values, bubble_data)
        measure_selection_sort(value, sorted_values, random_values, selection_data)
        measure_insertion_sort(value, sorted_values, random_values, insertion_data)
    bubble_df = pd.DataFrame.from_dict(bubble_data).set_index('List Size')
    selection_df = pd.DataFrame.from_dict(selection_data).set_index('List Size')
    insertion_df = pd.DataFrame.from_dict(insertion_data).set_index('List Size')
    merged_df = pd.merge(selection_df, insertion_df, on='List Size')
    merged_df = pd.merge(merged_df, bubble_df, on='List Size')
    merged_df = merged_df.sort_index()
    print(merged_df)
main()
            
