import numpy as np
from src.Deck import Deck
import pytest
from collections import Counter


@pytest.fixture
def Deck_52():
    return Deck()


def test_deck_has_standard_cards(Deck_52):
    deck_cards_set = Counter(Deck_52.cards)
    expected = Counter(4 * ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'])
    assert deck_cards_set == expected, deck_cards_set

def test_shuffled_same_length(Deck_52):
    original = Deck_52.cards.copy()
    Deck_52.shuffle()
    shuffled = Deck_52.cards
    assert original != shuffled

def test_shuffled_is_not_null(Deck_52):
    Deck_52.shuffle()
    assert Deck_52.cards != None


def test_draw_from_top(Deck_52):
    top_card = Deck_52.cards[-1]
    drawn_card = Deck_52.draw_from_top()
    assert  top_card == drawn_card


def test_reset_deck(Deck_52):
    Deck_52.reset_deck()
    assert Deck_52.cards == 4 * ['2', '3', '4', '5', '6', '7', '8', '9',
                                     '10', 'Jack', 'Queen', 'King', 'Ace']
