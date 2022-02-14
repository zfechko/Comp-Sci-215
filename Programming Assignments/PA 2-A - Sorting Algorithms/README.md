# Programming Assignment 2: Sorting Algorithms

For this assignment you should not use jupyter notebooks as tempting as it is

## Assignment Instructions

### Data Generation
- [ ] Generate sample data as Numpy ndarray using one or more numpy methods. For example, you can use `numpy.random.randint()` to generate an array of random values
- [ ] Create a linked list data set using the sample data, it would be sorted using a sorting algorithm
- [ ] Generate at least 9 different data sets (3 sample sizes with 3 lists at each size in sorted / unsorted order)

Sorted / Unsorted order:
1. An already sorted array in ascending order
2. An already sorted array in descending order
3. An unsorted array in random order

Data Size:
1. 250
2. 500
3. 1000
4. More if your computer can handle it

Note: Make sure to re-create the linked list with the same numpy ndarray for each sorting routine

### Sorting Routines
Implement the following sorting routines as either individual functions or as methods of a class
- [ ] Selection sort
- [ ] Bubble sort
- [ ] Insertion sort
- [ ] Shell sort

Each sorting routing should measure execution time, data comparison count, and data swap count metrics

### Sorting Metrics and Program Output
The program should generate metrics for each combination of the data set and sorting routine and you should writethe contents of the sorting results to a CSV file named `sort_results.csv`

### Program Flow
Write a main function that performs the following tasks. Compose the function after checking off the following items
- [ ] Generate a sample data with one of the configuration combinations (sorted/unsorted config with data size config)
- [ ] Create linked list with the sample data
- [ ] Sort the linked list using a sorting routine. It should also measure and return sorting metrics
- [ ] Store the results of the sorting metrics temporarily in a Pandas DataFrame, output the sorting metrics to a CSV file
- [ ] Repeat the process of generating the sample data, creating the list, sorting it, and outputting the metrics for each config