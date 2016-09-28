import random
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Spades', 'Clubs', 'Hearts', 'Diamonds']


class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)

    def card_value(self):
        if self.value == 'J' or self.value == 'Q' or self.value == 'K':
            return 10

        elif self.value == 'A':
            return 11

        else:
            return int(self.value)


class Deck():
    def __init__(self):
        self.deck = []
        for value in VALUES:
            for suit in SUITS:
                self.deck.append(Card(value, suit))
        random.shuffle(self.deck)

    def __str__(self):
        cards = []
        for card in self.deck:
            cards.append(str(card))
        return str(cards)

    def __getitem__(self, index):
        return self.deck[index]

    def remove_card(self, card):
        self.deck.remove(card)

    def shuffle(self):
        random.shuffle(self.deck)
