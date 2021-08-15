class Player:
    """
    Represents a player: money, hand cards, wager
    """

    def __init__(self, starting_money: int = 1000):
        self.money = starting_money
        self.wager = 0
        self.cards = []


class Dealer:
    def __init__(self, starting_money: int = 1000):
        self.money = starting_money
        self.wager = 0
        self.cards = []
