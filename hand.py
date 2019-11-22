

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

    def __repr__(self):
        return str(self.cards)

    def can_split(self):
        cardlst = [card for card in self.cards if card.value >= 10]  # 2 cards in list if hand has 2 royalty or 10
        if len(cardlst) == 2:
            return True
        if self.cards[0].value == self.cards[1].value:
            return True
        else:
            print("cant split")
            return False

    def calc_hand_value(self):
        c_copy = [card.value for card in self.cards]
        c_copy = sorted(c_copy, reverse=True)
        cardlst = []
        for value in c_copy:
            if value > 10:
                cardlst.append(10)
                continue
            if value <= 10 and value != 1:
                cardlst.append(value)
                continue
            if value == 1:
                if sum(cardlst) + 11 > 21:
                    cardlst.append(1)
                    continue
                else:
                    cardlst.append(11)
        summ = sum(cardlst)
        print(cardlst)
        if summ == 21 and len(self.cards) == 2:
            self.black_jack = True
            self.stand_flag = True
            return summ

        if summ == 21:
            self.stand_flag = True
            return summ

        if summ > 21:
            self.burn_flag = True
        return summ

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
        player.bank += self.bet
        self.bet = 0

    def win_black(self, player):
        self.bet *= 2.5
        player.bank += self.bet
        self.bet = 0

    def tie(self, player):
        player.bank += self.bet
        self.bet = 0
