"""
Title: Primality Test (MA2)
Author: Zach Fechko
Version: 1.0
Last Updated: Jan 19, 2022

Description: This program contains three functions, two for checking that a user chosen number is prime and another
for finding the sum of all prime numbers up to a user chosen number
"""

from math import sqrt


def is_prime(n):
    """
    Given an integer n, this function runs through all the integers from 2 to the square root of n to check
    if the number is prime or not, returns true if the number is prime, and false if it's composite
    """
    for x in range(2, int(sqrt(n)) + 1): # the + 1 is protection for numbers that return a square root that rounds to 0 which makes it always return that a number is prime
        if n % x == 0: # if the number cleanly divides with no remainder
            return False # the function returns false because the number is composite
    else: # if it doesn't divide cleanly 
        return True # the function returns true

def check_if_prime(num):
    """
    Given an integer num, this function calls is_prime() to check if the number is prime, if is_prime() returns True, then it prints "number is prime" to the terminal,
    if is_prime() returns False, it prints "number is composite" 
    """
    if is_prime(num) == True: # if is_prime() returns True
        print(num, "is prime") # it prints that the number is prime
    else: #if it returns false
        print(num, "is composite") # it prints that the number is composite

def sum_primes(num):
    """
    Given an integer num, this function will utilize the is_prime() function to check if every number in a range 1 to num is prime and then add
    that to a sum variable if is_prime() returns True, and then prints the results
    """
    sum = int(0)
    for x in range(1, num + 1): # the + 1 is for if the user chosen number is also prime and should be included
        if is_prime(x) == True:
            sum += x
    print("The sum of primes up to", num, "is", sum)

def run_functions():
    """
    This is a wrapper function that will accept an integer input from the user and then supply that number to the check_if_prime()
    and sum_primes() functions. Contains guard code that makes sure the user inputs an integer that is greater than or equal to 2 or a floating point number
    """
    num = 0
    while num < 2: #protective loop so that the user is forced to put in a number greater than or equal to 2
        num = int(float(input("Enter an integer greater than or equal to 2: "))) # nested casting so the terminal takes a float input and then converts that to an int
    check_if_prime(num) #calls the two functions above
    sum_primes(num)

run_functions()