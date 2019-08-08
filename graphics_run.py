from tkinter import *
import threading
import time
from PIL import ImageTk, Image
import os
from graphic_game import GraphicGame


class Rungame(GraphicGame):
    def __init__(self, deck, dealer, gamblers):
        self.deck = deck
        self.dealer = dealer
        self.gamblers = gamblers
        self.players = gamblers.copy().append(dealer)
        self.current_player_idx = 0


        b = Canvas(win, bg="white", height=80, width=150)
        b.place(x=60, y=20)
        y = 20
        for player in players:
            b.create_text(70, 20, fill="black", font="Times 8 bold",
                          text="{} your bank is {} ".format(player.name, player.bank))