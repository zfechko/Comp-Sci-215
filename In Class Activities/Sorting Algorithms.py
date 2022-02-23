
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

def merge_sort(array):
    """
    Average case time complexity: O(n log(n))
    Worst case time complexity: O(n log(n))
    Best case time complexity: Ω(n log(n))
    Space complexity: O(n)
    """
    if len(array) <= 1:
        return
    mid = len(array) // 2

    left = array[:mid].copy()
    right = array[mid:].copy()

    merge_sort(left)
    merge_sort(right)

    merge(array, left, right)



def merge(array, left_half, right_half):
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            array[k] = left_half[i]
            i = i + 1
        else:
            array[k] = right_half[j]
            j = j + 1
        k = k + 1

    while i < len(left_half):
        array[k] = left_half[i]
        i = i + 1
        k = k + 1
    while j < len(right_half):
        array[k] = right_half[j]
        j = j + 1
        k = k + 1

def partition(array, start_index, end_index):
    pivot_value = array[start_index]

    left_mark = start_index + 1
    right_mark = end_index

    while True:
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            break
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp
    array[start_index] = array[right_mark]
    array[right_mark] = pivot_value
    return right_mark

def quick_sort_helper(array, start_index, end_index):
    if start_index < end_index:
        split_point = partition(array, start_index, end_index)
        quick_sort_helper(array, start_index, split_point - 1)
        quick_sort_helper(array, split_point + 1, end_index)

def quick_sort(array):
    """
    Average Time: O(n log(n))
    Best Time: Ω(n log(n))
    Worst Time: O(n^2)
    Space: O(log(n))
    """
    quick_sort_helper(array, 0, len(array) - 1)


for i in range (1, 11):
    arr.append(random.randint(1, 50))
print(arr)
quick_sort(arr)
print(arr)
