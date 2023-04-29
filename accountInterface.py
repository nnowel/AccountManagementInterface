import csv


class Account:
    """
    houses all attributes to be housed by checking, savings, and credit classes
    attributes: account_id (4-digit string of numbers), balance (float), interest (int)
    """
    def __init__(self, account_id='', balance=0.0):
        self.account_id = account_id
        self.balance = balance

        if isinstance(self, Checking):
            self.interest = 0
        if isinstance(self, Saving):
            self.interest = 1

    # account_id property
    def get_account_id(self):
        return self._account_id

    def set_account_id(self, account_id):
        if not isinstance(account_id, str):
            raise TypeError('account ID must be string')

        allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for digit in account_id:
            if digit not in allowed_chars:
                raise ValueError('id should consist only of numeric digits')

        if len(account_id) != 4:
            raise ValueError('account ID must be 4 numbers long')

        else:
            self._account_id = account_id

    def del_account_id(self):
        del self._account_id

    account_id = property(get_account_id, set_account_id, del_account_id)

    # balance property
    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if not isinstance(balance, (float, int)):
            raise TypeError('balance must be float or integer')

        if balance < 0:
            raise ValueError('balance cannot be negative')

        else:
            self._balance = balance

    def del_balance(self):
        self._balance = 0

    balance = property(get_balance, set_balance, del_balance)

    # interest property
    def get_interest(self):
        return self._interest

    def set_interest(self, interest):
        self._interest = interest

    def del_interest(self):
        raise TypeError('cannot delete interest')

    interest = property(get_interest, set_interest, del_interest)

    def __str__(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance:.2f}, Interest: {self.interest}"

    def deposit(self):
        if isinstance(self, (Checking, Saving)):
            username = input('type in username')
            account = input('checking (c) or saving (s)?')
            amount = input('enter dollar amount')

            customer = lookup(username)
            if account == 'c':
                customer.checking.balance = customer.checking.balance + amount
            elif account == 's':
                customer.saving.balance = customer.saving.balance + amount
        else:
            print('cannot deposit into credit account')

    def withdraw(self):
        if isinstance(self, (Checking, Saving)):
            username = input('type in username')
            account = input('checking (c) or saving (s)?')
            amount = input('enter dollar amount')

            customer = lookup(username)
            if account == 'c':
                try:
                    customer.checking.balance = customer.checking.balance - amount
                except ValueError:
                    print('withdraw amount greater than balance')
            elif account == 's':
                try:
                    customer.saving.balance = customer.saving.balance - amount
                except ValueError:
                    print('withdraw amount greater than balance')
        else:
            print('cannot withdraw from credit account')


class Checking(Account):
    """
    represents the checking account
    attributes: same as account
    """


class Saving(Account):
    """
    represents the savings account
    attributes: same as account
    """


class Credit(Account):
    """
    represents the credit account
    attributes: same as account plus credit_limit (float)
    """
    def __init__(self, account_id='', balance=0.0, credit_limit=0):
        self.balance = balance
        self.credit_limit = credit_limit
        self.account_id = account_id
        self.interest = 30

    # balance property for credit
    # def get_balance(self):
        # return self._balance

    # def set_balance(self, balance):
        # if not isinstance(balance, (float, int)):
            # raise TypeError('balance must be float or integer')

        # if balance < 0:
            # raise ValueError('balance cannot be negative')

        # if balance > self.credit_limit:
            # raise ValueError('balance exceeds credit limit')

        # else:
            # self._balance = balance

    # def del_balance(self):
        # self._balance = 0

    # balance = property(get_balance, set_balance, del_balance)

    # credit_limit property
    def get_credit_limit(self):
        return self._credit_limit

    def set_credit_limit(self, credit_limit):
        if not isinstance(credit_limit, (int, float)):
            raise TypeError('credit limit must be integer or float')

        if credit_limit < 0:
            raise ValueError('credit limit cannot be negative')

        if credit_limit < self.balance:
            raise ValueError('credit limit must be greater than current balance')

        else:
            self._credit_limit = credit_limit

    def del_credit_limit(self):
        del self._credit_limit

    credit_limit = property(get_credit_limit, set_credit_limit, del_credit_limit)

    def __str__(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance:.2f}, Interest: {self.interest}, " \
               f"Credit Limit: {self.credit_limit:.2f}"

    def charge(self):
        username = input('type in username')
        amount = input('enter dollar amount')

        customer = lookup(username)
        try:
            customer.credit.balance = customer.credit.balance + amount
        except ValueError:
            print('charge exceeds credit limit')

    def payment(self):
        username = input('type in username')
        account = input('checking (c) or saving (s)?')
        amount = input('enter dollar amount')

        customer = lookup(username)
        if account == 'c':
            try:
                customer.checking.balance = customer.checking.balance - amount
            except ValueError:
                print('insufficient funds in checking account')
            try:
                customer.credit.balance = customer.credit.balance - amount
            except ValueError:
                print('payment amount exceeds current balance')
        elif account == 's':
            try:
                customer.saving.balance = customer.saving.balance - amount
            except ValueError:
                print('insufficient funds in saving account')
            try:
                customer.credit.balance = customer.credit.balance - amount
            except ValueError:
                print('payment amount exceeds current balance')


class Customer:
    """
    represents a customer's 3 bank accounts
    attributes: username (string), checking (Checking object), saving (Saving object), credit (Credit object)
    """
    def __init__(self, username='', checking=Checking, saving=Saving, credit=Credit):
        self.username = username
        self.checking = checking
        self.saving = saving
        self.credit = credit

    # username property
    def get_username(self):
        return self._username

    def set_username(self, username):
        if not isinstance(username, str):
            raise TypeError('username must be a string')

        else:
            self._username = username

    def del_username(self):
        del self._username

    username = property(get_username, set_username, del_username)

    # checking property
    def get_checking(self):
        return self._checking

    def set_checking(self, checking):
        if not isinstance(checking, Checking):
            raise TypeError('checking account must be a Checking object')

        else:
            self._checking = checking

    def del_checking(self):
        del self._checking

    checking = property(get_checking, set_checking, del_checking)

    # saving property
    def get_saving(self):
        return self._saving

    def set_saving(self, saving):
        if not isinstance(saving, Saving):
            raise TypeError('savings account must be a Saving object')

        else:
            self._saving = saving

    def del_saving(self):
        del self._saving

    saving = property(get_saving, set_saving, del_saving)

    # credit property
    def get_credit(self):
        return self._credit

    def set_credit(self, credit):
        if not isinstance(credit, Credit):
            raise TypeError('credit account must be a Credit object')

        else:
            self._credit = credit

    def del_credit(self):
        del self._credit

    credit = property(get_credit, set_credit, del_credit)

    def __str__(self):
        return f"Username - {self.username}, Checking - {self.checking}, Savings - {self.saving}, " \
               f"Credit - {self.credit}"


customerList = []


def importFromCSV(csvFile):
    with open(csvFile, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            checking_obj = Checking(str(row[1]), float(row[2]))
            saving_obj = Saving(str(row[3]), float(row[4]))
            credit_obj = Credit(str(row[5]), float(row[6]), float(row[7]))
            customer_obj = Customer(str(row[0]), checking_obj, saving_obj, credit_obj)
            customerList.append(customer_obj)


def lookup(username):
    location = 0
    for obj in customerList:
        if username == obj.username:
            break
        location += 1
    print(location)
    return customerList[location]


def viewCustomers(customerList):
    for obj in customerList:
        print(obj)


def deposit():
    username = input('type in username: ')
    account = input('checking (c) or saving (s)? ')
    amount = input('enter dollar amount: ')

    customer = lookup(username)
    if account == 'c':
        customer.checking.balance = customer.checking.balance + float(amount)
    elif account == 's':
        customer.saving.balance = customer.saving.balance + float(amount)


def withdraw():
    username = input('type in username: ')
    account = input('checking (c) or saving (s)? ')
    amount = input('enter dollar amount: ')

    customer = lookup(username)
    if account == 'c':
        try:
            customer.checking.balance = customer.checking.balance - float(amount)
        except ValueError:
            print('TRANSACTION CANCELLED: withdraw amount greater than balance')
    elif account == 's':
        try:
            customer.saving.balance = customer.saving.balance - float(amount)
        except ValueError:
            print('TRANSACTION CANCELLED: withdraw amount greater than balance')


def credit_charge():
    username = input('type in username: ')
    amount = input('enter dollar amount: ')

    customer = lookup(username)
    try:
        customer.credit.balance = customer.credit.balance + float(amount)
    except ValueError:
        print('TRANSACTION CANCELLED: charge exceeds credit limit')


def credit_payment():
    username = input('type in username: ')
    account = input('checking (c) or saving (s)? ')
    amount = input('enter dollar amount: ')

    customer = lookup(username)
    if account == 'c':
        try:
            customer.checking.balance = customer.checking.balance - float(amount)
        except ValueError:
            print('TRANSACTION CANCELLED: insufficient funds in checking account')
        try:
            customer.credit.balance = customer.credit.balance - float(amount)
        except ValueError:
            print('TRANSACTION CANCELLED: payment amount exceeds current balance')
    elif account == 's':
        try:
            customer.saving.balance = customer.saving.balance - float(amount)
        except ValueError:
            print('TRANSACTION CANCELLED: insufficient funds in saving account')
        try:
            customer.credit.balance = customer.credit.balance - float(amount)
        except ValueError:
            print('TRANSACTION CANCELLED: payment amount exceeds current balance')


def exitInterface():
    with open('/Users/nathanielnowel/PycharmProjects/AccountManagementInterface/newAccounts.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['username,checking_id,checking_balance,savings_id,savings_balance,credit_id,credit_balance,credit_limit'])
        writer.writerow(
            [f"{customerList[0].username},{customerList[0].checking.account_id},{customerList[0].checking.balance},"
             f"{customerList[0].saving.account_id},{customerList[0].saving.balance},{customerList[0].credit.account_id},"
             f"{customerList[0].credit.balance},{customerList[0].credit.credit_limit}"])
        writer.writerow(
            [f"{customerList[1].username},{customerList[1].checking.account_id},{customerList[1].checking.balance},"
             f"{customerList[1].saving.account_id},{customerList[1].saving.balance},{customerList[1].credit.account_id},"
             f"{customerList[1].credit.balance},{customerList[1].credit.credit_limit}"])
        writer.writerow(
            [f"{customerList[2].username},{customerList[2].checking.account_id},{customerList[2].checking.balance},"
             f"{customerList[2].saving.account_id},{customerList[2].saving.balance},{customerList[2].credit.account_id},"
             f"{customerList[2].credit.balance},{customerList[2].credit.credit_limit}"])


def interface():
    choice = ''
    while True:
        print('1: import customer account data from CSV')
        print('2: view customer account information')
        print('3: Deposit money')
        print('4: withdraw money')
        print('5: purchase with credit card')
        print('6: make credit card payment')
        print('7: exit and export account data to CSV')
        print('0: quit')

        choice = input('select an option: ')

        if choice == '1':
            importFromCSV('/Users/nathanielnowel/PycharmProjects/AccountManagementInterface/accounts.csv')
        elif choice == '2':
            viewCustomers(customerList)
        elif choice == '3':
            deposit()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            credit_charge()
        elif choice == '6':
            credit_payment()
        elif choice == '7':
            exitInterface()
            break
        elif choice == '0':
            break


# importFromCSV('accounts.csv')
# viewCustomers(customerList)
# exitInterface()
interface()
# withdraw()
# print(customerList)

