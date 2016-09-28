from Card import Card, Deck
from Player import Player, Dealer


class Game():
    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck

    def play(self):
        # print("Credits: {}".format(self.player.credits))
        print(self.dealer)
        print(self.dealer.get_result())
        print(self.player)
        print(self.player.get_result())
        while self.player.credits > 0:
            while True:
                if self.player.get_result() == 21 and len(self.player.hand) == 2:
                    print("BlackJack!")
                    print("\n")
                    self.player.credits += 15
                    return
                elif self.player.get_result() > 21:
                    print("Busted")
                    print("\n")
                    self.player.credits -= 10
                    return
                elif self.dealer.get_result() > 21:
                    print("You win!")
                    print("\n")
                    self.player.credits += 10
                    return
                elif self.dealer.get_result() == 21:
                    self.dealer.stand()
                else:
                    if self.player.turn:
                        command = input("Enter command :>")
                        if command == 'h':
                            self.player.hit(self.deck)
                            print(self.dealer)
                            print(self.dealer.get_result())
                            print(self.player)
                            print(self.player.get_result())
                        elif command == 's':
                            self.player.stand()
                            # print(self.dealer)
                            # print(self.dealer.get_result())
                            # print(self.player)
                            # print(self.player.get_result())
                        elif command == 'd':
                            self.player.hit(self.deck)
                            self.player.turn = False
                            print(self.player)
                            print(self.player.get_result())
                            print("\n")
                    elif self.dealer.turn:
                        while self.dealer.get_result() < 17:
                            self.dealer.hit(self.deck)
                        if self.dealer.get_result() > 21:
                            print(self.dealer)
                            print(self.dealer.get_result())
                            print("Dealer Busted!")
                            print("\n")
                            self.player.credits += 10
                            return
                        else:
                            self.dealer.stand()
                            break

            if self.player.get_result() > self.dealer.get_result():
                print(self.dealer)
                print(self.dealer.get_result())
                print(self.player)
                print(self.player.get_result())
                print("You win!")
                print("\n")
                self.player.credits += 10
                return
            elif self.player.get_result() == self.dealer.get_result():
                print(self.dealer)
                print(self.dealer.get_result())
                print(self.player)
                print(self.player.get_result())
                print("Push!")
                print("\n")
                return
            else:
                print(self.dealer)
                print(self.dealer.get_result())
                print(self.player)
                print(self.player.get_result())
                print("Dealer wins!")
                print("\n")
                self.player.credits -= 10
                return

    def first_cards(self):
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)


def main():
    player = Player("Player")
    dealer = Dealer("Dealer")
    deck = Deck()
    game = Game(player, dealer, deck)
    game.first_cards()
    game.play()


if __name__ == '__main__':
    while True:
        main()
