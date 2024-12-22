from game_cards.DeckOfCards import DeckOfCards
from game_cards.Card import Card
from game_cards.CardGame import CardGame
from game_cards.Player import Player

player1_name = str(input("please insert a name for player 1: "))
player2_name = str(input("please insert a name for player 2: "))
card_game = CardGame(player1_name, player2_name, 26)
print("")
print(f"The cards of {player1_name} are: ")
print(card_game.player1.cards_list)
print("")
print(f"The cards of {player2_name} are: ")
print(card_game.player2.cards_list)
print("")

for round in range(10):
    player1_card = card_game.player1.get_card()
    player2_card = card_game.player2.get_card()
    print("")
    print(f"{player1_name} card is: {player1_card}")
    print(f"{player2_name} card is: {player2_card}")
    if player1_card > player2_card:
        card_game.player1.add_card(player1_card)
        card_game.player1.add_card(player2_card)
        print(f"the winner of this round is {player1_name}")
        print(f"the winner card is: {player1_card}")
        print("")
        print(f"{player1_name} has {len(card_game.player1.cards_list)} cards left")
        print(f"{player2_name} has {len(card_game.player2.cards_list)} cards left")
       # print(f"{player1_name} has :{len(card_game.player1.cards_list)}")
       # print(f"{player2_name} has :{len(card_game.player2.cards_list)}")
    else:
        card_game.player2.add_card(player1_card)
        card_game.player2.add_card(player2_card)
        print(f"the winner of this round is {player2_name}")
        print(f"the winner card is: {player2_card}")
        print("")
        print(f"{player1_name} has {len(card_game.player1.cards_list)} cards left")
        print(f"{player2_name} has {len(card_game.player2.cards_list)} cards left")
        print("")

if card_game.get_winner() == None:
    print("Its a tie")
else:
    print(f"the winner is: {card_game.get_winner()} " )









