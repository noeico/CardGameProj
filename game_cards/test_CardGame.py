from unittest import TestCase
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from game_cards.CardGame import CardGame

class TestCardGame(TestCase):

    def setUp(self):
        self.card_game = CardGame("Noei", "Shani", 26)

    def test_valid_init_valid(self):
        """test a simple valid arguments for __init__"""
        self.assertEqual('Noei', self.card_game.player1.name)





    




