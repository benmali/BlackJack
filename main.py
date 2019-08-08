from deck import Deck
from players import Gambler, Dealer
import time
import threading
import tkinter as tk
from graphic_game import GraphicGame



class MainGame:
    def __init__(self):
        self.dealer = Dealer()
        deck = Deck()
        g1 = Gambler("Ben",deck )
        g2 = Gambler("Gil",deck)
        self.win = GraphicGame(deck, dealer, [g1, g2])

    def start_game(self):
        print("Main Thread activated")
        deck = Deck()
        g1 = Gambler("Ben",)
        g2 = Gambler("Gil")
        gamblers = [g1, g2]
        g1.bet, g2.bet = 2,2
        active_players = [player for player in gamblers if player.bet > 0]  # player without bet is excluded
        if len(active_players) > 0:  # if a gambler is active
            for player in active_players:  # deal 2 cards to initialize the game
                for i in range(2):
                    player.hands[0].get_card(deck)
                    print(player.hands[0].cards)
                for i in range(2):  # dealer gets 2 cards
                    self.dealer.hand.get_card(deck)
            for player in active_players:
                while not player.should_stop():
                    time.sleep(0.1)

    def conclude(self, players):
        if self.dealer.hand.value > 21:  # Dealer is burnt, all active hands win
            for player in players:
                for hand in player.hands:
                    if not hand.burn_flag:  # hand isn't burned
                        if hand.black_jack:  # hand is blackjack
                            player.bank += hand.win_black(player)
                        else:  # hand is any value less than 21
                            player.bank += hand.win(player)
        else:
            for player in players:
                for hand in player.hands:
                    if self.dealer.hand.burn_flag and not hand.burn_flag:  # Dealer burn - auto win for active hands
                        if hand.black_jack:  # hand is blackjack
                            hand.win_black(player)
                            continue
                        else:  # hand is any valid value
                            hand.win(player)
                            continue

                    if not hand.burn_flag and not self.dealer.hand.burn_flag:  # hand isn't burned, dealer isn't burned

                        if hand.black_jack and not self.dealer.hand.black_jack:  # winning scenarios
                            player.bank += hand.win_black(player)
                            continue
                        if hand.value > self.dealer.hand.value:
                            hand.win(player)
                            continue

                        if self.dealer.hand.value == hand.value:  # draw with dealer
                            player.bank = hand.tie(player)
                            player.bank += hand.win(player)
                            continue


deck = Deck()
active_players = []
g1 = Gambler("Ben",deck)
g2 = Gambler("Gil",deck)
dealer = Dealer()

main = MainGame()
win = GraphicGame(deck, dealer, [g1, g2])
thread = threading.Thread(target=main.start_game)
# make loop terminate when the user exits the window
thread.daemon = True
thread.start()
win.mainloop()