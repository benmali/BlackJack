import random
from random import  randint
import itertools


class CardPlayer:




    def __init__(self, name, hand, second_hand, money, bet, second_bet):
        self.name = name
        self.hand = []
        self.money = money
        self.bet = bet
        self.second_bet = 0
        self.second_hand = []
        self.second_hand_value = 0
        self.hand_value = 0
        self.hit_counter = 0
        self.hit_counter2 = 0
        self.ace_counter = 0
        self.ace_counter2 = 0
        self.split = 0
        self.deck  = {"Hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Picks": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
            }



    def __repr__(self):
        return "CardPlayer('{}','{}')".format(self.name, self.hand)


    
    def get_player_list(self):
        players_list = raw_input("Enter player names")
        players_list = list(players_list.split(" "))
        print (players_list)
        return players_list

   
    def get_card(self):

        """First deal of the game"""
        if self.hand == [] and (self.split == 0):
            for i in range(2):
                self.deal_hand1()
            return self.hand, self.hand_value, self.second_hand, self.second_hand_value
        "Regular Hit"
        if self.second_hand == [] and (self.hit_counter >= 2) and (self.split == 0):
            self.deal_hand1()
        """Gets the 2nd Card to user's 2nd hand when user splits"""
        if len(self.second_hand) == 1: #Draws Automatically when user splits
            self.deal_hand1()
            self.deal_hand2()
        if len(self.second_hand) >= 2 and (self.split == 1):
            self.deal_hand2()

        return self.hand, self.hand_value, self.second_hand, self.second_hand_value

    def deal_hand1(self):
        drawn_card = list(random.choice(self.deck.items()))
        drawn_card = [drawn_card[0], random.choice(drawn_card[1])]
        #self.deck.pop(drawn_card[0], drawn_card[1])  # Erasing the drawn card from the dictionary
        self.hand.append(drawn_card)

        self.hit_counter += 1  # calculates how many times have the player hit to get the cards vale

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

        if (self.hand_value > 21) and (self.ace_counter > 0):
            self.ace_counter -= 1
            self.hand_value -= 10

    def deal_hand2(self):
        drawn_card = list(random.choice(self.deck.items()))
        drawn_card = [drawn_card[0], random.choice(drawn_card[1])]
        #self.deck.pop(drawn_card[0], drawn_card[1])  # Erasing the drawn card from the dictionary
        self.second_hand.append(drawn_card)
        self.hit_counter2 += 1  # calculates how many times have the player hit to get the cards vale

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

        if (self.second_hand_value > 21) and (self.ace_counter2 > 0):
            self.ace_counter2 -= 1
            self.second_hand_value -= 10


    def make_bet(self):

        while True:
            try:
                self.bet = int(raw_input("Enter a number to bet"))
                print (" your bet is: ", self.bet)
            except ValueError:
                print (" Enter a valid number")
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
            if self.hand_value >= 21:

                break

            print "{} your Cards are: {}".format(self.name, self.hand)
            p_decision = raw_input("Enter Stand, Hit, Split or Double")
            if self.split == 1:
                print "This is your 2nd hand"

            if p_decision == "Stand" or "stand" or "s":
                if len(self.second_hand) == 2:
                    self.split += 1
                    self.player_turn()
                else:
                    break
            elif p_decision == "Hit" or "hit" or "h":
                    self.get_card()

            elif p_decision == "Split" or "split" or "sp":

                if self.hand[0][1] == self.hand[1][1]:
                    self.second_bet += self.bet
                    self.money -= self.bet
                    self.hand = self.hand[0]  #First card stays in hand #1
                    self.second_hand = self.hand[1]  #Second card goes to hand #2
                    self.get_card()
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






def start_game():


    PlayerOne.make_bet()
    print PlayerOne.money

    PlayerTwo.make_bet()
    print PlayerTwo.money

    """Starting the game with dealing each player 2 cards!"""

    PlayerOne.get_card()
    PlayerTwo.get_card()
    Dealer.get_card()

    print("Player one's hand is: ", PlayerOne.hand)
    print ("Dealer's face-up card is:", Dealer.hand[1][::])
    PlayerOne.player_turn()
    print("Player two's hand is: ", PlayerTwo.hand)
    print ("Dealer's face-up card is:", Dealer.hand[1][::])
    PlayerTwo.player_turn()
    """Bets are over, Dealer drawing!!!"""
    print ("Player One hand value is {}".format(PlayerOne.hand_value))
    print ("Player Two hand value is {}".format(PlayerTwo.hand_value))
    while Dealer.hand_value < 17:  ##Conversion needed for hand_value #Dealer stops hitting at 17
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

    while True:
        y = raw_input("Play again? Press Yes or No")
        if y == "Yes" or "yes" or"y":
            PlayerOne.hand = []
            PlayerOne.second_hand = []
            PlayerOne.hand_value = 0
            PlayerOne.second_hand_value = 0
            PlayerTwo.hand = []
            PlayerTwo.second_hand = []
            PlayerTwo.hand_value = 0
            PlayerTwo.second_hand_value = 0
            Dealer.hand = []
            Dealer.hand_value = 0
            PlayerOne.hit_counter = 0
            PlayerTwo.hit_counter = 0
            PlayerTwo.hit_counter2 = 0
            PlayerOne.hit_counter2 = 0
            Dealer.hit_counter = 0
            start_game()


        else:
            exit()

Dealer = CardPlayer("Dealer", [], [], 50000, [], [])
PlayerOne = CardPlayer("Ben", [], [], 5000, [], [])
PlayerTwo = CardPlayer("Roni", [], [], 5000, [], [])
start_game()



