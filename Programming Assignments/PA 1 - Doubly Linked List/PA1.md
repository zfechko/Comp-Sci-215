# Programming Assignment 1: Doubly Linked List

## Assignment Requirements
- Node Class
    - Fields: 
        - data
        - next
        - prev
    - Methods: (check off once they're complete and work)
        - [x] `__init__(self, data)`
        - [x] `get_data(self)`
        - [x] `set_data(self, new_data)`
        - [x] `get_next(self)` 
        - [x] `set_next(self, new_next)` (might need to modify to link prev)
        - [x] `get_prev(self)`
        - [x] `set_prev(self, new_prev)`
        - [x] `__str__(self)`
- Doubly Linked List Class:
    - Fields:
        - head
        - tail
    - Methods: (check off once they're complete and work)
        - [x] `__init__(self)`
        - [x] `add(self, item)`
        - [x] `search(self, item)`
        - [x] `remove(self, item)`
        - [x] `size(self)`
        - [x] `is_empty(self)`
        - [x] `__str__(self)`
        - [x] `append(self, item)` (complete but could probably optimize)
        - [x] `insert(self, index, item)` 
        - [x] `pop(self, index=None)`
        - [x] `__iter__(self)`

The implementation should also have a `main()` function that creates a doubly linked list object, calls its methods with appropriate sample data, and prints the result of each method

# Bonus
Create a circular doubly linked list class
- Circular doubly linked list class
    - Fields:
        - head
    - Methods:
        - [ ] `__init__(self)`
        - [ ] `add(self, item)`
        - [ ] `search(self, item)`
        - [ ] `remove(self, item)`
        - [ ] `size(self)`
        - [ ] `is_empty(self)`
        - [ ] `__str__(self)`
        - [ ] `append(self, item)`
        - [ ] `insert(self, index, item)`
        - [ ] `pop(self, index=None)`
        - [ ] `__iter__(self)`
