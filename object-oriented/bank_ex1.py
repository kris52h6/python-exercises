class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)


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
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}' if hasattr(self, 'age') else f'Name: {self.name}'


def main():
    b = Bank()
    a = Account(1)
    a2 = Account(5)
    c = Customer('Kristian')
    c2 = Customer('Anna', 20)

    b.add_account(a)
    b.add_account(a2)

    print(c)
    print(c2)

    for i in b.accounts:
        print(i)


main()
