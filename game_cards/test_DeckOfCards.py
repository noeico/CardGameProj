from unittest import TestCase, mock

from charset_normalizer.utils import range_scan

from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from unittest.mock import patch

class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck_of_cards = DeckOfCards()

    def test_52_cards(self):
        """test that it only intiate with 52 cards"""
        self.assertEqual(52, len(self.deck_of_cards.list_of_cards))

    def test_cards_shuffle(self):
        new_cards_list1 = self.deck_of_cards.list_of_cards
        new_cards_list2 = self.deck_of_cards.list_of_cards.copy() # without copy() - the two lists would be the same object on memory adress
        self.deck_of_cards.cards_shuffle()
        self.assertNotEqual(new_cards_list1, new_cards_list2)

    def test_deal_one(self):
        """checking that the card was removoed from the player's deck of cards"""
        taken_card = self.deck_of_cards.deal_one()
        self.assertNotIn(taken_card, self.deck_of_cards.list_of_cards)

    def test_deal_one_no_cards(self):
        """test when the deck is empty"""
        deck_of_cards = DeckOfCards()
        deck_of_cards.list_of_cards = []
        deck_of_cards.deal_one()












