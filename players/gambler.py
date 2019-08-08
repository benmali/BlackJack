from .card_player import CardPlayer
from hand import Hand


class Gambler(CardPlayer):
    def __init__(self, name, deck):
        super().__init__('Gambler')
        self.bet = 0
        self.bank = 5000  # initial money of player
        self.hands = []  # player starts with 1 hand
        self.split = False
        self.name = name
        self.deck = deck
        if len(self.hands) > 2:
            raise ValueError("Illegal number of hands")


    def split(self):
        start_bet = self.hands[0].bet
        if self.hands[0].cards[0] == self.hands[0].cards[1]:
            self.split = True
            self.hands.append(Hand())  # creating a second hand
            for i in range(1):  # splitting cards to hands
                self.hands[i].cards = [self.hands[0].cards[i]]
            for i in range(1):
                self.hands[i].get_card(self.deck)
                self.hands[i].bet = start_bet / 2

        else:
            raise ValueError("Can\"t split uneven cards!")

    def check_active_hand(self):
        if len(self.hands) == 0:
            return None
        if self.hands[0].burn_flag or self.hands[0].stand_flag:
            if len(self.hands) == 2 and (self.hands[1].burn_flag or self.hands[1].stand):
                return self.hands[1]
            else:
                return None
        else:
            return self.hands[0]

    def player_turn(self):
        hand = self.check_active_hand()
        while hand is not None:  # as long as the player has an active hand playing
            if hand.value > 21 and not self.split:  # common condition for burning
                break

            if hand.value > 21 and self.split:  # In case 1st hand is burned but didn't play 2nd
                self.check_active_hand().burn_flag = True

            if hand.value == 21 and hand.black_jack:  # Hand is BlackJack
                self.check_active_hand().stand_flag = True

            hand = self.check_active_hand()

    def double(self):
        active_hand = self.check_active_hand()
        self.bank -= active_hand.bet
        active_hand.bet *= 2
        active_hand.get_card(self.deck)
        self.stand()

    def hit(self):
        hand = self.check_active_hand()
        if hand is not None:
            hand.get_card(self.deck)

    def stand(self):
        hand = self.check_active_hand()
        if hand is not None:
            hand.stand()

    def should_stop(self):
        if self.check_active_hand() is None:
            return True
        else:
            return False
