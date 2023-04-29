class Account:
    """
    Abstract class representing an account object.

    Attributes:
        _id: four numerical digit string representing the Account id, cannot be empty
            (so no default provided)
    """

    # Account doesn't need an __init__ since we don't ever want to instantiate
    # an Account object (only the three subclasses will be instantiated, and
    # they each need their own __init__ anyway)

    def __str__(self):
        return self.id

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        if not isinstance(new_id, str):
            raise TypeError('id should be a string')
        elif len(new_id) != 4:
            raise ValueError('id should be four digits long')

        allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for digit in new_id:
            if digit not in allowed_chars:
                raise ValueError('id should consist only of numeric digits')

        self._id = new_id

    def del_id(self):
        del self._id
        del self

    id = property(get_id, set_id, del_id)

class Savings(Account):
    '''
    Savings class inherits Account
    '''

    def __init__(self, new_id):
        self.id = new_id

    # Overriding the __str__ class for purpose of demonstration
    # (the __str__ in Account is perfectly good to inherit)
    def __str__(self):
        return f'This is a Savings id: {self.id}'

    # property id is inherited from Account
    # If you wanted different behavior for the Savings class specifically,
    # you would override the method/property here.


# This will throw an error, since Account has
#acct = Account('1234')

# Notice __init__ is inherited
savings = Savings('1234')
print(savings)
print(type(savings))

try:
    savings.set_id('5678')
#    savings.set_id('abcd')
#    print("This won't execute.")
except:
    print('Bad ID given. Not updating ID.')

print(savings)