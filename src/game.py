from src.card import Card
from src.deck import Deck
from src.player import Dealer


class Game:
    """
    Represents the game structure: players & dealer
    """

    def __init__(self, dealer=Dealer(), *players):
        self.deck: Deck = Deck()
        self.dealer: Dealer = dealer
        self.dealer_card: Card = None
        self.rounds_played: int = 0
        self.players = [*players]

    def start_game(self):
        self.deck.shuffle()

    def play_round(self, num_rounds: int = 1):
        for __ in range(num_rounds):
            self._play_single_round()

    def _play_single_round(self):
        if len(self.deck.cards) < 15:
            self.deck.reset_cards()
        self.dealer.cards = self.deck.draw(2)
        self.dealer_card = self.dealer.cards[0]
        self.rounds_played += 1
