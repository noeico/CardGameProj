from unittest import TestCase, mock
from game_cards.Player import Player
from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from unittest.mock import patch

class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player('Noei', 20)
        self.deck_of_cards = DeckOfCards()

    def test_init_valid(self):
        """test a simple valid arguments for __init__"""
        self.assertEqual('Noei', self.player.name)
        self.assertEqual(20,self.player.number_of_cards)

    def test_init_valid_empty_num_of_cards(self):
        player1 = Player('Noei')
        self.assertEqual('Noei', self.player.name)

    def test_lowest_number_of_cards(self):
        """test what happens when the init gets minimum cards"""
        player = Player('Noei', 10)
        self.assertEqual('Noei', player.name)
        self.assertEqual(10, player.number_of_cards)

    def test_highest_number_of_cards(self):
        """test what happens when the init gets maximum card"""
        player = Player('Noei', 26)
        self.assertEqual('Noei', player.name)
        self.assertEqual(26, player.number_of_cards)

    def test_init_higher_number_of_cards(self):
        """test that if number of cards is higher than 26, it still init with 26 cards"""
        player = Player('Noei', 27)
        self.assertEqual('Noei', player.name)
        self.assertEqual(26, player .number_of_cards)

    def test_init_lower_number_of_cards(self):
        """test that if number of cards is lower than 10, it still init with 26 cards"""
        player = Player('Noei', 9)
        self.assertEqual('Noei', player.name)
        self.assertEqual(26, player .number_of_cards)

    def test_init_lnvalid_type_name(self):
        """test when the name is different than string"""
        with self.assertRaises(TypeError):
            player = Player(43, 25)
            self.assertEqual("aaa", player.name)
            self.assertEqual(43, 25)

    #test that all the cards are filling according to number of times they needed and the right card from deal one method
    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(10, 3))
    def test_set_hand(self,mock_deal_one):
        self.player.set_hand(self.deck_of_cards)
        mock_cards_list=[]
        for x in range(20):
            mock_cards_list.append(Card(10,3))
        self.assertEqual(mock_cards_list,self.player.cards_list) #comppares the two lists

    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(10, 3))
    def test_Set_hand_minimum_cards(self,mock_deal_one):
        player1 = Player('Noei', 10)
        player1.set_hand(self.deck_of_cards)
        mock_cards_list = []
        for x in range(10):
            mock_cards_list.append(Card(10,3))
        self.assertEqual(mock_cards_list, player1.cards_list)

    #tests max cards for set_hand
    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(10, 3))
    def test_Set_hand_maximum_cards(self, mock_deal_one):
        player1 = Player('Noei', 26)
        player1.set_hand(self.deck_of_cards)
        mock_cards_list = []
        for x in range(26):
            mock_cards_list.append(Card(10, 3))
        self.assertEqual(mock_cards_list, player1.cards_list)

    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(10, 3))
    def test_Set_hand_invalid_over_max_cards(self, mock_deal_one):
        player1 = Player('Noei', 27)
        player1.set_hand(self.deck_of_cards)
        mock_cards_list = []
        for x in range(27):
            mock_cards_list.append(Card(10, 3))
        self.assertNotEqual(mock_cards_list, player1.cards_list)


    @mock.patch('game_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(10, 3))
    def test_Set_hand_invalid_below_min_cards(self, mock_deal_one):
        player1 = Player('Noei', 9)
        player1.set_hand(self.deck_of_cards)
        mock_cards_list = []
        for x in range(9):
            mock_cards_list.append(Card(10, 3))
        self.assertNotEqual(mock_cards_list, player1.cards_list)

    def test_get_card_removes_from_card_list(self):
        """tests that get_card actually removes the card from the player card list"""
        self.player.set_hand(self.deck_of_cards)
        taken_card = self.player.get_card()
        self.assertNotIn(taken_card,self.player.cards_list)

    def test_get_card_empty_deck_of_cards(self):
        """test what happens if the player has no cards at all"""
        player1 = Player("Noei")
        player1.cards_list = []
        player1.get_card()

    def test_add_card(self):
        card1 = Card(12,2)
        self.player.add_card(card1)
        self.assertIn(card1, self.player.cards_list)
















