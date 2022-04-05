# PA 5: HashMaps

## Assignment Instructions

Implement a `HashMap` class that consists of two Python lists - the first list stores the `key` while the second list stores the `value`. The `key` and `value` should be stored in the corresponding 'slots'

The HashMap should implement **chaining** for collision handling. So each 'slot' should contain a linked list. The `key` or `value` should be added to the linked list within the slot.

Here is a summary of `HashMap` methods to define
- `HashMap()`: constructor implemented as `__init__()` method
- `__str__()` returns a string representation of the key-value pairs stored in the HashMap
- `__len__()` returns the number of key-value pairs present in the HashMap
- `__contains__(key)` checks if a key is present in the HashMap, returns True if it's found, false if it is not
- `__getitem__(key)` calls the `get(key)` method and returns the `value`
- `__setitem__(key, value)` calls `insert(key, value)`
- `__delitem__(key)` calls the `remove(key)` method
- `hash_function(key)` Applies a hash function on the key and returns its slot position. The hash function can be a simple remainder method
- `insert(key, value)` adds a key-value pair to the map and returns the corresponding value. If the key is not present in the map, `-1` is returned
- `get(key)` checks if a key exists in the map and returns the corresponding value. If the key is not present in the map, -1 is returned
- `remove(key)` removes the key-value pair from the map and returns the slot position. If the key is not found, the method returns -1

### Word Count Program
Create a simple program to read words from a text file, store the word and its count in a HashMap, and let the user check how many times a word appears

The program should contain the following:
- `map` a HashMap containing word-count pairs
- `total_count` total count of all words

Recommended program sequence:
1. Initialize `map` with the HashMap constructor and `total_count` to 0
2. Prompt the user for a text file input. Open that file for reading
3. For each word in the file:
    - Parse the word by making it lowercase and removing special characters execept for apostrophes
    - Check if the parsed word already exists in the map
    - If the parsed word does not exist, read its count, increment it by 1, and update the parsed word's count in the HashMap
    - Update `total_count` value
4. Print total count of words read from the text file.
5. Prompt the user for a word
    - If the word exists in the HashMap, retrieve its count and print it to the terminal
    - If the word does not exist, print that to the terminal
6. Continue step 5 until the user terminates the program using "Q" or "q"