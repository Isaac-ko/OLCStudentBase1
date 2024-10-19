'''
Create the game of Black Jack
'''
import random
import time

wallet = 100

suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']

# Step 1: Create the deck of cards
# Create a dictionary to store the value of each card rank
# Cards 2–10 are worth their face value, J, Q, K are worth 10, 
# and Ace can be 1 or 11
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'JACK':10, 'QUEEN':10,'KING':10, 'ACE':11}

# Combine ranks and suits to build a deck of cards
deck = [] # this will contain all your cards
for s in suits:
    for r in ranks: 
        deck.append([r, s])
# print(deck)

# Shuffle the deck
for i in range(10):
    random.shuffle(deck)
# print(deck)

# Initialize hands for the player and the banker
player_hand = [deck.pop(), deck.pop()]
banker_hand = [deck.pop(), deck.pop()]

# print(player_hand)
# print(banker_hand)

def calculate_hand(hand):
    ace_count = 0

    points = 0
    # loop through every card
    for c in hand:
        if c[0] == "ACE":
            ace_count +=1
        #print(c[0])
        card_point = values[c[0]]
        points = points + card_point
    
    #print(points)

    # handle the aces if points > 21
    while points > 21 and ace_count > 0:
        points = points - 10 # treat my ace as 1, not 11
        ace_count = ace_count - 1

    return points

# print(calculate_hand(player_hand))
# print(calculate_hand(banker_hand))

# to show the display of the card 
def display_hand(hand, turn):
    if turn.lower() == "player":
        print("\n")
        print("&"*30)
        print("{:^30}".format("Player Hand"))
        print("{:^30}".format("-----------"))

        for c in hand:
            card_value = "{} {}".format(c[0], c[1])
            print("{:^30}".format(card_value))
        
        score_msg = "You have {} points.".format(calculate_hand(hand))
        print("{:^30}".format(score_msg))

        print("&"*30)
        print("\n")
    elif turn.lower() == "banker_hide":
        print("\n")
        print("$"*30)
        print("{:^30}".format("Banker Hand"))
        print("{:^30}".format("-----------"))

        b_card = hand[0]
        b_card_value = "{} {}".format(b_card[0], b_card[1])
        print("{:^30}".format(b_card_value))
        print("{:^30}".format("? ? ? ? ?"))
        print("$"*30)
        print("\n")
    if turn.lower() == "banker_show":
        print("\n")
        print("$"*30)
        print("{:^30}".format("Banker Hand"))
        print("{:^30}".format("-----------"))

        for c in hand:
            card_value = "{} {}".format(c[0], c[1])
            print("{:^30}".format(card_value))
        
        score_msg = "Banker have {} points.".format(calculate_hand(hand))
        print("{:^30}".format(score_msg))

        print("$"*30)
        print("\n")
    # banker_hide
    # banker_show

while wallet > 0:
    game_start = input("Type p to play or q to quit: ").lower()

    if game_start == "p":
        bet = int(input("input amount: "))
        if bet >= wallet:
            break
        else:
            print("you do not have enough money in your wallet.")
            print("Wallet: ${}".format(wallet))

        while True:
            display_hand(banker_hand, "banker_show")
            display_hand(player_hand, "player")

            if calculate_hand(player_hand) == 21:
                print("you have 21! Black Jack!")
                break
            elif calculate_hand(player_hand) > 21:
                print("you have {} points".format(calculate_hand(player_hand)))
                print("You busted")
                break

            player_action = input("1 = hit, 2 = check")

            if player_action.isdigit():
                if player_action == "1":
                    player_hand.append(deck.pop())

                elif player_action == "2":

                    while calculate_hand(banker_hand) <= 17:
                        print("$$$ Banker is thinking...")
                        time.sleep(1)
                        print("$$$ Banker draws a card...")
                        banker_hand.append(deck.pop())

                    if calculate_hand(banker_hand) > 21:
                        display_hand(banker_hand, "banker_show")
                        display_hand(player_hand, "player")
                        print("Banker busted")
                        print("you win")
                        break
                    else:
                        player_score = calculate_hand(player_hand)
                        banker_score = calculate_hand(banker_hand)
                        display_hand(banker_hand, "banker_show")
                        display_hand(player_hand, "player")

                        if player_score > banker_score:
                            print("You won the game!")
                        elif player_score < banker_score:
                            print("banker won the game!")
                        else:
                            print("You both have the same points. its a draw")
                        break
            else:
                  print("Invalid input.option 1 or 2 only")
        
    elif game_start == "q":
        print("BYe")
        break


# Function to calculate the value of a hand

# Function to display the hand of cards (with rank and suit)

# Game Loop, Player and Banker Turn

    # Show player's hand and banker's visible card

    # Check for Blackjack (21 points) in the player's hand

    # Ask player if they want to hit or stand

    #  Add a new card to the player's hand if they choose to hit

        # Check if the player busts (goes over 21)

    # End player's turn

    # Banker's turn (if player hasn't busted)
    # Banker hits until their total is 17 or more
    # Compare player and banker totals to determine the winner