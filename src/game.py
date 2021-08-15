from src.card import Card
from src.deck import Deck
from src.player import Dealer


class Game:
    """
    Represents the game structure: players & dealer
    """

    def __init__(self, dealer=Dealer(), *players):
        self.deck: Deck = Deck()
        self.dealer = dealer
        self.dealer_card: Card = None

    def start_game(self):
        self.deck.shuffle()

    def play_round(self):
        self.dealer.cards = self.deck.draw(2)
        print(self.dealer.cards, self.dealer.cards[0])
        self.dealer_card = self.dealer.cards[0]
