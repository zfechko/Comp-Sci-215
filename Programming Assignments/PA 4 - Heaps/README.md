# PA 4 - Heaps

## Assignment Overview
For this assignment you are going to leverage your understanding of a Binary Min Heap to implement:
- Binary Max Heap
- Ternary Max Heap

### Binary Max Heap
Modify the implementation code for Binary Min Heaps so that the item with the maximum value is at the top of the heap

### Testing your Binary Max Heap
Test your implementation by building the binary max heap with sample data. The test should show building of the binary max heap with individual data values as well as with a list of data values

### Ternary (3-) Max Heap
The Heap can be further improved by making it a `d-ary` Heap, a general Heap with `d` children instead of 2. In this part of the assignment, you will implement a ternary max heap where the item with maximum value is at the top of the heap.

Assuming the Ternary Heap root is at index 1, the relation between a node, its parent and its children can be computed as
- Node(index):
    - i(i > 1)
- Parent of the Node (index):
    - floor((i - 2) / 3) + 1
- Children of the Node (indices)
    - 3 * i - 1
    - 3 * i
    - 3 * i + 1

### Testing your Ternary Max Heap
Once again, test your implementation by building the Ternary Max Heap with sample data. The test should show building of Ternary Max Heap with individual data items as well as with a list of data items - similar to the test code in notes.

Though this is not required, you may improvise the test by adding a set of random numbers, and removing and printing out the items in the order of their priorities.

### Classes to define
- Define class `BinaryMaxHeap`. The methods should match closely to the Binary Min Heap implementation code provided in lecture notes
- Define class `TernaryMaxHeap`. The methods should match closely to the Binary Min Heap implementation code provided in lecture notes

### Bonus
Use `graphviz` to visualize the heap