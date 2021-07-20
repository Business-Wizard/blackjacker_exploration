import random


class Deck:
    """A representation of a deck of cards"""

    def __init__(self):
        self.cards = 4 * [
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

    def shuffle(self):
        """Shuffles the order of cards in the deck"""
        random.shuffle(self.cards)
        return self.cards

    def draw_from_top(self):
        return self.cards.pop(-1)

    def reset_deck(self):
        self.cards = 4 * [
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
