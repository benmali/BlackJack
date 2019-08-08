from enum import Enum


class CardTypes(Enum):
    HEARTS = 1
    SPADES = 2
    DIAMONDS = 3
    CLUBS = 4


class Card:
    def __init__(self, color: CardTypes, value: int):
        self.color = color
        self.value = value
        if self.color == CardTypes.DIAMONDS:
            self.color = "Diamonds"
        if self.color == CardTypes.CLUBS:
            self.color = "Clubs"
        if self.color == CardTypes.HEARTS:
            self.color = "Hearts"
        if self.color == CardTypes.SPADES:
            self.color = "Spades"
    def __repr__(self):
        return ("{} of {}".format(self.color, self.value))
