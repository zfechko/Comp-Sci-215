"""
Title: Amortization Table (MA3)
Author: Zach Fechko
Version: 1.0
Last Updated: Jan 25, 2022

Description:
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
        r = ((self.R / 100) / 12)
        return (r * self.P) / (1 - (1 + r) ** -(self.N * 12))

    def calculate_interest(self):
        """
        Calculates the interest payment for each month of payment
        """
        r = ((self.R / 100) / 12)
        return r * self.remaining

    def calculate_principal_payment(self):
        """
        Calculates the principal payment and returns it, using the calculate.interest() function to help
        """
        return self.monthly_payment - self.calculate_interest()

    def set_remaining_balance(self):
        """
        Sets the current balance to the new balance after payment and then returns the balance
        """
        self.remaining = self.remaining - self.calculate_principal_payment()
        return self.remaining

    def regular_schedule(self):
        """
        Creates a regular schedule of loan payment using a list of touples and returns it
        """
        tuple_list = [("month #", "starting_balance", "monthly payment", "principal payment", "interest payment", "ending principal balance")]
        for x in range(1, (self.N * 12) + 1):
            temp_tuple = (x, round(self.remaining, 2), round(self.monthly_payment, 2), round(self.calculate_principal_payment(), 2), round(self.calculate_interest(), 2), round(self.set_remaining_balance(), 2))
            tuple_list.append(temp_tuple)
        return tuple_list

    def accelerated_schedule(self, additional_payment):
        self.monthly_payment = self.monthly_payment + additional_payment
        self.remaining = self.P
        month_num = 1
        tuple_list = [("month #", "starting_balance", "monthly payment", "principal payment", "interest payment", "ending principal balance")]
        while self.remaining > 0:
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
            file.write(', ')
        file.write('\n')
    print("Regular schedule successfully written to file")
    file.close()

def write_accelerated_to_file(existing_list):
    file = open("accelerated_schedule.csv", "w")
    for x in range(len(existing_list)):
        for y in range(len(existing_list[x])):
            if x > 0 and y > 0:
                file.write('$')
            file.write(str(existing_list[x][y]))
            file.write(', ')
        file.write('\n')
    print("Accelerated schedule successfully printed to file")
    file.close()

def main():
    """
    Main function for the assignment, prompts the user for values regarding a loan and then performs Loan class 
    member functions to create two schedules, one regular, one accelerated, and prints those to two csv files
    """
    loan_purpose = input("What is this loan for? ")
    P = float(input("What is the principal loan amount? $"))
    R = float(input("What is the monthly interest rate? (enter as a percent) "))
    N = int(input("How many years are you going to pay for this loan? "))
    additional_payment = float(input("How much more per month are you willing to spend? $"))

    user_loan = Loan(P, R, N)
    regular_list = user_loan.regular_schedule()
    write_regular_to_file(regular_list)

    accelerated_list = user_loan.accelerated_schedule(additional_payment)
    write_accelerated_to_file(accelerated_list)

main()






