class Deck:

    def __init__(self):
        self.cards = ['A', 'K', 'S', 2, 9]

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'The current deck of cards is: {self.cards}'

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        d = Deck()
        d.cards = self.cards + other.cards
        return d

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]


def Main():
    d = Deck()
    print(repr(d))
    print(d)
    print(len(d))
    print(d + d)
    print(d.cards[0])
    d.cards[0] = 5
    print(d)

    del d.cards[0]

    print(d)


Main()
