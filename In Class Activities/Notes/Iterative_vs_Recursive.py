
def iterative_binary_search(alist, target):
    """
    Iterative implementation of binary search
    Time complexity: O(log(n))
    """
    start = 0
    end = len(alist) - 1
    mid = 0

    while start <= end:
        mid = (start + end) // 2
        if alist[mid] < target:
            low = mid + 1
        elif alist[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1


def recursive_binary_search(alist, target, start, end):
    """
    Recursive implementation of binary search
    Time Complexity: O(log2(n))
    """
    if start > end:
        return -1
    mid = (start + end) // 2
    if alist[mid] == target:
        return mid
    elif alist[mid] < target:
        return recursive_binary_search(alist, target, mid + 1, end)
    else:
        return recursive_binary_search(alist, target, start, mid - 1)

    
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(recursive_binary_search(array, 6, 0, len(array) - 1))