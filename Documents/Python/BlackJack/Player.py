from Card import Card, Deck


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.turn = True
        self.credits = 100

    def __str__(self):
        cards = []
        for card in self.hand:
            cards.append(str(card))
        return str(cards)

    def hit(self, deck):
        card = deck[0]
        self.hand.append(card)
        deck.remove_card(card)

    def stand(self):
        self.turn = False

    def get_result(self):
        result = 0
        result_with_A = 0
        for card in self.hand:
            if card.value == 'A':
                result += card.card_value()
                result_with_A += 1
            else:
                result_with_A += card.card_value()
                result += card.card_value()
        if result_with_A != 0:
            if result > 21:
                result = result_with_A
                return result
            else:
                return result
        else:
            return result


class Dealer(Player):
    def dealers_turn(self, deck):
        if self.turn:
            while self.get_result() < 17:
                self.hit(deck)
            else:
                self.stand()
