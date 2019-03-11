import random
from Tkinter import *
import threading
import time
from PIL import ImageTk, Image
import os


class CardPlayer:
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.money = money
        self.bet = 0
        self.second_bet = 0
        self.second_hand = []
        self.second_hand_value = 0
        self.hand_value = 0
        self.hit_counter = 0
        self.hit_counter2 = 0
        self.ace_counter = 0
        self.ace_counter2 = 0
        self.split = 0
        self.stand_flag = False
        self.stand2 = True
        self.black_jack = 0
        self.deck = {"Hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                     "Diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                     "Clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
                     "Spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]}

    def __repr__(self):
        return "CardPlayer('{}','{}')".format(self.name, self.hand)

    def reset(self):
        self.hand = []
        self.bet = 0
        self.second_bet = 0
        self.second_hand = []
        self.second_hand_value = 0
        self.hand_value = 0
        self.hit_counter = 0
        self.hit_counter2 = 0
        self.ace_counter = 0
        self.ace_counter2 = 0
        self.split = 0
        self.stand_flag = False
        self.stand2 = True
        self.black_jack = 0
        play = True

    def conclude(self):
        c = Canvas(win, bg="white", height=400, width=500)
        if self.hand_value > 21:  # Regular Burn
            print("{} is burned, lost this hand".format(self.name))
            c.create_text(200, 20, fill="black", font="Times 14 bold",
                                    text="{} is burned!".format(self.name))
            c.place(relx=0.5, rely=0.5, anchor=CENTER)
            time.sleep(2.5)
            play = False
            return
        if len(self.second_hand) != 0:  # Split situation
            if self.hand_value <= 21 and Dealer.hand_value > self.hand_value and (Dealer.hand_value <= 21):
                print("Dealer Won against 1st hand")
                c.create_text(200, 20, fill="black", font="Times 14 bold",
                              text="Dealer Won against {}'s 1st hand".format(self.name))
                c.place(relx=0.5, rely=0.5, anchor=CENTER)
            if self.second_hand_value <= 21 and Dealer.hand_value > self.second_hand_value and (Dealer.hand_value <= 21):
                self.win()
                print("Dealer Won against 2nd hand")
                c.create_text(200, 50, fill="black", font="Times 14 bold",
                              text="Dealer Won against {}'s 2nd hand".format(self.name))
                c.place(relx=0.5, rely=0.5, anchor=CENTER)
                time.sleep(2.5)
            if self.hand_value <= 21 and Dealer.hand_value < self.hand_value:
                self.win()
                print("Dealer Lost against 1st hand")
                c.create_text(200, 20, fill="black", font="Times 14 bold",
                              text="Dealer won against {}'s 1st hand".format(self.name))
                c.place(relx=0.5, rely=0.5, anchor=CENTER)
            if self.second_hand_value <= 21 and Dealer.hand_value < self.second_hand_value:
                self.win()
                print("Dealer Lost against 2nd hand")
                c.create_text(200, 50, fill="black", font="Times 14 bold",
                              text="Dealer lost against {}'s 2nd hand".format(self.name))
                c.place(relx=0.5, rely=0.5, anchor=CENTER)
                time.sleep(2.5)
        if self.hand_value <= 21 and Dealer.hand_value > self.hand_value and (Dealer.hand_value <= 21):
            print("Dealer Won against {}".format(self.name))
            c.create_text(200, 20, fill="black", font="Times 14 bold",
                          text="Dealer Won against {}".format(self.name))
            c.place(relx=0.5, rely=0.5, anchor=CENTER)
            time.sleep(2.5)
            play = False
            return
        if self.hand_value <= 21 and Dealer.hand_value < self.hand_value and (Dealer.hand_value <= 21):
            self.win()
            print("{} Won against the dealer".format(self.name))
            c.create_text(200, 20, fill="black", font="Times 14 bold",
                          text="{} Won against the Dealer".format(self.name))
            c.place(relx=0.5, rely=0.5, anchor=CENTER)
            time.sleep(2.5)
            play = False
            return
        if Dealer.hand_value > 21 and self.hand_value <= 21:
            self.win()
            print ("Dealer burned, {} won the hand".format(self.name))
            c.create_text(200, 20, fill="black", font="Times 14 bold",
                          text="Dealer burned, {} won the hand".format(self.name))
            c.place(relx=0.5, rely=0.5, anchor=CENTER)
            time.sleep(2.5)
            play = False
            return
        if (self.hand_value <= 21) and (Dealer.hand_value > self.hand_value) and (Dealer.hand_value <= 21):
            print("Dealer Won against {}".format(self.name))
            c.create_text(200, 20, fill="black", font="Times 14 bold",
                          text="Dealer Won against {}".format(self.name))
            c.place(relx=0.5, rely=0.5, anchor=CENTER)
            time.sleep(2.5)
            play = False
            return
        if (self.hand_value <= 21) and (Dealer.hand_value == self.hand_value) and (Dealer.hand_value <= 21):
            print("Dealer is tied against {}".format(self.name))
            self.tie()
            c.create_text(200, 20, fill="black", font="Times 14 bold",
                          text="Dealer is tied against {}".format(self.name))
            c.place(relx=0.5, rely=0.5, anchor=CENTER)
            time.sleep(2.5)
            play = False
            return

    def win(self):
        self.bet *= 2
        self.money += self.bet

    def winbj(self):
        self.bet *= 2.5
        self.money += self.bet

    def tie(self):
        self.money += self.bet


    def make_bet(self):

            try:
                if self.bet > 0:
                    time.sleep(0.1)
                    win.update()

                label = Label(win, text="{}, Enter a number to bet!".format(self.name))
                label.pack()
                input = Entry(win, textvariable=self.bet)
                input.pack()
                time.sleep(5)
                self.bet = int(input.get())
                input.destroy()
                label.destroy()
                time.sleep(0.1)
                win.update()

                print (" your bet is: ", self.bet)

                # Bet entered successfully

                if self.bet <= self.money:
                    self.money -= self.bet

                else:
                    print ("Not enough money to bet!!!")

            except ValueError: # If bet was not entered on time, a default bet of 1 is given
                input.destroy()
                label.destroy()


    def conv_value(self, value):
        if value == "Jack" or value == "Queen" or value == "King":
            return 10
        elif value == "Ace":
            return 11
        else:
            return value

    def hit(self):
        if not self.stand_flag:
            self.deal_hand1()
        if self.stand_flag and self.split == 1:
            self.deal_hand2()
        return self.hand, self.hand_value, self.second_hand, self.second_hand_value

    def stand(self):
        if len(self.second_hand) == 0:
            self.stand_flag = True
            return
        elif self.stand_flag == True and self.split == 1:
            self.stand2 = True
            return
        elif len(self.second_hand) == 2 and self.split == 1:
            self.stand_flag = True


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
            self.stand2 = False
        else:
            print ("Can't split unequal cards!")

    def double(self):
        if  not self.stand2 or not self.stand_flag:
            if len(self.hand) == 2 or len(self.second_hand) == 2:
                self.money -= self.bet
                self.bet *= 2
                if not self.stand_flag and self.split == 0:
                    self.deal_hand1()
                    self.stand_flag = True
                    return
                if self.stand_flag and self.split == 1:
                    self.deal_hand2()
                    self.stand2 = True
                    return
                if not self.stand_flag and self.split == 1:
                    self.deal_hand1()
                    self.stand_flag = True
                    return
                else:
                    return


    def deal_hand1(self):
        if not self.stand_flag : #regular scenario
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

        if self.stand_flag and self.split == 1:
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


    def show_cards(self):
        imglst = []
        start_pos = [100, 250]
        c = Canvas(win, bg="white", height=400, width=500)
        if self.name == "Dealer":
            c.create_text(200, 30, fill="black", font="Times 10 italic bold",
                          text="Dealer Drawing!".format(self.name))
            start_pos = [220, 140]
            for i in range(len(self.hand)):
                value = self.hand[i][1]
                symbol = (self.hand[i][0]).lower()
                image = Image.open(str(os.getcwd()) + "/cards/{}/{}/{}.png".format(value, symbol, value))
                image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
                img = ImageTk.PhotoImage(image)
                imglst.append(img)
            for img in imglst:
                c.create_image(tuple(start_pos), image=img)  ##### add location instead of anchor
                c.place(relx=0.5, rely=0.5, anchor=CENTER)
                start_pos[0] += 40
                start_pos[1] += 20
            time.sleep(2)
            return

        for i in range(len(self.hand)):  # displaying cards for players, regardless of split
            value = self.hand[i][1]
            symbol = (self.hand[i][0]).lower()
            image = Image.open(str(os.getcwd()) + "/cards/{}/{}/{}.png".format(value, symbol, value))
            image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
            img = ImageTk.PhotoImage(image)
            imglst.append(img)
        for img in imglst:
            image = Image.open(
                str(os.getcwd()) + "/cards/{}/{}/{}.png".format(Dealer.hand[1][1],
                                                                Dealer.hand[1][0],
                                                                Dealer.hand[1][1]))
            image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
            im = ImageTk.PhotoImage(image)
            c.create_image((260, 105), image=im)  # coordinates are position of image
            c.create_image(tuple(start_pos), image=img)  ##### add location instead of anchor
            c.place(relx=0.5, rely=0.5, anchor=CENTER)
            start_pos[0] += 40
            start_pos[1] += 20
        if self.split == 0:
            c.create_text(250, 20, fill="black", font="Times 9 bold",
                          text="{} your cards value is {}\nDealer upside card is {} ".format(self.name, self.hand_value,
                                                                                             Dealer.hand[1][:]))
            time.sleep(2)
            return

        if self.split == 1:  # if split happens, display hand 2
            start_pos = [300, 250]
            imglst2 = []
            for i in range(len(self.second_hand)):
                value = self.second_hand[i][1]
                symbol = (self.second_hand[i][0]).lower()
                image = Image.open(
                    str(os.getcwd()) + "/cards/{}/{}/{}.png".format(value, symbol, value))
                image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
                img = ImageTk.PhotoImage(image)
                imglst2.append(img)
            for img in imglst2:
                image = Image.open(
                    str(os.getcwd()) + "/cards/{}/{}/{}.png".format(Dealer.hand[1][1],
                                                                                      Dealer.hand[1][0],
                                                                                      Dealer.hand[1][1]))
                image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
                im = ImageTk.PhotoImage(image)
                c.create_image((260, 105), image=im)  # coordinates are position of image
                c.create_image(tuple(start_pos), image=img)  ##### add location instead of anchor
                c.place(relx=0.5, rely=0.5, anchor=CENTER)
                start_pos[0] += 40
                start_pos[1] += 20
            if not self.stand_flag:
                c.create_text(250, 20, fill="black", font="Times 9 bold",
                          text="{} your cards value is {}\nDealer upside card is {} ".format(self.name, self.hand_value,
                                                                                             Dealer.hand[1][:]))
                time.sleep(2)
                return
            if self.stand_flag:
                c.create_text(250, 20, fill="black", font="Times 9 bold",
                              text="{} your cards value is {}\nDealer upside card is {} ".format(self.name,
                                                                                                 self.second_hand_value,
                                                                                                 Dealer.hand[1][:]))
                time.sleep(2)
                return

    def player_turn(self):
        while True:  # Player gets 7 seconds to play his hand, or he stands automatically
            try:
                self.show_cards()
                if self.hand_value > 21 and self.split == 0:  # common condition for burning
                    self.show_cards()
                    print ("")
                    print ("{} your hand is {}, you got burned!".format(self.name, self.hand))
                    break

                if self.hand_value > 21 and self.split == 1:  # In case 1st hand is burned but didn't play 2nd
                    self.show_cards()
                    self.stand_flag = True

                if self.hand_value == 21:
                    if self.conv_value(self.hand[0][0]) == 10 and self.conv_value(
                            self.hand[0][1]) == 11:  # BLACKJACK
                        print ("{} your hand is {}, you got BlackJack!".format(self.name, self.hand))
                        self.black_jack = 1
                    self.stand_flag = True

                if len(self.second_hand) > 0:

                    if self.second_hand_value > 21 and self.stand_flag:  # stand on first hand, burn on 2nd
                        self.show_cards()
                        print ("")
                        print ("{} your hand is {}, you got burned!".format(self.name, self.second_hand))
                        self.stand2 = True

                    if self.second_hand_value == 21:
                        if self.conv_value(self.second_hand[0][0]) == 10 and self.conv_value(self.second_hand[0][1]) == 11:  # BLACKJACK
                            print ("{} your hand is {}, you got BlackJack!".format(self.name, self.second_hand))
                            self.black_jack = 1
                        self.stand2 = True

                if self.stand_flag and self.stand2:
                        self.show_cards()
                        break

            except IOError:
                print("IO error")


def play_again():
    global play
    play = True
    PlayerOne.reset()
    PlayerTwo.reset()
    Dealer.reset()


def create_bet_canvas():
    b = Canvas(win, bg="white", height=80, width=150)
    b.place(x=60, y=20)
    b.create_text(70, 20, fill="black", font="Times 8 bold",
                  text="{} your bank is {} ".format(PlayerOne.name, PlayerOne.money))
    b.create_text(70, 50, fill="black", font="Times 8 bold",
                  text="{} your bank is {} ".format(PlayerTwo.name, PlayerTwo.money))


def main_game():

    while True:

        players = [PlayerOne, PlayerTwo]

        create_bet_canvas()
        for player in players:
            player.make_bet()
            create_bet_canvas()
            print str(player.money) + "\n"
        players = [player for player in players if player.bet > 0]  # player without bet is excluded

        for i in range(2):
            for player in players:
                player.deal_hand1()
            Dealer.deal_hand1()
        for player in players:
            print ("Dealer's face-up card is:", Dealer.hand[1][::])
            player.player_turn()
        #Bets are over, Dealer drawing!!
        while True:
            if Dealer.hand_value < 17:
                Dealer.show_cards()
                Dealer.deal_hand1()
            if Dealer.hand_value >= 17:
                Dealer.show_cards()
                break
        print "Dealer cards: ", Dealer.hand
        print ("Dealer's Cards value is : {}".format(Dealer.hand_value))
        for player in players:
            print ("{} hand value is {}".format(player.name, player.hand_value))
            player.conclude()
        b = Canvas(win, bg="white", height=80, width=150)
        b.place(x=60, y=20)
        b.create_text(70, 20, fill="black", font="Times 8 bold",
                      text="{} your bank is {} ".format(PlayerOne.name, PlayerOne.money))
        b.create_text(70, 50, fill="black", font="Times 8 bold",
                      text="{} your bank is {} ".format(PlayerTwo.name, PlayerTwo.money))
        c = Canvas(win, bg="white", height=450, width=200)
        c.place(x=270, y=250)
        button1 = Button(c, text="Play Again", command=play_again,
                         anchor=W)
        button1.configure(width=10, activebackground="#33B5E5",
                          relief=FLAT)
        button1.pack()
        global play
        play = False
        time.sleep(10)
        if play:
            c.delete(button1)
            win.update()
            pass
        else:
            break


win = Tk()
win.geometry("1000x600")
win.title('Black Jack')
Dealer = CardPlayer("Dealer", 50000)
PlayerOne = CardPlayer("Ben", 5000)
PlayerTwo = CardPlayer("Roni", 5000)
players = [PlayerOne, PlayerTwo]
global play
play = True
thread = threading.Thread(target=main_game)

# make loop terminate when the user exits the window
thread.daemon = True
thread.start()

# defining GUI and buttons outside of class:
frame = Frame(win)
frame.pack()
# player 1 buttons
hitButton = Button(win, text="Hit - {}".format(PlayerOne.name), fg="green", bg="white", command=PlayerOne.deal_hand1)
standButton = Button(win, text="Stand", fg="red", bg="white", command=PlayerOne.stand)
splitButton = Button(win, text="Split", fg="blue", bg="white", command=PlayerOne.split_cards)
doubleButton = Button(win, text="Double", fg="blue", bg="white",command =PlayerOne.double)
hitButton.place(x=310, y=550)
standButton.place(x=365, y=550)
splitButton.place(x=403, y=550)
doubleButton.place(x=435, y=550)

# player 2 buttons
hitButton = Button(win, text="Hit - {}".format(PlayerTwo.name), fg="green", bg="white", command=PlayerTwo.deal_hand1)
standButton = Button(win, text="Stand", fg="red", bg="white", command=PlayerTwo.stand)
splitButton = Button(win, text="Split", fg="blue", bg="white", command=PlayerTwo.split_cards)
doubleButton = Button(win, text="Double", fg="blue", bg="white",command = PlayerTwo.double)
hitButton.place(x=460+20, y=550)
standButton.place(x=510+30, y=550)
splitButton.place(x=553+25, y=550)
doubleButton.place(x=588+22, y=550)

win.mainloop()

