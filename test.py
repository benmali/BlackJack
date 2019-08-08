
from hand import Hand
import time
from players import Dealer, Gambler
from deck import Deck
import tkinter as tk
import os
from PIL import ImageTk, Image


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
        for F in (MainGameWindow, BetPage):  # tuple of all pages in program
            frame = F(container, self, gamblers)  # defining a page
            self.frames[F] = frame  # adding page to dictionary
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(BetPage)  # showing bet page

    def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    def format_card(self, card):
        if card.value == 1:
            return card.color, "Ace"
        if card.value == 11:
            return card.color, "Jack"
        if card.value == 12:
            return card.color, "Queen"
        if card.value == 13:
            return card.color, "King"
        else:
            return card.color, card.value

    def show_hand_value(self, player, canvas):
        for hand in player.hands:
            canvas.create_text(150, 20, fill="black", font="Times 8 bold",
                          text="{}, your hand value is {} ".format(player.name, hand.value))

    def show_cards(self, player):
        img_lst = []
        start_pos = [100, 250]
        c = tk.Canvas(self, bg="white", height=500, width=700)
        for hand in player.hands:
            for card in hand.cards:
                color, value = self.format_card(card)  # converting card to display it
                image = Image.open(str(os.getcwd()) + "/cards/{}/{}/{}.png".format(value, color, value))
                image = image.resize((90, 120), Image.ANTIALIAS)  # The (150, 100) is (w, h)
                img = ImageTk.PhotoImage(image)
                img_lst.append(img)
            for img in img_lst:
                c.create_image(tuple(start_pos), image=img)  # add location instead of anchor
                c.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                start_pos[0] += 40
                start_pos[1] += 20
                self.show_hand_value(player,c)  # showing hand value on screen
            time.sleep(2)  # must put sleep here, or graphics disappear,causes "flashing"


class MainGameWindow(tk.Frame):
    def __init__(self, parent, controller, players):
        tk.Frame.__init__(self, parent)

        if players[0].check_active_hand() is None:
            current_player = players[1]
        else:
            current_player = players[0]
        self.create_bet_canvas(players)

        hit_button = tk.Button(self, text="   Hit   ", fg="green", bg="white", command=current_player.hit)
        stand_button = tk.Button(self, text="   Stand   ", fg="red", bg="white", command=current_player.stand)
        split_button = tk.Button(self, text="   Split   ", fg="blue", bg="white", command=current_player.split)
        double_button = tk.Button(self, text="   Double   ", fg="blue", bg="white", command=current_player.double)
        hit_button.place(x=640, y=700)
        stand_button.place(x=685, y=700)
        split_button.place(x=744, y=700)
        double_button.place(x=796, y=700)

    def create_bet_canvas(self, players):
        b = tk.Canvas(self, bg="white", height=750, width=1420)
        b.place(x=60, y=20)
        y = 20
        for player in players:
            b.create_text(70, y, fill="black", font="Times 8 bold",
                        text="{} your bank is {} ".format(player.name, player.bank))
            y += 25

    def canvas(self, players):
        b = tk.Canvas(self, bg="white", height=750, width=1420)
        b.place(x=60, y=20)


class BetPage(tk.Frame):

    def __init__(self, parent, controller, players):
        tk.Frame.__init__(self, parent)
        for player in players:
            label = tk.Label(self, text="{}, Your current bank is {}".format(player.name, player.bank))
            label.pack()
        label = tk.Label(self, text="Enter bets!")
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
