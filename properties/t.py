class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, x):
        if type(x) != str:
            print('Not a string')
        else:
            self._name = x


p = Person('Test')
