"""
Title: Primality Test (MA2)
Author: Zach Fechko
Version: 1.0
Last Updated: Jan 19, 2022

Description: This program contains two functions, one prompts the user for an integer and then checks if it's prime, 
the other prompts the user for another integer and will sum all the integers up to that number
"""

from math import sqrt


def is_prime(n):
    """
    Given an integer n, this function runs through all the integers from 2 to the square root of n to check
    if the number is prime or not, returns true if the number is prime, and false if it's composite
    """
    for x in range(2, int(sqrt(n)) + 1): # the + 1 is protection for numbers that return a square root that rounds to 0 which makes it always return that a number is prime
        if n % x == 0:
            return False
    else:
        return True

def check_if_prime(num):
    """
    Given an integer num, this function calls is_prime() to check if the number is prime, if is_prime() returns True, then it prints "number is prime" to the terminal,
    if is_prime() returns False, it prints "number is composite" 
    """
    if is_prime(num) == True:
        print(num, "is prime")
    else:
        print(num, "is composite")

def sum_primes(num):
    """
    Given an integer num, this function will utilize the is_prime() function to check if every number in a range 1 to num is prime and then add
    that to a sum variable if is_prime() returns True, and then prints the results
    """
    sum = int(0)
    for x in range(1, num + 1):
        if is_prime(x) == True:
            sum += x
    print("The sum of primes up to", num, "is", sum)

def run_functions():
    """
    This is a wrapper function that will accept an integer input from the user and then supply that number to the check_if_prime()
    and sum_primes() functions. Contains guard code that makes sure the user inputs an integer that is greater than or equal to 2
    """
    num = 0
    while num < 2 and num is not int:
        num = int(input("Enter an integer greater than or equal to 2: "))
    check_if_prime(num)
    sum_primes(num)

run_functions()