from collections import Counter

import pytest

from src.Deck import Deck


@pytest.fixture
def Deck_52():
    return Deck()


@pytest.fixture
def Deck_52_Counter():
    return Counter(
        4
        * ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    )


@pytest.fixture
def Deck_52_List():
    return 4 * [
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


def test_deck_has_standard_cards(Deck_52, Deck_52_Counter):
    deck_cards_set = Counter(Deck_52.cards)
    expected = Deck_52_Counter
    assert deck_cards_set == expected, "Deck does not have the correct cards"


def test_shuffled_same_length(Deck_52):
    original = Deck_52.cards.copy()
    shuffled = Deck_52.shuffle()
    assert original != shuffled, "Deck.shuffle did not change the card order"
    assert Counter(original) == Counter(
        shuffled
    ), "Deck.shuffle has added/removed cards"


def test_draw_from_top(Deck_52):
    top_card = Deck_52.cards[-1]
    drawn_card = Deck_52.draw_from_top()
    assert top_card == drawn_card


def test_reset_deck(Deck_52, Deck_52_List):
    Deck_52.reset_deck()
    assert Deck_52.cards == Deck_52_List
