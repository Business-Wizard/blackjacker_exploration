import random
from itertools import product
from typing import List

from src.Card import Card


class Deck:
    """A representation of a deck of cards"""

    def __init__(self):
        self.cards = self.reset_cards()

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
        return [Card(rank, suit) for suit, rank in product_list]

    def shuffle(self):
        """Shuffles the order of cards in the deck"""
        random.shuffle(self.cards)
        return self.cards

    def draw_from_top(self):
        return self.cards.pop(-1)
