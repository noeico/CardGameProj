
from game_cards.DeckOfCards import DeckOfCards
import random

class Player:
    def __init__(self, name, number_of_cards = None):
        """init the Player object, number of cards can be None"""
        if type(name) != str:
            raise TypeError("name must be a String !!")
        if number_of_cards is None:
            self.number_of_cards = 26
        else:
            if type(number_of_cards) != int:
                raise TypeError("number_of_cards must be an integer !!")
            if number_of_cards > 26 or number_of_cards < 10:
                self.number_of_cards = 26
            else:
                self.number_of_cards = number_of_cards
        self.name = name
        self.cards_list = []

    def set_hand(self,deck_of_cards: DeckOfCards):
        """inserting cards to the cards list of the player, according to number of cards"""
        for x in range (self.number_of_cards):
            self.cards_list.append(deck_of_cards.deal_one())

    def get_card(self):
        """choosing a random card from the player card list and removing it from the list"""
        if not self.cards_list:# if the player has no cards at all - it returns None
            return None
        else:
            selected_card = random.choice(self.cards_list)
            self.cards_list.remove(selected_card)
            return selected_card

    def add_card(self, added_card):
        """adding card to the card list"""
        self.cards_list.append(added_card)

    def __str__(self):
        return self.name





