import os
import random

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_name = input("Enter you name: ")

# Create Clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Create function to show  hand
def show_card(player):
     print("-----------------------------------------------------------")
     print(f"{player["name"]} got: {player["cards"]} and the sum of his cards is: {sum(player["cards"])}")
     print("-----------------------------------------------------------")
# Create function to determine Ace value
def ace_value(cards):
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

# Create function to give card to player
def get_card(player):
    player["cards"].append(random.choice(cards_deck))

# Create function to calculate player score
def score(player):
    return sum(player["cards"])

# Create function to check for wining
def game_over(player1_score, dealer_score):

    if player1_score > 21:
        print(f"{player_name} you go over 21, you lose 😥 ")
    elif dealer_score > 21:
        print("The Dealer go over 21, You win 😊")
    elif dealer_score == 21:
        print("Dealer got 21, You lose 😔")
    elif player1_score > dealer_score:
        print(f"{player_name} Win 😁")
    else:
        print("You lose 😭")

def game_logic():
    input("To start press enter...")
    player1 = {"name": player_name, "cards": []}
    dealer = {"name": "Dealer", "cards": []}
    for _ in range(2):
        get_card(player1)
        get_card(dealer)

    show_card(player1)
    print(f"The Dealer got [{dealer["cards"][0]}, *]")
    print("-----------------------------------------------------------")

    another_card = True
    while another_card:
        if len(player1["cards"]) == 2 and score(player1) == 21:
            print(f"Blackjack, {player1["name"]} wins 😎")
            break
        else:
            if input("Do you want another card? (Y/N) ").lower() == "y":
                get_card(player1)
                #
                if score(player1) > 21 and 11 in player1["cards"]:
                    ace_value(player1["cards"])
                    if score(player1) > 21:
                        print(f"{player1["name"]} you go over 21, you lose 😥 ")
                        another_card = False
                    else:
                        pass
                elif score(player1) > 21:
                    print(f"{player1["name"]} you go over 21, you lose 😥 ")
                    another_card = False
                else:
                    show_card(player1)
            else:
                another_card = False

            while score(dealer) < 17:
                get_card(dealer)

    show_card(player1)
    show_card(dealer)
    game_over(score(player1), score(dealer))

    if input("Do you want to play again? (Y/N) ").lower() == "y":
        game_logic()
    else:
        print("Bye Bye!")

game_logic()

