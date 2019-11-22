from .card_player import CardPlayer
from hand import Hand


class Dealer(CardPlayer):
    def __init__(self):
        super().__init__('Dealer')
        self.hand = Hand()


    def open_cards(self, deck):
        while True:
            if self.hand.value < 17:
                self.hand.get_card(deck)
            if self.hand.value >= 17:
                break
        return self.hand.value

    @property
    def hand2_value(self):
        raise Exception('The dealer has no hand 2')
