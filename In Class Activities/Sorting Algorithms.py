import random

arr = []

def selection_sort(array):
    """
    Performs selection sort on a list/array
    Worst Case Time Complexity: O(n^2)
    Best Case Time Complexity: Ω(n^2)
    Space Complexity: O(1)
    """
    for i in range (0, len(array)):
        smallest_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
        if i != smallest_index:
            temp = array[i]
            array[i] = array[smallest_index]
            array[smallest_index] = temp

def bubble_sort(array):
    """
    Performs bubble sort on a list/array
    Worst Case Time Complexity: O(n^2)
    Best Case Time Complexity: Ω(n^2)
    Space Complexity: O(1)     
    """
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

def insertion_sort(array):
    """
    Performs insertion sort on a list/array
    Worst Case Time Complexity: O(n^2)
    Best Case Time Complexity: Ω(n)
    Space Complexity:
    """
    for i in range(1, len(array)):
  
        key = array[i]
        j = i-1
        while j >=0 and key < arr[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key

def shell_sort(array):
    """
    Performs shell sort on a list/array
    Worst Case Time Complexity: O(n(log(n))^2)
    Best Case Time Complexity: Ω(n log(n))
    Space Complexity: 
    """
    gap = len(array) // 2
    
    while (gap >= 1):
        for k in range(0, gap):
            for i in range(k + gap, len(array), gap):
                j = i

                while(j - gap) >= 0 and array[j - gap] > array[j]:
                    temp = array[j]
                    array[j] = array[j - gap]
                    array[j - gap] = temp
                    j = j - gap
            gap = gap // 2

