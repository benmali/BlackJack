from abc import ABC
from typing import List

from card import Card
from hand import Hand



class CardPlayer(ABC):
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __repr__(self):
        return self.name


    @property
    def hand_value(self,hand):
        return self.calc_hand_value(hand)

    @property
    def hand_blackjack(self,hand):
        return len(hand.cards) == 2 and hand.value == 21

    @property
    def hand_burn(self,hand):
        return hand.value > 21

    def calc_hand_value(self, hand):
        return sum([card.value for card in hand])
    def show_cards_cli(self):
        for hand in self.hands:
            print(hand.cards)

    def draw(self, hand):
        pass


