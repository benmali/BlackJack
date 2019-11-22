import random

from card import Card, CardTypes


class Deck:
    def __init__(self):
        cards = []
        for value in range(1, 14):
            cards.append(Card(CardTypes.CLUBS, value))
            cards.append(Card(CardTypes.HEARTS, value))
            cards.append(Card(CardTypes.SPADES, value))
            cards.append(Card(CardTypes.DIAMONDS, value))
        self.cards = cards

    def draw(self):
        return random.choice(self.cards)

