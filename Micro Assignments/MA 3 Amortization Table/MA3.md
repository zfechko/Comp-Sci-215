# Micro Assignment 3: Amortization Table

## Assignment Instructions
1. Define class `Loan` with the following fields and methods
    - `P` (field): original principal amount on the loan
    - `R` (field): monthly interest rate of the loan
    - `N` (field): number of total years on the loan
    - `regular_schedule()` (method):  Returns the amortization schedule as a list of tuples (which is a list where each element is a tuple). Each item in the list is a tuple of (month number, starting principal balance, monthly payment, principal payment, interest payment and ending principal balance). The number of items in the list should be same as the number of months for the loan.
    - `accelerated_schedule(amount)` (method): Returns the accelerated amortization schedule as a list of tuples. Each item in the list is a tuple of (month number, starting principal balance, monthly payment, principal payment, interest payment and ending principal balance). The number of items in the list sould be less than or equal to the number of months for the loan. Be sure to slice the list before returning to items with zero (0) balance are trucated.

2. Define main program to prompt the user for:
    - What the loan is for(eg. home)
    - Principal loan amount (eg. 500000)
    - Yearly interest rate of the loan as a percent
    - Number of years of the loan
    -Additional amount per month for accelerated schedule

3. Create an instance of `Loan` class with the computed P, R, and N values. Note that R is the interest rate, and N is the number of months. Call `regular_schedule()` and `accelerated_schedule(amount)` to obtain the schedule as a list of tuples

4. Write loan payment schedule to a CSV file:
    - Write header row with column names seperated by tab ('\t')
    - Write each tuple from the list with elements seperated by tab
    - Write results from `regular_schedule()` and `accelerated_schedule(amount)` to different csv files

5. Code to display the loan repayment schedule

## To-Do List
- [x] create a function that correctly calculates monthly payments
- [x] create a function that correctly calculates interest and principal payments 
- [x] create `regular_schedule()` function that returns a list of tuples
- [x] create `accelerated_schedule(amount)` function that returns a list of tuples
- [x] figure out how to print each list of tuples to a csv file
- [x] create `main()` function that wraps all the functions into one smooth process
- [x] figure out a way to update remaining principal without actually changing the member value