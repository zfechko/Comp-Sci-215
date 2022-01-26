"""
Title: Amortization Table (MA3)
Author: Zach Fechko
Version: 1.0
Last Updated: Jan 25, 2022

Description: Calculates the payment schedules of an amortized loan, one being a regular 
schedule, the other being an accelerated schedule that involves additional payment, then prints
those schedules to individual csv files
"""



class Loan:
    def __init__(self, P, R, N):
        self.P = P #principal amount
        self.R = R #monthly interest rate
        self.N = N #total years on the loan
        self.monthly_payment = self.calculate_monthly_payment()
        self.remaining = P
    
    def calculate_monthly_payment(self):
        """
        Calculates the constant monthtly payment and returns it
        """
        r = ((self.R / 100) / 12) # calculates the r variable that is specified in the assignment instructions
        return (r * self.P) / (1 - (1 + r) ** -(self.N * 12)) # using the provided equation it returns the monthly payment

    def calculate_interest(self):
        """
        Calculates the interest payment for each month of payment
        """
        r = ((self.R / 100) / 12) #calculates r
        return r * self.remaining # returns the interest

    def calculate_principal_payment(self):
        """
        Calculates the principal payment and returns it, using the calculate.interest() function to help
        """
        return self.monthly_payment - self.calculate_interest()

    def set_remaining_balance(self):
        """
        Sets the current balance to the new balance after payment and then returns the balance
        """
        self.remaining = self.remaining - self.calculate_principal_payment() #changes the remaining balance by subtracting the principal payment from the original amount
        return self.remaining #returns the new remaining balance

    def regular_schedule(self):
        """
        Creates a regular schedule of loan payment using a list of touples and returns it
        """
        tuple_list = [("month #", "starting_balance", "monthly payment", "principal payment", "interest payment", "ending principal balance")] #creates a list with a tuple for the headers of the csv/list
        for x in range(1, (self.N * 12) + 1): # for x from 1 to N in months
            temp_tuple = (x, round(self.remaining, 2), round(self.monthly_payment, 2), round(self.calculate_principal_payment(), 2), round(self.calculate_interest(), 2), round(self.set_remaining_balance(), 2)) #overwrites the temp tuple with values, rounding them to 2 decimal places
            tuple_list.append(temp_tuple) #appends the temp tuple to the main list
        return tuple_list #returns the list

    def accelerated_schedule(self, additional_payment):
        """
        Creates an accelerated schedule of loan payment using an additional payment amount specified by the user
        and then uses that number to create a list of tuples and then returns that list
        """
        self.monthly_payment = self.monthly_payment + additional_payment #adds the additional payment to get the new monthly payment amount
        self.remaining = self.P #resets the remaining balance
        month_num = 1 #counter variable for month number that gets incremented in the while loop
        tuple_list = [("month #", "starting_balance", "monthly payment", "principal payment", "interest payment", "ending principal balance")]
        while self.remaining > 0: # using a while loop because the condition for ending the loop changes because we don't know how long they'll pay
            temp_tuple = (month_num, round(self.remaining, 2), round(self.monthly_payment, 2), round(self.calculate_principal_payment(), 2), round(self.calculate_interest(), 2), round(self.set_remaining_balance(), 2))
            tuple_list.append(temp_tuple)
            month_num = month_num + 1
        return tuple_list


def write_regular_to_file(existing_list):
    """
    Writes an existing list of tuples to regular_schedule.csv
    """
    file = open("regular_schedule.csv", "w")
    for x in range(len(existing_list)):
        for y in range(len(existing_list[x])):
            if x > 0 and y > 0:
                file.write('$')
            file.write(str(existing_list[x][y]))
            file.write(',')
        file.write('\n')
    print("Regular schedule successfully written to file")
    file.close()

def write_accelerated_to_file(existing_list):
    """
    Writes an existing list of tuples to accelerated_schedule.csv
    """
    file = open("accelerated_schedule.csv", "w") #opens the csv file for writing
    for x in range(len(existing_list)):
        for y in range(len(existing_list[x])): #nested for loops for accessing each tuple and element inside the tuples
            if x > 0 and y > 0: #this is for adding the $ for the values that need it
                file.write('$')
            file.write(str(existing_list[x][y])) #writes the tuple element to the csv
            file.write(',') #adds a comma to seperate the values in the csv
        file.write('\n') #writes the new line character so that we can start a new row
    print("Accelerated schedule successfully printed to file") #success statement
    file.close() #close the file

def print_schedule(existing_list):
    """
    Prints the schedule to the screen
    """
    for x in range(len(existing_list)):
        for y in range(len(existing_list[x])):
            print(existing_list[x][y], end = '\t')
        print('\n')

def main():
    """
    Main function for the assignment, prompts the user for values regarding a loan and then performs Loan class 
    member functions to create two schedules, one regular, one accelerated, and prints those to two csv files
    """
    loan_purpose = input("What is this loan for? ")
    P = abs(float(input("What is the principal loan amount? $")))
    R = abs(float(input("What is the monthly interest rate? (enter as a percent) ")))
    N = int(input("How many years are you going to pay for this loan? "))
    additional_payment = float(input("How much more per month are you willing to spend? $"))

    user_loan = Loan(P, R, N)
    regular_list = user_loan.regular_schedule()
    write_regular_to_file(regular_list)
    print_schedule(regular_list)

    accelerated_list = user_loan.accelerated_schedule(additional_payment)
    write_accelerated_to_file(accelerated_list)
    print_schedule(accelerated_list)

main()






