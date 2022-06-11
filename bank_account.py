import re


class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "First National Dojo"
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
account1 = BankAccount(0.01, 10)
account2 = BankAccount(0.02, 30)
account1.deposit(100).deposit(20).deposit(800).withdraw(20).yield_interest().display_account_info()
account2.deposit(90).deposit(90).withdraw(80).withdraw(7).yield_interest().display_account_info()
