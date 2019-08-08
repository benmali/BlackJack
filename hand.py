from abc import ABC
from typing import List
from card import Card
from deck import Deck


class Hand:

    def __init__(self):
        self.value = 0
        self.cards = []
        self.bet = 0
        self.ace_flag = False
        self.ace_counter = 0
        self.stand_flag = False
        self.burn_flag = False
        self.black_jack = False

    def calc_hand_value(self):
        total = 0
        for card in self.cards:
            if card.value > 10:  # card is royalty
                total += 10
                continue

            if card.value == 1 and total < 21:  # card is ace and sum is less than 21
                total += 11
                continue

            if card.value == 1 and total > 21:  # card is ace and sum is over 21
                if self.ace_counter == 1:
                    self.ace_flag = False
                else:
                    self.ace_counter -= 1
                total += 1
                continue

            else:
                total += card.value

        if total == 21 and len(self.cards) == 2:
            self.black_jack = True

        if total > 21:
            self.burn_flag = True
        return total

    def get_card(self, deck):  # calls get card method on specific deck
        drawn_card = deck.draw()
        self.cards.append(drawn_card)
        if drawn_card.value == 1:
            self.ace_flag = True
            self.ace_counter += 1
        self.value = self.calc_hand_value()

    def stand(self):
        self.stand_flag = True

    def win(self, player):
        self.bet *= 2
        player.money += self.bet
        self.bet = 0

    def win_black(self, player):
        self.bet *= 2.5
        player.money += self.bet
        self.bet = 0

    def tie(self, player):
        player.money += self.bet
        self.bet = 0
