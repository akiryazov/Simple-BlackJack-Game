import random

CARDS = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6),
         ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]


class Player():

    def __init__(self):

        self.hand = []

    def stand(self):
        pass

    def get_hand_value(self):
        value = 0
        for card in self.hand:
            value += card[1]
        return(value)

    def __str__(self):
        return "{0} - {1}".format([card[0] for card in self.hand], self.get_hand_value())

    def hit(self):
        self.hand.append(random.choice(CARDS))
        return self.get_hand_value()
