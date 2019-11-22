import tkinter as tk
from hand import Hand
import time
from players import Dealer, Gambler
from deck import Deck
import threading
import threading
import time
from PIL import ImageTk, Image
import os
from deck import Deck
from players import Gambler, Dealer
import time
import threading
from hand import Hand


#from main import start_game

deck = Deck()
active_players = []
g1 = Gambler("Ben", deck)
g2 = Gambler("Gil", deck)
dealer = Dealer()


class GraphicGame(tk.Tk):
    def __init__(self, deck, dealer, gamblers):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.deck = deck
        self.dealer = dealer
        self.gamblers = gamblers
        self.players = gamblers.copy().append(dealer)
        self.current_player_idx = 0

        self.frames = {}  # dictionary to place all pages
        for F in (BetPage, MainGameWindow):  # tuple of all pages in program
            frame = F(container, self, gamblers)  # defining a page
            self.frames[F] = frame  # adding page to dictionary
            frame.grid(row=0, column=0, sticky="nsew")

        frame = BetPage(container,self,[g1,g2])  # creating frame for bet page
        self.frames[BetPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(BetPage)  # showing bet page

    def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()


class BetPage(tk.Frame):
    def __init__(self, parent, controller, players):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter Your Bet")
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Enter a number to bets!")
        label.pack()
        input = tk.Entry(self)
        input.pack()
        self.update()
        button3 = tk.Button(self, text="Add Bet",
                            command=lambda: self.get_input(input, players))
        button3.pack()
        button4 = tk.Button(self, text="Continue to Game",
                            command=lambda: controller.show_frame(MainGameWindow))
        button4.pack()

    def get_input(self, input, players):  # this function belongs to bet page
        hand = Hand()
        hand.bet = int(input.get())
        if len(players[0].hands) == 0:
            players[0].hands.append(hand)
            label = tk.Label(self, text="{}, {} bet was entered".format(players[0], hand.bet))
            label.pack()
            return
        if len(players[1].hands) == 0:
            players[1].hands.append(hand)
            label = tk.Label(self, text="{}, {} bet was entered".format(players[1], hand.bet))
            label.pack()
            return

    @property
    def current_player(self):
        return self.gamblers[self.current_player_idx]

    def split(self):
        self.current_player.split()
        self.draw_split()


class MainGameWindow(tk.Frame):
    def __init__(self, parent, controller, players):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Game Window")
        label.pack()
        if players[0].check_active_hand() is None:
            current_player = players[1]
        else:
            current_player = players[0]

        label = tk.Label(self, text="{}, Enter a number to bet!".format(players))
        label.pack()
        self.create_bet_canvas(players)

        hit_button = tk.Button(self, text="Hit", fg="green", bg="white", command=current_player.hit)
        stand_button = tk.Button(self, text="Stand", fg="red", bg="white", command=current_player.stand)
        split_button = tk.Button(self, text="Split", fg="blue", bg="white", command=current_player.split)
        double_button = tk.Button(self, text="Double", fg="blue", bg="white", command=current_player.double)
        hit_button.place(x=310, y=550)
        stand_button.place(x=365, y=550)
        split_button.place(x=403, y=550)
        double_button.place(x=435, y=550)

    def create_bet_canvas(self, players):
        b = tk.Canvas(self, bg="white", height=80, width=150)
        b.place(x=60, y=20)
        y = 20
        for player in players:
            b.create_text(70, 20, fill="black", font="Times 8 bold",
                        text="{} your bank is {} ".format(player.name, player.bank))




"""

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

            print(" your bet is: ", self.bet)

            # Bet entered successfully

            if self.bet <= self.money:
                self.money -= self.bet

            else:
                print("Not enough money to bet!!!")

        except ValueError:  # If bet was not entered on time, bet stays 0, and the user will not play this turn
            input.destroy()
            label.destroy()

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
                              text="{} your cards value is {}\nDealer upside card is {} ".format(self.name,
                                                                                                 self.hand_value,
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
    """
