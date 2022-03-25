##################################################################
# Title: Palindrome Checker Application
# Author: Srini Badri
# Version: 1.0
# Description: A program to check whether a word is a palindrome.
# Reference: https://runestone.academy/ns/books/published/pythonds/BasicDS/PalindromeChecker.html
##################################################################

from DequeClass import Deque

def palindrome_checker(aString):
    deq = Deque()

    for ch in aString:
        deq.add_rear(ch)

    print("Deque:", deq)

    stillEqual = True

    while deq.size() > 1:
        first = deq.remove_front()
        last = deq.remove_rear()
        if first != last:
            stillEqual = False
            break

    return stillEqual
    
    
def main():
    word = str(input("Enter a word: "))

    result = palindrome_checker(word)
    
    if result:
        print("The word is a Palindrome")
    else:
        print("The word is not a Palindrome")

if __name__ == "__main__":
    main()
