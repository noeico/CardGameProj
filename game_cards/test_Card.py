from unittest import TestCase
from game_cards.Card import Card
from unittest import TestCase, mock
from unittest.mock import patch

class TestCard(TestCase):

    def setUp(self):
        self.card = Card(10,2)

    def test_init_valid(self):
        """test a simple valid arguments for __init__"""
        self.assertEqual(10, self.card.type_of_card)
        self.assertEqual(2, self.card.suit)

    def test_init_valid_highest_type(self):
        """test when the value of the card is the highest it can be - 14 means Ace"""
        card = Card(14, 2)
        self.assertEqual(14, card.type_of_card)
        self.assertEqual(2, card.suit)

    def test_init_valid_highest_suit(self):
        """test when the suit of the card is the highest it can be - which is 4"""
        card = Card(8, 4)
        self.assertEqual(8, card.type_of_card)
        self.assertEqual(4, card.suit)

    def test_init_valid_lowest_suit(self):
        """test when the suit of the card is the lowest it can be - which is 1"""
        card = Card(8, 1)
        self.assertEqual(8, card.type_of_card)
        self.assertEqual(1, card.suit)

    def test_init_low_suit_number(self):
        """test when the suit of the card is below 1"""
        with self.assertRaises(ValueError):
            card = Card(8, 0)
            self.assertEqual(8, card.type_of_card)
            self.assertEqual(0, card.suit)

    def test_init_high_suit_number(self):
        """test when the suit of the card is higher than it can get - 4 is the max"""
        with self.assertRaises(ValueError):
            card = Card(8, 5)
            self.assertEqual(8, card.type_of_card)
            self.assertEqual(5, card.suit)

    def test_init_high_value_number(self):
        """test when the value of the card is higher than it can get - 14 is the max"""
        with self.assertRaises(ValueError):
            card = Card(15, 3)
            self.assertEqual(15, card.type_of_card)
            self.assertEqual(3, card.suit)

    def test_init_low_value_number(self):
        """test when the value of the card is not an integer"""
        with self.assertRaises(TypeError):
            card = Card("aaa", 3)
            self.assertEqual("aaa", card.type_of_card)
            self.assertEqual(3, card.suit)

    def test_init_low_value_number(self):
        """test when the value of the card is not an integer"""
        with self.assertRaises(TypeError):
            card = Card(12, "ccc")
            self.assertEqual(12, card.type_of_card)
            self.assertEqual("ccc", card.suit)

    def test_gt_value_suit_the_same(self):
        """test highest card by value - suit is the same"""
        card1 = Card(13,2)
        card2 = Card(12,2)
        self.assertGreater(card1,card2)

    def test_gt_value_suit_is_higher(self):
        """test highest wheen value is the same and suit is higher"""
        card1 = Card(12, 3)
        card2 = Card(12, 2)
        self.assertGreater(card1, card2)

    def test_gt_value_suit_is_lower(self):
        """test highest card when value is the same and suit is lower"""
        card1 = Card(12, 1)
        card2 = Card(12, 2)
        self.assertLess(card1, card2)

    def test_gt_value_suit_is_lower(self):
        """test highest card when value is the same and suit is lower"""
        card1 = Card(11, 3)
        card2 = Card(12, 2)
        self.assertLess(card1, card2)

    def test_eq_card_is_same(self):
        """test when value is different and higher"""
        card1 = Card(11, 3)
        card2 = Card(11, 3)
        self.assertEqual(card1,card2)


    def test_eq_suit_different(self):
        """test when value is the same and suit is different"""
        card1 = Card(12, 3)
        card2 = Card(12, 2)
        self.assertNotEqual(card1,card2)

    def test_eq_value_and_suit_is_different(self):
        """test when value is different and suit is different"""
        card1 = Card(10, 3)
        card2 = Card(12, 2)
        self.assertNotEqual(card1, card2)

    def test_eq_suit_different_value(self):
        """test when value is different and suit is the same"""
        card1 = Card(10, 3)
        card2 = Card(12, 3)
        self.assertNotEqual(card1, card2)