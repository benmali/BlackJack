import random
#import tkinter
#top = tkinter.Tk()

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
        self.stand_flag = 0
        self.deck  = {"Hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Picks": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
            }

    def __repr__(self):
        return "CardPlayer('{}','{}')".format(self.name, self.hand)

    def reset(self):
        self.hand = []
        self.second_bet = 0
        self.second_hand = []
        self.second_hand_value = 0
        self.hand_value = 0
        self.hit_counter = 0
        self.hit_counter2 = 0
        self.ace_counter = 0
        self.ace_counter2 = 0
        self.split = 0
        self.stand_flag = 0

    def conclude(self):#not done yet!
        if self.hand_value > 21:
            self.lost()
            print("{} is burned, lost this hand".format(self.name))
            return
        if len(self.second_hand) != 0:
            if self.hand_value <= 21 and Dealer.hand_value > self.hand_value and (Dealer.hand_value <= 21):
                self.lost()
                print("Dealer Won against 1st hand")
            if self.second_hand_value <= 21 and Dealer.hand_value > self.second_hand_value and (Dealer.hand_value <= 21):
                self.win()
                print("Dealer Won against 2nd hand")
            if self.hand_value <= 21 and Dealer.hand_value < self.hand_value:
                self.win()
                print("Dealer Lost against 1st hand")
            if self.second_hand_value <= 21 and Dealer.hand_value < self.second_hand_value:
                self.win()
                print("Dealer Lost against 2nd hand")
        if self.hand_value <= 21 and Dealer.hand_value > self.hand_value and (Dealer.hand_value <= 21):
            self.lost()
            print("Dealer Won against {}".format(self.name))
            return
        if self.hand_value <= 21 and Dealer.hand_value < self.hand_value and (Dealer.hand_value <= 21):
            self.win()
            print("{} Won against the dealer".format(self.name))
            return
        if Dealer.hand_value > 21 and self.hand_value <=21:
            self.win()
            print ("Dealer burned, {} won the hand".format(self.name))
            return
        if (self.hand_value <= 21) and (Dealer.hand_value > self.hand_value) and (Dealer.hand_value <= 21):
            self.lost()
            print("Dealer Won against {}".format(self.name))



    def win(self):
        self.bet *= 2
        self.money += self.bet
    def lost(self):
        self.money -= self.bet
    def tie(self):
        self.money += self.bet
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

        """Gets the 2nd Card to user's 2nd hand when user splits"""
        if len(self.second_hand) == 1:  # Draws Automatically when user splits
            self.deal_hand1()
            self.deal_hand2()
            return self.hand, self.hand_value, self.second_hand, self.second_hand_value

        "Regular Hit"
        if self.stand_flag == 0:
            self.deal_hand1()
        if self.stand_flag == 1:
            self.deal_hand2()
        return self.hand, self.hand_value, self.second_hand, self.second_hand_value

    def conv_value(self,value):
        if value == "Jack" or value == "Queen" or value == "King":
            return 10
        elif value == "Ace":
            return 11
        else:
            return value

    def deal_hand1(self):
        drawn_card = list(random.choice(self.deck.items()))
        drawn_card = [drawn_card[0], random.choice(drawn_card[1])]
        self.hand.append(drawn_card)
        self.hit_counter += 1  # calculates how many times have the player hit to get the cards vale
        self.hand_value += self.conv_value(self.hand[self.hit_counter - 1][1])
        if self.hand[self.hit_counter - 1][1] == "Ace":
            self.ace_counter += 1
        if (self.hand_value > 21) and (self.ace_counter > 0):
            self.ace_counter -= 1
            self.hand_value -= 10

    def deal_hand2(self):
        drawn_card = list(random.choice(self.deck.items()))
        drawn_card = [drawn_card[0], random.choice(drawn_card[1])]
        self.second_hand.append(drawn_card)
        self.hit_counter2 += 1  # calculates how many times have the player hit to get the cards vale
        self.second_hand_value += self.conv_value(self.second_hand[self.hit_counter2 - 1][1])
        if self.second_hand[self.hit_counter2 - 1][1] == "Ace":
            self.ace_counter2 += 1

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

            if self.hand_value >= 21 and self.split == 1:
                """In case 1st hand is burned but didnt play 2nd"""
                pass
            elif self.second_hand_value >= 21:
                print ("")
                print ("{} your hand is {}, you got burned!".format(self.name, self.second_hand))
                break
            elif self.hand_value >= 21 and self.split == 0:
                print ("")
                print ("{} your hand is {}, you got burned!".format(self.name,self.hand))
                break

            if self.stand_flag == 0:
                print("")
                print "{} your Cards are: {}, card value: {}".format(self.name, self.hand,self.hand_value)
            if self.stand_flag == 1:
                print("")
                print "This is your 2nd hand"
                print "{} your Cards are: {}, card value: {}".format(self.name, self.second_hand,self.second_hand_value)
            p_decision = raw_input("Enter Stand, Hit, Split or Double")

            if p_decision == "Stand" or p_decision == "stand" or p_decision == "s":
                if len(self.second_hand) == 0:
                    break
                elif self.stand_flag == 1:
                    break

                elif len(self.second_hand) == 2 and self.split == 1:
                    self.stand_flag = 1

            elif p_decision == "Hit" or p_decision == "hit" or p_decision == "h":
                self.get_card()

            elif p_decision == "Split" or  p_decision == "split" or p_decision == "sp":
                if self.conv_value(self.hand[0][1]) == self.conv_value(self.hand[1][1]):
                    self.second_bet += self.bet
                    self.money -= self.bet
                    self.second_hand = [list(self.hand[1])]  # Second card goes to hand #2
                    self.second_hand_value = self.conv_value(self.second_hand[0][1])
                    self.hand = [list(self.hand[0])]  # First card stays in hand #1
                    self.hand_value = self.conv_value(self.hand[0][1])
                    self.hit_counter = 1
                    self.hit_counter2 = 1
                    self.deal_hand1()
                    self.deal_hand2()
                    self.split += 1
                    continue

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


    print ("Dealer's face-up card is:", Dealer.hand[1][::])
    PlayerOne.player_turn()
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
    PlayerOne.conclude()
    PlayerTwo.conclude()
    while True:
        y = raw_input("Play again? Press Yes or No")
        if y == "Yes" or "yes" or"y":
            PlayerOne.reset()
            PlayerTwo.reset()
            Dealer.reset()
            start_game()
        else:
            exit()


Dealer = CardPlayer("Dealer", [], [], 50000, [], [])
PlayerOne = CardPlayer("Ben", [], [], 5000, [], [])
PlayerTwo = CardPlayer("Roni", [], [], 5000, [], [])
start_game()



