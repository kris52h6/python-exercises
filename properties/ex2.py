class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, *args):
        for i in args:
            self.accounts.append(i)


class Account:

    def __init__(self, *args):
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.balance = args[1]

    def __str__(self):
        return f'Account id: {self.id}, Account balance: {self.balance}' if hasattr(self, 'balance') else f'Account id: {self.id}, Account balance: 0'


class Customer:

    def __init__(self, *args):
        self.account = None
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}' if hasattr(self, 'age') else f'Name: {self.name}'

    def add_account(self, account):
        self.account = account

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 18:
            self._age = value
        else:
            print('too young')


def main():
    b = Bank()
    a = Account(1)
    a2 = Account(5)
    c = Customer('Kristian')
    c2 = Customer('Anna', 20)
    print(c.account)

    c.add_account(a)
    c2.age = 10
    print(c2.age)

    print(c.account)

    b.add_account(a)
    b.add_account(a2)

    print(c)
    print(c2)

    for i in b.accounts:
        print(i)


main()
