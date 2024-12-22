from random import random
import random
from game_cards.Card import Card

class DeckOfCards:
    def __init__(self):
        self.list_of_cards = []
        for card_value in range(2, 15):  # 14 is the highest which means "Ace"
            for suit in range(1, 5):
                self.list_of_cards.append(Card(card_value, suit))

    def __str__(self):
        return f"{self.list_of_cards}"

    def cards_shuffle(self):
        """shuffle the deck of the cards"""
        random.shuffle(self.list_of_cards)

    def deal_one(self):
        """take a random card from the deck of the cards"""
        if len(self.list_of_cards) == 0:
            return None
        chosen_card = random.choice(self.list_of_cards)
        self.list_of_cards.remove(chosen_card)
        return chosen_card

