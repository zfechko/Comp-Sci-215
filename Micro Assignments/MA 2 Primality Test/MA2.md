# Micro Assignment 2: Primality Test

## Assignment Directions

### Python Program - Part 1 
Write a program (`primality_test.py`) that prompts the user for an integer, n, where n>=2, determines if the input value is a prime number, and prints out the result. The program should handle invalid inputs and corner cases (eg. n<2) well and should not throw errors.

Within the program, define a predicate function, `is_prime(n)`, that accepts an integer argument `n` and returns True if `n` is prime, False otherwise.


Example program outputs (Part 1 only):
```
Please enter an integer >= 2: 100
100 is not prime!

Please enter an integer >= 2: 17
17 is prime!
```

### Python Program - Part 2 
Extend your previous program to compute sum of prime numbers. For this part of the solution, implement a function called `sum_primes(M)` that accepts an integer M as an argument and returns the sum of all primes from 2 to M.

Determines sum of all prime numbers from 2 to M (i.e. sum of x, such that 2 <= x <= M). 
Print the resulting sum to the console.

Example program outputs (Parts 1 & 2):
```
Please enter an integer >= 2: 100
100 is not prime!
Sum of primes from 2 to 100 is 1060!

Please enter an integer >= 2: 17
17 is prime!
Sum of primes from 2 to 17 is 58!
```


## Assignment Checklist
- [x] create `is_prime()` function
- [x] create function to display primality to terminal
- [x] create function that sums prime numbers in a range and print it to the terminal
- [x] implement guard code to prevent user from inputting a floating point/other invalid value