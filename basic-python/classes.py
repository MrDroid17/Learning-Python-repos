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

# using class
sobhit = Person('Sobhit Kumar', 'random@email.com')
print('Name:', sobhit.get_name())
print('Email:', sobhit.get_email())
