"""
Title: Programming Assignment 2-B, Divide and Conquer Sorting Algorithms
Author: Zach Fechko
Version: 1.0
Last Updated: Feb 27, 2022

Description: This program uses doubly linked lists to test the efficiency of sorting algorithms
"""

import linked_list
import timeit
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt


def swap_data(node_1, node_2):
    """
    Swaps the data of two nodes
    """
    temp = node_1.data 
    node_1.data = node_2.data 
    node_2.data = temp
    
def partition(left, right, ll):
    pivot = right.data
    i = left.prev
    j = left
    
    while j != right:
        if j.data <= pivot:
            ll.comparisons += 1
            if i == None:
                i = left
            else:
                i = i.next
            swap_data(i, j) 
            ll.swaps += 1
        j = j.next
    if i == None:
         i = left
    else:
        i = i.next
    swap_data(i, right)
    ll.swaps += 1
    return i

def quick_sort_helper(l, h, ll):
    if h != None and l != h and l != h.next:
        temp = partition(l, h, ll)
        quick_sort_helper(l, temp.prev, ll)
        quick_sort_helper(temp.next, h, ll)

def quick_sort(ll):
    """
   Performs quicksort on the linked list
    """
    node = ll.tail
    quick_sort_helper(ll.head, node, ll)
    
def measure_merge_sort(size, sorted_values, random_values, data_dict):
    """
    Runs all the tests on merge sort    
    """
    ascending_list = linked_list.DLL()
    descending_list = linked_list.DLL()
    random_list = linked_list.DLL()
    for x in range(1, size + 1):
        ascending_list.append(sorted_values[x])
        descending_list.add(sorted_values[x])
        random_list.append(random_values[x])
        
    runtime = timeit.timeit(lambda:merge_wrapper(ascending_list), number=1)
    data_dict["list type"].append("ascending sorted " + str(ascending_list.size()))
    data_dict["runtime"].append(runtime)
    data_dict["comparisons"].append(ascending_list.comparisons)
    data_dict["data swaps"].append(ascending_list.swaps)
    
    runtime = timeit.timeit(lambda:merge_wrapper(descending_list), number=1)
    data_dict["list type"].append("descending sorted " + str(descending_list.size()))
    data_dict["runtime"].append(runtime)
    data_dict["comparisons"].append(descending_list.comparisons)
    data_dict["data swaps"].append(descending_list.swaps)
    
    runtime = timeit.timeit(lambda:merge_wrapper(random_list), number=1)
    data_dict["list type"].append("random sorted " + str(random_list.size()))
    data_dict["runtime"].append(runtime)
    data_dict["comparisons"].append(random_list.comparisons)
    data_dict["data swaps"].append(random_list.swaps)
    
def measure_quick_sort(size, sorted_values, random_values, data_dict):
    ascending = linked_list.DLL()
    descending = linked_list.DLL()
    random_list = linked_list.DLL()
    for x in range (1, size + 1):
        ascending.append(sorted_values[x])
        descending.add(sorted_values[x])
        random_list.append(random_values[x])
        
    runtime = timeit.timeit(lambda:quick_sort(ascending), number=1)
    data_dict["list type"].append("ascending sorted " + str(ascending.size()))
    data_dict["runtime"].append(runtime)
    data_dict["comparisons"].append(ascending.comparisons)
    data_dict["data swaps"].append(ascending.swaps)
    
    runtime = timeit.timeit(lambda:quick_sort(descending), number=1)
    data_dict["list type"].append("descending sorted " + str(descending.size()))
    data_dict["runtime"].append(runtime)
    data_dict["comparisons"].append(descending.comparisons)
    data_dict["data swaps"].append(descending.swaps)
    
    runtime = timeit.timeit(lambda:quick_sort(random_list), number=1)
    data_dict["list type"].append("random sorted " + str(random_list.size()))
    data_dict["runtime"].append(runtime)
    data_dict["comparisons"].append(random_list.comparisons)
    data_dict["data swaps"].append(random_list.swaps)
    
    
    
def merge_wrapper(ll):    
    ll.head = ll.merge_sort(ll.head)
    
    
    
def main():
    """
    Wrapper function that does all the things that are required in the directions
    """
    sizes = [250, 500, 1000]
    sorted_values = np.arange(1001)
    random_values = random.randint(1000, size=(1001))
    merge_data = {
        "list type": [],
        "runtime": [],
        "comparisons": [],
        "data swaps": []
        }
    quick_data = {
        "list type": [],
        "runtime": [],
        "comparisons": [],
        "data swaps": []
        }
    for size in sizes:
      measure_merge_sort(size, sorted_values, random_values, merge_data)
      measure_quick_sort(size, sorted_values, random_values, quick_data)
     
    merge_df = pd.DataFrame.from_dict(merge_data).set_index('list type')
    quick_df = pd.DataFrame.from_dict(quick_data).set_index('list type')
   
    
    combined_df = merge_df.join(quick_df, on='list type', lsuffix='_merge', rsuffix='_quick')
    combined_df.to_csv(r'sorted_results.csv', encoding='utf-8')
    
    x_labels = [250, 500, 1000]
    x_locs = np.arange(1,4)
    descending_merge_runtime = pd.Series([combined_df.loc["descending sorted 250", "runtime_merge"],
                                         combined_df.loc["descending sorted 500", "runtime_merge"],
                                         combined_df.loc["descending sorted 1000", "runtime_merge"]],
                                         index=[250, 500, 1000], name="Merge Sort")
    
    descending_quick_runtime = pd.Series([combined_df.loc["descending sorted 250", "runtime_quick"],
                                         combined_df.loc["descending sorted 500", "runtime_quick"],
                                         combined_df.loc["descending sorted 1000", "runtime_quick"]],
                                         index=[250, 500, 1000], name="Quick Sort")
    
    random_merge_runtime = pd.Series([combined_df.loc["random sorted 250", "runtime_merge"],
                                         combined_df.loc["random sorted 500", "runtime_merge"],
                                         combined_df.loc["random sorted 1000", "runtime_merge"]],
                                         index=[250, 500, 1000], name="Merge Sort")
    
    random_quick_runtime = pd.Series([combined_df.loc["random sorted 250", "runtime_quick"],
                                         combined_df.loc["random sorted 500", "runtime_quick"],
                                         combined_df.loc["random sorted 1000", "runtime_quick"]],
                                         index=[250, 500, 1000], name="Quick Sort")
    
    random_series = [random_merge_runtime, random_quick_runtime]
    descending = [descending_merge_runtime, descending_quick_runtime]
    
    f, ax = plt.subplots()
    ax.set_title("Descending Sorted")
    ax.set_ylabel("Runtime")
    ax.set_xlabel("List Size N")
    ax.set_xticklabels(x_labels)
    ax.set_xticks(x_locs)
    for series in descending:
        plt.plot(x_locs, series, label=series.name)
    plt.legend(loc=0)
    plt.show()
    
    ax.set_title("Random Sorted")
    ax.set_ylabel("Runtime")
    ax.set_xlabel("List Size N")
    ax.set_xticklabels(x_labels)
    ax.set_xticks(x_locs)
    for series in random_series:
        plt.plot(x_locs, series, label=series.name)
    plt.legend(loc=0)
    plt.show()

main()

