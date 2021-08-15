import random
from itertools import product
from typing import List

from src.card import Card


class Deck:
    """A representation of a deck of cards"""

    def __init__(self):
        self.cards = []
        self.reset_cards()

    def reset_cards(self):
        ranks: List[str] = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]

        suits: List[str] = ["Spades", "Hearts", "Diamonds", "Clubs"]

        product_list = product(suits, ranks)
        self.cards = [Card(rank, suit) for suit, rank in product_list]

    def shuffle(self):
        """Shuffles the order of cards in the deck"""
        random.shuffle(self.cards)
        return self.cards

    def draw(self, num: int = 1) -> List[Card]:
        assert num > 0, "must draw at least one card"
        if num == 1:
            return [self.cards.pop(0)]
        else:
            return [self.cards.pop(0) for __ in range(num)]
