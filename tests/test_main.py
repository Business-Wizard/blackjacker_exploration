import numpy as np
import src.main as main



tester_deck = main.Deck()


def test_deck_has_standard_cards():
    assert tester_deck.cards == 4 * [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def test_shuffled_same_length():
    original = tester_deck.cards.copy()
    tester_deck.shuffle()
    shuffled = tester_deck.cards
    assert original != shuffled

def test_shuffled_is_not_null():
    tester_deck.shuffle()
    assert tester_deck.cards != None


def test_draw_from_top():
    assert tester_deck.cards[-1] == tester_deck.draw_from_top()

