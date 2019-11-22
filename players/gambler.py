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

    def split_cards(self):
        print("Attempting split")
        start_bet = self.hands[0].bet
        if (self.check_active_hand()).can_split():
            self.split = True
            self.hands.append(Hand())  # creating a second hand
            # splitting cards to hands
            self.hands[1].cards = [self.hands[0].cards[1]]
            del self.hands[0].cards[1]
            for i in range(2):
                self.hands[i].get_card(self.deck)
                self.hands[i].bet = start_bet / 2

        else:
            raise ValueError("Can\"t split uneven cards!")

    def check_active_hand(self):
        if len(self.hands) == 0:
            return None
        if self.hands[0].burn_flag or self.hands[0].stand_flag:  # if first hand stands or burns
            if len(self.hands) == 2 and not (self.hands[1].burn_flag or self.hands[1].stand_flag):  # if player has 2 hands
                return self.hands[1]
            else:
                return None

        else:
            return self.hands[0]

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
            print(hand)

    def stand(self):
        hand = self.check_active_hand()
        if hand is not None:
            hand.stand()

    def should_stop(self):
        if self.check_active_hand() is None:
            return True
        else:
            return False
