"""
Title: Primality Test (MA2)
Author: Zach Fechko
Version: 1.0
Last Updated: Jan 18, 2022

Description: This program contains two functions, one prompts the user for an integer and then checks if it's prime, 
the other prompts the user for another integer and will sum all the integers up to that number
"""

def is_prime():
    """
    This function prompts the user for an integer using the terminal and will determine whether that integer is a prime number
    or not
    """
    num = int(input("Please type an integer greater than or equal to 2 to check primality: ")) # prompts the user for an integer to check if it's prime
    not_prime_flag = False # this is a flag that gets set to true if the number isn't prime
    for x in range(2, num): # the function runs through every number from 2 to the number - 1 because if you include 1 then the function will always say a number isn't prime
        if num % x == 0: # if the current x divides num without any remainder
            not_prime_flag = True #the flag is set to true
            break # The loop ends as to not take up too much time complexity, even though it's still O(n)
    if not_prime_flag == True: # if the flag is set to true, which means the number isn't prime
        print(num, "is not prime because it is divisible by", x) # prints not prime to the terminal and the first number it is divisible by
    else:
        print(num, "is prime")

def sum_numbers():
    """
    This function prompts the user for an integer and will sum all integers from 1 to the chosen number and then print the result
    """
    num = int(input("Please type an integer greater than or equal to 2 to sum to: ")) # this function has two variables, one for the number to add up to and the actual sum itself
    sum = int(0)
    for x in range(num + 1): # the plus 1 makes sure that the loop actually includes the number that the user specified
        sum += x # uses the += operator to add each x to the sum
    print("the sum from 1 to", num, "is", sum) # prints the sum to the terminal

is_prime()

sum_numbers()