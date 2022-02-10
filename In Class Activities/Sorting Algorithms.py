def selection_sort(array):
    """
    Time Complexity: O(n^2)
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

