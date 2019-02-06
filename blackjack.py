import random
from Tkinter import *
import threading
import time
from PIL import ImageTk, Image
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
        self.elapsed = 0
        self.deck  = {"Hearts": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Diamonds": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Clubs": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"],
            "Spades": [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
            }


    def __repr__(self):
        return "CardPlayer('{}','{}')".format(self.name, self.hand)
    """
    def cards(self):
        for card in self.hand:
            # Setting it up
            img = ImageTk.PhotoImage(Image.open("C://users/ben/desktop/python projetcts/.png"))

            # Displaying it
            imglabel = Label(win, image=img).grid(row=1, column=1)
    """



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
            di = Label(win, text="{} is burned, lost this hand".format(self.name))
            di.pack()
            time.sleep(2)
            di.destroy()
            win.update()
            return
        if len(self.second_hand) != 0:
            if self.hand_value <= 21 and Dealer.hand_value > self.hand_value and (Dealer.hand_value <= 21):
                print("Dealer Won against 1st hand")
                di = Label(win, text="Dealer Won against 1st hand".format(self.name))
                di.pack()
                time.sleep(2)
                di.destroy()
                win.update()
            if self.second_hand_value <= 21 and Dealer.hand_value > self.second_hand_value and (Dealer.hand_value <= 21):
                self.win()
                print("Dealer Won against 2nd hand")
                di = Label(win, text="Dealer Won against 2nd hand".format(self.name))
                di.pack()
                time.sleep(2)
                di.destroy()
                win.update()
            if self.hand_value <= 21 and Dealer.hand_value < self.hand_value:
                self.win()
                print("Dealer Lost against 1st hand")
                di = Label(win, text="Dealer Lost against 1st hand")
                di.pack()
                time.sleep(2)
                di.destroy()
                win.update()
            if self.second_hand_value <= 21 and Dealer.hand_value < self.second_hand_value:
                self.win()
                print("Dealer Lost against 2nd hand")
                di = Label(win, text="Dealer Lost against 2nd hand")
                di.pack()
                time.sleep(2)
                di.destroy()
                win.update()
        if self.hand_value <= 21 and Dealer.hand_value > self.hand_value and (Dealer.hand_value <= 21):
            print("Dealer Won against {}".format(self.name))
            di = Label(win, text="Dealer Won against {}".format(self.name))
            di.pack()
            time.sleep(2)
            di.destroy()
            win.update()
            return
        if self.hand_value <= 21 and Dealer.hand_value < self.hand_value and (Dealer.hand_value <= 21):
            self.win()
            print("{} Won against the dealer".format(self.name))
            di = Label(win, text="{} Won against the dealer".format(self.name))
            di.pack()
            time.sleep(2)
            di.destroy()
            win.update()
            return
        if Dealer.hand_value > 21 and self.hand_value <=21:
            self.win()
            print ("Dealer burned, {} won the hand".format(self.name))
            di = Label(win, text="Dealer burned, {} won the hand".format(self.name))
            di.pack()
            time.sleep(2)
            di.destroy()
            win.update()
            return
        if (self.hand_value <= 21) and (Dealer.hand_value > self.hand_value) and (Dealer.hand_value <= 21):
            print("Dealer Won against {}".format(self.name))
            di = Label(win, text="Dealer Won against {}".format(self.name))
            di.pack()
            time.sleep(2)
            di.destroy()
            win.update()

    def win(self):
        self.bet *= 2
        self.money += self.bet

    def winbj(self):
        self.bet *= 2.5
        self.money += self.bet

    def tie(self):
        self.money += self.bet


    def make_bet(self):

        while True:
            try:
                while self.elapsed <=7:
                    label = Label(win, text="{}, Enter a number to bet!".format(self.name))
                    label.pack()
                    input = Entry(win, textvariable=self.bet)
                    input.pack()
                    time.sleep(2)
                    self.bet = int(input.get())
                    input.destroy()
                    label.destroy()
                    time.sleep(0.1)
                    win.update()
                    if self.bet > 0:
                        time.sleep(0.1)
                        win.update()
                        break
                    self.bet = int(raw_input("Enter a number to bet"))
                    print (" your bet is: ", self.bet)

                # Bet entered successfully

                if self.bet <= self.money:
                    self.money -= self.bet
                    break
                else:
                    print ("Not enough money to bet!!!")
                    return False

            except ValueError:
                input.destroy()
                label.destroy()
                print (" Enter a valid number")


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
            self.stand_flag = 2
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
        if self.split == 0:
            self.deal_hand1()
            self.stand_flag = 1
            return
        else:
            self.deal_hand2()
            self.stand_flag = 2
            return


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


    def player_turn(self):
        while True: # Player gets 7 seconds to play his hand, or he stands automatically
            try:
                imglst = []
                start_pos = [100,250]
                c = Canvas(win, bg = "white",height = 400, width = 500)
                for i in range(len(self.hand)):
                    value = self.hand[i][1]
                    symbol = (self.hand[i][0]).lower()
                    image = Image.open( "C://users/ben/desktop/python projects/cards/{}/{}/{}.png".format(value, symbol, value))
                    image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
                    img = ImageTk.PhotoImage(image)
                    imglst.append(img)
                for img in imglst:
                    image = Image.open(
                        "C://users/ben/desktop/python projects/cards/{}/{}/{}.png".format(Dealer.hand[1][1],
                                                                                          Dealer.hand[1][0],
                                                                                          Dealer.hand[1][1]))
                    image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
                    im = ImageTk.PhotoImage(image)
                    c.create_image((260, 70), image=im)  # coordinates are position of image
                    c.create_image(tuple(start_pos), image = img) ##### add location instead of anchor
                    c.place(relx=0.5, rely=0.5, anchor=CENTER)
                    start_pos[0] += 40
                    start_pos[1] += 20

                if self.hand_value > 21 and self.split == 1:
                    """In case 1st hand is burned but didnt play 2nd"""
                    self.stand_flag = 1
                    self.split = 0
                if self.hand_value == 21:
                    if self.conv_value(self.hand[0][0]) == 10 and self.conv_value(self.hand[0][1]) == 11:#BLACKJACK
                        label = Label(win, text="{} your hand is {}, you got BlackJack!".format(self.name, self.hand))
                        label.pack()
                        print ("{} your hand is {}, you got BlackJack!".format(self.name, self.hand))
                        self.black_jack = 1
                        break
                    if self.conv_value(self.hand[0][0]) == 11 and self.conv_value(self.hand[0][1]) == 10:# BLACKJACK
                        displ = Label(win, text="{} your hand is {}, you got BlackJack!".format(self.name, self.hand))
                        displ.pack()
                        time.sleep(3)
                        displ.destroy()
                        win.update()
                        print ("{} your hand is {}, you got BlackJack!".format(self.name, self.hand))
                        self.black_jack = 1
                        break
                    displ = Label(win, text="{} your hand is {}, you got 21!".format(self.name, self.hand))
                    displ.pack()
                    time.sleep(3)
                    displ.destroy()
                    win.update()
                    print ("{} your hand is {}, you got 21!".format(self.name, self.hand))
                    break

                if self.second_hand_value > 21:
                    llll = Label(win, text="{} your hand is {}, you got burned!".format(self.name, self.hand))
                    llll.pack()
                    time.sleep(3)
                    llll.destroy()
                    llll = Label(win, text="")
                    llll.pack()
                    llll.destroy()
                    win.update()
                    time.sleep(1)
                    print ("")
                    print ("{} your hand is {}, you got burned!".format(self.name, self.second_hand))
                    break
                if self.hand_value > 21 and self.split == 0:# common condition for burning
                    displ = Label(win,text="{} your hand is {}, you got burned!".format(self.name,self.hand))
                    displ.pack()
                    time.sleep(3)
                    displ.destroy()
                    time.sleep(0.1)
                    win.update()
                    time.sleep(0.1)
                    print ("")
                    print ("{} your hand is {}, you got burned!".format(self.name,self.hand))
                    break
                if self.stand_flag == 0:
                    print("")
                    displ = Label(win, text="{} your Cards are: {}, card value: {}".format(self.name, self.hand,self.hand_value))
                    displ.pack()
                    time.sleep(3)
                    displ.destroy()
                    win.update()
                    print "{} your Cards are: {}, card value: {}".format(self.name, self.hand,self.hand_value)
                if self.stand_flag == 1:
                    displ.destroy()
                    win.update()
                    print("")
                    print "This is your 2nd hand"
                    print "{} your Cards are: {}, card value: {}".format(self.name, self.second_hand,self.second_hand_value)
                    break
                if self.stand_flag == 2:
                    displ.destroy()
                    break
                time.sleep(3)
            except IOError:
                pass


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
win.geometry("1000x600")
win.title('Black Jack')


def turntimer():
    event.set()
    time.sleep(7)
    event.clear()


def update():
    while True:
        win.update()




Dealer = CardPlayer("Dealer", [], [], 50000, [], [],win)
PlayerOne = CardPlayer("Ben", [], [], 5000, [], [],win)
PlayerTwo = CardPlayer("Roni", [], [], 5000, [], [],win)
players = [PlayerOne, PlayerTwo]



thread = threading.Thread(target=main_game)

#make loop terminate when the user exits the window
thread.daemon = True
thread.start()
event = threading.Event()

#for player in players:
frame = Frame(win)
frame.pack()
#player 1 buttons
hitButton = Button(win, text="Hit - {}".format(PlayerOne.name), fg="green", bg="white", command=PlayerOne.deal_hand1)
standButton = Button(win, text="Stand", fg="red", bg="white", command=PlayerOne.stand)
splitButton = Button(win, text="Split", fg="blue", bg="white", command=PlayerOne.split)
doubleButton = Button(win, text="Double", fg="blue", bg="white",command =PlayerOne.double)
hitButton.place(x=310, y=550)
standButton.place(x=365, y=550)
splitButton.place(x=403, y=550)
doubleButton.place(x=435, y=550)

#player 2 buttons
hitButton = Button(win, text="Hit - {}".format(PlayerTwo.name), fg="green", bg="white", command=PlayerTwo.deal_hand1)
standButton = Button(win, text="Stand", fg="red", bg="white", command=PlayerTwo.stand)
splitButton = Button(win, text="Split", fg="blue", bg="white", command=PlayerTwo.split)
doubleButton = Button(win, text="Double", fg="blue", bg="white",command = PlayerTwo.double)
hitButton.place(x=460+20, y=550)
standButton.place(x=510+30, y=550)
splitButton.place(x=553+25, y=550)
doubleButton.place(x=588+22, y=550)







win.mainloop()

