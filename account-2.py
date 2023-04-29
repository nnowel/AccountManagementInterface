class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance
        
    def __str__(self):
        return f"Account {self.account_id}: balance {self.balance}"
        
class Checking(Account):
    def __init__(self, account_id, balance):
        super().__init__(account_id, balance)
        self.interest = 0
        
class Savings(Account):
    def __init__(self, account_id, balance):
        super().__init__(account_id, balance)
        self.interest = 0.01
        
class Credit(Account):
    def __init__(self, account_id, balance, credit_limit):
        super().__init__(account_id, balance)
        self.credit_limit = credit_limit
        self.interest = 0.3
        
    def set_balance(self, new_balance):
        if new_balance > self.credit_limit:
            print("Error: balance exceeds credit limit")
        else:
            self.balance = new_balance
        
    def __str__(self):
        return f"Credit account {self.account_id}: balance {self.balance}, credit limit {self.credit_limit}"
        
class Customer:
    def __init__(self, username, checking, savings, credit):
        self.username = username
        self.checking = checking
        self.savings = savings
        self.credit = credit
import csv


filename = input("Enter the name of the csv file: ")
with open(filename, "r") as file:
    reader = csv.reader(file)
    customers = reader
def import_from_csv():
    
    next(reader)  # Skip header row
    for row in reader:
        checking = Checking(row[0], float(row[1]))
        savings = Savings(row[0], float(row[2]))
        credit = Credit(row[0], float(row[3]), float(row[4]))
        customer = Customer(row[5], checking, savings, credit)
        customers.append(customer)

def view_customers():
    for customer in customers:
        print(customer)
        print(customer.checking)
        print(customer.savings)
        print(customer.credit)

def deposit():
    customer = select_customer()
    account_type = input("Enter the account type (checking/savings): ")
    amount = float(input("Enter the amount to deposit: "))
    if account_type == "checking":
        customer.checking.deposit(amount)
    elif account_type == "savings":
        customer.savings.deposit(amount)
    else:
        print("Invalid account type")

def withdraw():
    customer = select_customer()
    account_type = input("Enter the account type (checking/savings): ")
    amount = float(input("Enter the amount to withdraw: "))
    if account_type == "checking":
        try:
            customer.checking.withdraw(amount)
        except ValueError as e:
            print(str(e))
    elif account_type == "savings":
        try:
            customer.savings.withdraw(amount)
        except ValueError as e:
            print(str(e))
    else:
        print("Invalid account type")

def credit_card_charge():
    customer = select_customer()
    amount = float(input("Enter the amount to charge: "))
    try:
        customer.credit.set_balance(customer.credit.balance + amount)
    except ValueError as e:
        print(str(e))

def credit_card_payment():
    customer = select_customer()
    account_type = input("Enter the account type (checking/savings): ")
    amount = float(input("Enter the amount to pay: "))
    if account_type == "checking":
        try:
            customer.checking.withdraw(amount)
            customer.credit.set_balance(customer.credit.balance - amount)
        except ValueError as e:
            print(str(e))
    elif account_type == "savings":
        try:
            customer.savings.withdraw(amount)
            customer.credit.set_balance(customer.credit.balance - amount)
        except ValueError as e:
            print(str(e))
    else:
        print("Invalid account type")

def select_customer():
    username = input("Enter the customer's username: ")
    for customer in customers:
        if customer.username == username:
            return customer
    print("Customer not found")
    return None

while True:
    print("Menu:")
    print("1. View customers")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Credit card charge")
    print("5. Credit card payment")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "2":
        view_customers()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        credit_card_charge()
    elif choice == "6":
        credit_card_payment()
    elif choice == "7":
        break
    else:
        print("Invalid choice")
        
