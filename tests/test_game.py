import pytest

from src.card import Card
from src.deck import Deck
from src.game import Game


@pytest.fixture
def game() -> Game:
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


def test_game_starts_with_no_rounds_played(game):
    game.start_game()
    assert game.rounds_played == 0, "game started with rounds_played != 0"


def test_game_plays_multiple_rounds(game):
    game.start_game()
    game.play_round(5)
    assert game.rounds_played == 5, f"rounds_played is inaccurate: {game.rounds_played}"


def test_game_reshuffles_when_low(game):
    game.start_game()
    game.deck.draw(50)
    game.play_round()
    assert len(game.deck.cards) > 40
