

class Card:
    def __init__(self,type_of_card, suit):
        if suit < 1 or suit > 4:
            raise ValueError("suit must be between 1 to 4 !!")
        if type_of_card < 2 or type_of_card > 14:
            raise ValueError("value must be between 2 to 14 !!")
        if type(suit) !=  int:
            raise TypeError("suit must be an integer")
        if type(type_of_card) !=  int:
            raise TypeError("type_of_card must be an integer")
        self.type_of_card = type_of_card
        self.suit = suit

    def __gt__(self, other):
        if self.type_of_card > other.type_of_card:
            return True
        elif self.type_of_card < other.type_of_card:
            return False
        elif self.suit > other.suit: #they are equal so it comes to here
            return True
        else:
            return False

    def __eq__(self, other):
        if self.type_of_card == other.type_of_card and self.suit == other.suit:
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.type_of_card},{self.suit}"

