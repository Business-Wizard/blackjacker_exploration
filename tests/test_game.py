from src.game import Game
import pytest
from src.deck import Deck
from src.card import Card


@pytest.fixture
def game():
    return Game()


def test_game_has_cards(game):
    assert len(game.deck.cards) > 0


def test_game_deck_shuffled(game):
    game.start_game()
    assert game.deck != Deck().cards


def test_dealer_has_two_cards(game):
    game.start_game()
    game.play_round()
    assert len(game.dealer.cards) == 2


def test_game_has_first_dealer_card(game):
    game.start_game()
    game.play_round()
    assert game.dealer_card is not None, "game is missing the dealer card"


def test_game_has_one_dealer_card(game):
    game.start_game()
    game.play_round()

    assert isinstance(game.dealer_card, Card)
