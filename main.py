from test import GraphicGame
from deck import Deck
from players import Gambler, Dealer
import time
import threading
from test import MainGraphicGame


class MainGame:
    def __init__(self, window, gamblers):
        self.dealer = window.dealer  # gets dealer object from main function
        self.gamblers = gamblers
        self.window = window
        self.deck = Deck()

    def start_game(self):
        print("Main Game activated")
        while True:
            time.sleep(7)
            active_players = [player for player in self.gamblers if player.hands[0].bet > 0]
            # player without bet is excluded
            if len(active_players) >= 1:
                break
        if len(active_players) > 0:  # if a gambler is active
            for player in active_players:  # deal 2 cards to initialize the game
                for i in range(2):
                    player.hands[0].get_card(self.deck)
                    print(player.hands[0].cards)
            for i in range(2):  # dealer gets 2 cards
                self.dealer.hand.get_card(self.deck)
                # end of game initialization

            # starting players' turns
            # every player gets his own frame, plays his hand
            frame = None
            for player in active_players:  # creating buttons for each player
                if frame is not None:  # if players have played before, destroy their old buttons
                    frame.destroy()
                frame = MainGraphicGame(self.window, player)
                self.window.frames[MainGraphicGame] = frame
                frame.pack()
                while not player.should_stop():  # not working properly, need to change to stop flashing cards
                    self.window.show_frame(MainGraphicGame)
                    self.window.show_cards(player)
                self.window.show_cards(player)  # show hands when player stops for burning or standing
            frame.destroy()
            self.conclude(active_players)

    def conclude(self, players):
        self.dealer.open_cards(self.deck)
        self.window.show_cards(self.dealer)
        if self.dealer.hand.value > 21:  # Dealer is burnt, all active hands win
            for player in players:
                for hand in player.hands:
                    if not hand.burn_flag:  # hand isn't burned
                        if hand.black_jack:  # hand is blackjack
                            hand.win_black(player)
                        else:  # hand is any value less than 21
                            hand.win(player)
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
                            hand.win_black(player)
                            continue
                        if hand.value > self.dealer.hand.value:
                            hand.win(player)
                            continue

                        if self.dealer.hand.value == hand.value:  # draw with dealer
                            hand.tie(player)
                            hand.win(player)
                            continue
        print("End of Game!")


deck = Deck()
active_players = []
g1 = Gambler("Ben", deck)
g2 = Gambler("Gil", deck)
dealer = Dealer()
win = GraphicGame(deck, dealer, [g1, g2])
win.geometry("1200x700")
win.title('Black Jack')
main = MainGame(win, [g1, g2])
thread = threading.Thread(target=main.start_game)
# make loop terminate when the user exits the window
thread.daemon = True
thread.start()
win.mainloop()
