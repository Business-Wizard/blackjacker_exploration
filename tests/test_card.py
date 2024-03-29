import pytest

from src.card import Card


@pytest.fixture
def Card_Ace_Spades():
    return Card("Ace", "Spades")


def test_card_print(Card_Ace_Spades):
    printed = Card_Ace_Spades.__repr__()
    expected = "Card(rank='Ace', suit='Spades')"
    assert printed == expected
