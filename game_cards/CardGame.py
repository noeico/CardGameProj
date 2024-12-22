
from game_cards.Player import Player
from DeckOfCards import DeckOfCards
class CardGame:

    def __init__(self, name_player1, name_player2, number_of_given_cards):
        self.player1 = Player(name_player1, number_of_given_cards)
        self.player2 = Player(name_player2, number_of_given_cards)
        self.number_of_given_cards = number_of_given_cards
        self.deck_of_cards = DeckOfCards()
        self.new_game()


    def new_game(self):
        """shuffeling the main cards and set cards to the players"""

        self.deck_of_cards.cards_shuffle()
        self.player1.set_hand(self.deck_of_cards)  
        self.player2.set_hand(self.deck_of_cards)

    def get_winner(self):
        """return the winner in the game"""
        if len(self.player1.cards_list) > len(self.player2.cards_list):
            return self.player1
        elif len(self.player1.cards_list) < len(self.player2.cards_list):
            return self.player2
        else:
            return None






