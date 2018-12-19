import random
import Tkinter as BLACKJACK
from Tkinter import *





class CardPlayer:

    def __init__(self, name, hand, second_hand , money , bet, second_bet,win ):
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
        self.black_jack = 0
        self.deck  = {"Hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Picks": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
            }
        frame = Frame(win)
        frame.pack()
        self.hitButton = Button(win, text="Hit", fg="green", bg="white", command=self.deal_hand1)
        self.standButton = Button(win, text="Stand", fg="red", bg="white", command=self.stand)
        self.splitButton = Button(win, text="Split", fg="blue", bg="white", command=self.split)
        self.doubleButton = Button(win, text="Double", fg="blue", bg="white")
        self.hitButton.pack(side=LEFT)
        self.standButton.pack(side=LEFT)
        self.splitButton.pack(side=LEFT)
        self.doubleButton.pack(side=LEFT)
        startbutton = Button(win, text="Start", fg="green", bg="white", )
        startbutton.config(command=main_game)
        startbutton.pack(side=TOP)



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
        self.black_jack = 0

    def conclude(self):
        if self.hand_value > 21:
            print("{} is burned, lost this hand".format(self.name))
            return
        if len(self.second_hand) != 0:
            if self.hand_value <= 21 and Dealer.hand_value > self.hand_value and (Dealer.hand_value <= 21):
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
            print("Dealer Won against {}".format(self.name))

    def win(self):
        self.bet *= 2
        self.money += self.bet

    def winbj(self):
        self.bet *= 2.5
        self.money += self.bet

    def tie(self):
        self.money += self.bet

    def first_cards(self): #to be deleted

        """First deal of the game"""
        if self.hand == [] and (self.split == 0):
            for i in range(2):
                self.deal_hand1()
            return self.hand, self.hand_value, self.second_hand, self.second_hand_value


    def make_bet(self):

        while True:
            try:
                label = Label(win, text="Entter a number to bet.")
                label.pack
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

    def conv_value(self, value):
        if value == "Jack" or value == "Queen" or value == "King":
            return 10
        elif value == "Ace":
            return 11
        else:
            return value

    def hit(self):
        if self.stand_flag == 0:
            self.deal_hand1()
        if self.stand_flag == 1:
            self.deal_hand2()
        return self.hand, self.hand_value, self.second_hand, self.second_hand_value

    def stand(self):
        if len(self.second_hand) == 0:
            return
        elif self.stand_flag == 1:
            return
        elif len(self.second_hand) == 2 and self.split == 1:
            self.stand_flag = 1

    def split_cards(self):
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
        else:
            print ("Can't split unequal cards!")

    def double(self):
        self.money -= self.bet
        self.bet *= 2
        self.get_card()

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

    def dealer_turn(self):

        while Dealer.hand_value <= 17:
            self.get_card()

    def player_turn(self):

        while True:

            if self.hand_value > 21 and self.split == 1:
                """In case 1st hand is burned but didnt play 2nd"""
                self.stand_flag = 1
                self.split = 0
                continue
            if self.hand_value == 21:
                if self.conv_value(self.hand[0][0]) == 10 and self.conv_value(self.hand[0][1]) == 11:
                    print ("{} your hand is {}, you got BlackJack!".format(self.name, self.hand))
                    self.black_jack = 1
                    break
                if self.conv_value(self.hand[0][0]) == 11 and self.conv_value(self.hand[0][1]) == 10:
                    print ("{} your hand is {}, you got BlackJack!".format(self.name, self.hand))
                    self.black_jack = 1
                    break
                print ("{} your hand is {}, you got 21!".format(self.name, self.hand))
                break

            if self.second_hand_value > 21:
                print ("")
                print ("{} your hand is {}, you got burned!".format(self.name, self.second_hand))
                break
            if self.hand_value > 21 and self.split == 0:
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
                if self.split == 1 and self.stand_flag == 1:
                    self.deal_hand2()
                else:
                    self.deal_hand1()

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
                if self.split == 1 and self.stand_flag == 1:
                    self.deal_hand2()
                    break
                else:
                    self.deal_hand1()
                break


def main_game():
    players = [PlayerOne, PlayerTwo]
    for player in players:
        player.make_bet()
        print str(player.money) + "\n"

    for i in range(2):
        for player in players:
            player.deal_hand1()
        Dealer.deal_hand1()
    for player in players:
        print ("Dealer's face-up card is:", Dealer.hand[1][::])
        player.player_turn()

    #Bets are over, Dealer drawing!!
    while Dealer.hand_value < 17:
        Dealer.deal_hand1()
        if Dealer.hand_value >= 17:
            break
    print "Dealer cards: ", Dealer.hand
    print ("Dealer's Cards value is : {}".format(Dealer.hand_value))
    for player in players:
        print ("{} hand value is {}".format(player.name, player.hand_value))
        player.conclude()
    #Concluding the game
    while True:
        y = raw_input("Play again? Press Yes or No")
        if y == "Yes" or "yes" or "y":
            PlayerOne.reset()
            PlayerTwo.reset()
            Dealer.reset()
            main_game()
        else:
            break

win = Tk()
win.geometry("500x600")


Dealer = CardPlayer("Dealer", [], [], 50000, [], [],win)
PlayerOne = CardPlayer("Ben", [], [], 5000, [], [],win)
PlayerTwo = CardPlayer("Roni", [], [], 5000, [], [],win)
startbutton = Button(win, text="Start", fg="green", bg="white",)
startbutton.config(command = main_game)




win.after(1000,main_game)

win.mainloop()

