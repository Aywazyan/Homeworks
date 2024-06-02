# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. 
# Start with a base class called BankAccount. Then, create two subclasses, SavingsAccount and CheckingAccount. 
# Each subclass should inherit from the BankAccount class.
# The BankAccount class should have the following attributes and methods:
# Attributes: account_number, balance
# Methods: __init__ (constructor), deposit, withdraw, and get_balance
# The SavingsAccount class should inherit from BankAccount and have an additional attribute interest_rate. 
# Override the deposit method to add interest to the balance when a deposit is made.
# The CheckingAccount class should inherit from BankAccount and have an additional attribute overdraft_fee. 
# Override the withdraw method to deduct the overdraft fee if a withdrawal causes the balance to go below zero.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
            
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount + (amount * self.interest_rate)
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount + self.overdraft_fee
            return self.balance
        else:
            print("Insufficient funds")
            return self.balance

s_acc = SavingsAccount(123456789, 1000, 0.1) # 0.1 = 10%
s_acc.deposit(200)

print("Savings Account Balance:",s_acc.get_balance())
s_acc.withdraw(150)

print("Savings Account Balance:",s_acc.get_balance())

c_acc = CheckingAccount(987654321, 1500, 30)

c_acc.withdraw(100)

print("Checking Account Balance:", c_acc.get_balance())