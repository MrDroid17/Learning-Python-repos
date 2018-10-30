class Person():
    # __ shows that variable are private
    __name = ''
    __email = ''

    # constructor
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    # getter and setters for name
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    # getter and setters for email
    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    # formatted string
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)

# using class
sobhit = Person('Sobhit Kumar', 'random@email.com')
print('Name:', sobhit.get_name())
print('Email:', sobhit.get_email())
print(sobhit.toString())

# inheritance
class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def toString(self):
        return '{} has balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)

droid = Customer('Mrdroid17', 'mrdroid@github.com', 100)
print(droid.toString())

droid.set_balance(500)
print(droid.toString())