import random


class Game():
    """Represents the game structure: players + dealer
    """


class Deck():
    """A representation of a deck of cards
    """
    def __init__(self):
        self.cards = 4 * ['2', '3', '4', '5', '6', '7', '8', '9',
                          '10', 'Jack', 'Queen', 'King', 'Ace']

    def shuffle(self):
        """Shuffles the order of cards in the deck
        """
        random.shuffle(self.cards)

    def draw_from_top(self):
        return self.cards.pop(-1)

    
    def reset_deck(self):
        self.cards = 4 * ['2', '3', '4', '5', '6', '7', '8', '9',
                          '10', 'Jack', 'Queen', 'King', 'Ace']



class Player():
    """Represents a player: money, hand cards, wager
    """
    def __init__(self, starting_money):
        self.money = starting_money
        self.wager = 0









