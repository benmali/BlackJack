import random
from random import  randint
import itertools


class CardPlayer:

    def __init__(self, name, hand, second_hand, money, bet, second_bet,):
        self.name = name
        self.hand = hand
        self.money = money
        self.bet = bet
        self.second_bet = second_bet
        self.second_hand = second_hand
        self.second_hand_value = 0
        self.hand_value = 0
        self.hit_counter = 0
        self.hit_counter2 = 0
        self.ace_counter = 0
        self.ace_counter2 = 0



    def __repr__(self):
        return "CardPlayer('{}','{}')".format(self.name, self.hand)



    def get_player_list(self):
        players_list = raw_input("Enter player names")
        players_list = list(players_list.split(" "))
        print (players_list)
        return players_list

    def get_split(self):
        if self.second_hand_value> 21:
            print ("You are burned baby!")
            return self.second_hand, self.second_hand_value
            print ("GOT 21")
            return self.second_hand, self.second_hand_value
        else:
            deck = {"Hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                    "Diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                    "Clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                    "Picks": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
                    }

            drawn_card = list(random.choice(deck.items()))
            drawn_card = [drawn_card[0], random.choice(drawn_card[1])]
            deck.pop(drawn_card[0], drawn_card[1])  # Erasing the drawn card from the dictionary
            self.second_hand.append(drawn_card)

            self.hit_counter2 += 1 #calculates how many times have the player hit to get the cards value
            if self.second_hand[self.hit_counter2 - 1][1] == "Jack":
                self.second_hand_value += 10
            elif self.second_hand[self.hit_counter2 - 1][1] == "Queen":
                self.second_hand_value += 10
            elif self.second_hand[self.hit_counter2 - 1][1] == "King":
                self.second_hand_value += 10
            elif self.second_hand[self.hit_counter2 - 1][1] == "Ace":
                self.second_hand_value += 11
                self.ace_counter2 += 1
            else:
                self.second_hand_value += self.second_hand[self.hit_counter2 - 1][1]

            if ("Ace" in self.second_hand) and (self.second_hand_value > 21) and (self.ace_counter2 > 0):
                self.ace_counter2 -= 1
                self.second_hand_value -= 10

            return self.second_hand, self.second_hand_value

    def get_card(self):
        if self.hand_value > 21:
            print ("You are burned ")
            return self.hand, self.hand_value
        elif self.second_hand_value == 21:
            print ("GOT 21")
            return self.hand, self.hand_value
        else:
            deck = {"Hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                    "Diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                    "Clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                    "Picks": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
                    }

            drawn_card = list(random.choice(deck.items()))
            drawn_card = [drawn_card[0], random.choice(drawn_card[1])]
            deck.pop(drawn_card[0], drawn_card[1])  # Erasing the drawn card from the dictionary
            self.hand.append(drawn_card)

            self.hit_counter += 1 #calculates how many times have the player hit to get the cards vale

            if self.hand[self.hit_counter - 1][1] == "Jack":
                self.hand_value += 10
            elif self.hand[self.hit_counter - 1][1] == "Queen":
                self.hand_value += 10
            elif self.hand[self.hit_counter - 1][1] == "King":
                self.hand_value += 10
            elif self.hand[self.hit_counter - 1][1] == "Ace":
                self.hand_value += 11
                self.ace_counter += 1
            else:
                self.hand_value += self.hand[self.hit_counter - 1][1]

            if ("Ace" in self.hand) and (self.hand_value > 21) and (self.ace_counter > 0):
                self.ace_counter -= 1
                self.hand_value -= 10

            return self.hand, self.hand_value

    def make_bet(self):

        while True:
            try:
                self.bet = int(raw_input("Enter a number to bet"))
                print (" your bet is: ", self.bet)
            except ValueError:
                print (" Enter a valid number")
                continue # Looping again to get a valid value
            else:
                break
                # Bet entered successfully

        if self.bet <= self.money:
            self.money -= self.bet
        else:
            print ("Not enough money to bet!!!")
            return False

    def player_turn(self):

        while True:
            print "{} your Cards are: {}".format(self.name, self.hand)
            p_decision = raw_input("Enter Stand, Hit, Split or Double")

            if p_decision == "Stand":
                break
            elif p_decision == "Hit":

                if self.hand_value > 21:
                    print ("Passed 21!")
                    break
                else:
                    self.get_card()
                    continue

            elif p_decision == "Split":

                if self.hand[0][1] == self.hand[1][1]:
                    self.second_bet += self.bet
                    self.money -= self.bet
                    self.hand = self.hand[0]  #First card stays in hand #1
                    self.second_hand = self.hand[1]  #Second card goes to hand #2
                    self.get_card()
                    self.get_split()
                    self.player_turn()

                else:
                    print ("Can't split unequal cards!")

            elif p_decision == "Double":
                self.money -= self.bet
                self.bet *= 2
                self.get_card()
                break

    def dealer_turn(self):

        while Dealer.hand_value <= 17:
            self.get_card()


class SplitPlayer(CardPlayer):
    pass
Dealer = CardPlayer("Dealer", [], [], 50000, [], [])
PlayerOne = CardPlayer("Ben", [], [], 5000, [], [])
PlayerTwo = CardPlayer("Roni", [], [], 5000, [], [])

PlayerOne.make_bet()
print PlayerOne.money

PlayerTwo.make_bet()
print PlayerTwo.money

"""Starting the game with dealing each player 2 cards!"""
i = 0
while i < 2:
    PlayerOne.get_card()
    PlayerTwo.get_card()
    Dealer.get_card()
    i += 1
print("Player one's hand is: ",PlayerOne.hand)
print ("Dealer's face-up card is:",Dealer.hand[0][::])
PlayerOne.player_turn()
print("Player two's hand is: ",PlayerTwo.hand)
print ("Dealer's face-up card is:",Dealer.hand[0][::])
PlayerTwo.player_turn()
"""Bets are over, Dealer drawing!!!"""
print ("Player One hand value is {}".format(PlayerOne.hand_value))
print ("Player Two hand value is {}".format(PlayerTwo.hand_value))
while Dealer.hand_value < 17:##Conversion needed for hand_value #Dealer stops hitting at 17
    Dealer.get_card()
    if Dealer.hand_value >= 17:
        break
print "Dealer cards: ", Dealer.hand
print ("Dealer's Cards value is : {}".format(Dealer.hand_value))
"""Concluding the game"""

if Dealer.hand_value <= 21:
    if Dealer.hand_value > PlayerOne.hand_value:
        Dealer.money += PlayerOne.bet
        PlayerOne.bet = 0
        print("Dealer beat Player One!")
    elif Dealer.hand_value == PlayerOne.hand_value:
        print("Player One tied with Dealer!")
    else:
        PlayerOne.bet *= 2
        PlayerOne.money += PlayerOne.bet
        PlayerOne.bet = 0
        print ("Dealer lost to Player One!")

if Dealer.hand_value <= 21:
    if Dealer.hand_value > PlayerTwo.hand_value:
        Dealer.money += PlayerTwo.bet
        PlayerTwo.bet = 0
        print("Dealer beat Player Two!")
    elif Dealer.hand_value == PlayerTwo.hand_value:
        print("Player Two tied with Dealer!")
    else:

        PlayerTwo.bet *= 2
        PlayerTwo.money += PlayerTwo.bet
        PlayerTwo.bet = 0
        print ("Dealer lost to Player Two!")
else:
    print "Dealer got burned!!"




