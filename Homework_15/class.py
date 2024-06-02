# Define a class named BankAccount with an __init__ method that initializes two instance variables: 
# account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as an argument
# and updates the account balance accordingly. 
# These methods also include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance of $1000.
# We deposit $500 and withdraw $200 from the account and print the account information.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.balance

account1 = BankAccount("Petros Petrosyan", 1000)

print(f"Balance = ${account1.balance}")

try:
    account1.deposit(int(input("Enter deposit amount : ")))
except:
    raise Exception("No letters or symbols allowed. \n Please try again")

print(f"Balance = ${account1.balance}")

try:
    account1.withdraw(int(input("Enter withdraw amount : ")))
except:
    raise Exception("No letters or symbols allowed. \n Please try again")

print("Account holder:", account1.account_holder)
print("Account balance:", account1.get_balance())
