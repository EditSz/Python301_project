import random
import sys

class Bank_Account():
    def __init__ (self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_details(self):
        print("\n-------------ACCOUNT DETAILS------------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available Balance: {self.balance} €\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Your current account balance is: {self.balance} €")
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds!")
            print(f"Your balance is only {self.balance} €.")
            print("Try to withdraw less than your balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"{amount} € successful withdrawal from the bank account!")
            print(f"Current balance after the withdrawal is: {self.balance} €")
            print()
    
    def check_balance(self):
        print(f"Available balance is: {self.balance} €")
        print()

    def options(self):
        print( """
             OPTIONS
        *********************
        Menu:
        1. Account Details
        2. Check Balance
        3. Deposit
        4. Withdraw
        5. Exit
        **********************
        """)

        while True:
            try:
                option = int(input("Please choose an option(1-5)!: "))
            except:
                print("Something went wrong. Please try again and choose an option (1-5)!: ")
                continue
            else:
                if option == 1:
                    account.account_details()
                elif option == 2:
                    account.check_balance()
                elif option == 3:
                    amount = float(input("How much do you want to deposit?: "))
                    account.deposit(amount)
                elif option == 4:
                    amount = float(input("How much do you want to withdraw?: "))
                    account.withdraw(amount)
                elif option == 5:
                    print("\nTransaction complete. Thank you for choosing us!\n ")
                    
                    sys.exit()

print("\n******** WELCOME IN THE SIMPLE BANK SYSTEM ********")
print("__________________________________________________\n")
print("------------CREATE YOUR ACCOUNT----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Your account created successfully! \n")

account = Bank_Account(name, account_number)

while True:
    trans = input("Do you want to do any transaction? (y/n): ")
    if trans == "y":
        account.options()
    elif trans == "n":
        print("""
        *** Thank you for choosing our services! ***
        **** We are waiting for you back! ****
        """)
        break
    else:
        print("Invalid aciton! Please enter 'y' or 'n'!")

