class Account:
    """
    houses all attributes to be housed by checking, savings, and credit classes
    attributes: account_id (4-digit string of numbers), balance (float), interest (int)
    """
    def __init__(self, account_id='', balance=0):
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

        for num in account_id:
            if type(num) != int:
                raise TypeError('account ID must be a string of 4 numbers')

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
        raise TypeError('interest cannot be modified')

    def del_interest(self):
        raise TypeError('cannot delete interest')

    interest = property(get_interest, set_interest, del_interest)

    def __str__(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance}, Interest: {self.interest}"


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
    def __init__(self, account_id='', balance=0, interest=30, credit_limit=0):
        self.account_id = account_id
        self.balance = balance
        self.interest = interest
        self.credit_limit = credit_limit

    # balance property for credit
    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if not isinstance(balance, (float, int)):
            raise TypeError('balance must be float or integer')

        if balance < 0:
            raise ValueError('balance cannot be negative')

        if balance > self.credit_limit:
            raise ValueError('balance exceeds credit limit')

        else:
            self._balance = balance

    def del_balance(self):
        self._balance = 0

    balance = property(get_balance, set_balance, del_balance)

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
        return f"Account ID: {self.account_id}, Balance: {self.balance}, Interest: {self.interest}, " \
               f"Credit Limit: {self.credit_limit}"


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
        return self.username

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
        return f"Username: {self.username}, Checking: {self.checking}, Savings: {self.saving}" \
               f"Credit: {self.credit}"
