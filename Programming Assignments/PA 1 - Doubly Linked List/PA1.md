# Programming Assignment 1: Doubly Linked List

## Assignment Requirements
- Node Class
    - Fields: 
        - data
        - next
        - prev
    - Methods: 
        - `__init__(self, data)`
        - `get_data(self)`
        - `set_data(self, new_data)`
        - `get_next(self)` 
        - `set_next(self, new_next)`
        - `get_prev(self)`
        - `set_prev(self, new_prev)`
        - `__str__(self)`
- Doubly Linked List Class:
    - Fields:
        - head
        - tail
    - Methods:
        - `__init__(self)`
        - `add(self, item)`
        - `search(self, item)`
        - `remove(self, item)`
        - `size(self)`
        - `is_empty(self)`
        - `__str__(self)`
        - `append(self, item)`
        - `insert(self, index, item)`
        - `pop(self, index=None)`
        - `__iter__(self)`
The implementation should also have a `main()` function that creates a doubly linked list object, calls its methods with appropriate sample data, and prints the result of each method

# Bonus
Create a circular doubly linked list class
- Circular doubly linked list class
    - Fields:
        - head
    - Methods:
        - `__init__(self)`
        - `add(self, item)`
        - `search(self, item)`
        - `remove(self, item)`
        - `size(self)`
        - `is_empty(self)`
        - `__str__(self)`
        - `append(self, item)`
        - `insert(self, index, item)`
        - `pop(self, index=None)`
        - `__iter__(self)`
