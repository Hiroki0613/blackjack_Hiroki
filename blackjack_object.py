# TODO (class Card) トランプ(suit=柄, number=数字)
# TODO (class Deck) デッキ (deal=カードを配る、shuffle)
# TODO (class Hand) 手札
# TODO (class Game) ゲーム

import random


class Card():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f'{self.suit} {self.number}'


trump = Card("🤍", 1)
print(trump)


class Deck():

    def __init__(self):
        suits = ['♠️', '❤︎', '♣️', '♦︎']
        numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.cards = []

        for suit in suits:
            for number in numbers:
                self.cards.append(Card(suit, number))

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


print(Deck().cards)

hand = Deck().deal()
print(hand)

deck = Deck()
deck.shuffle()
hand2 = deck.deal()
print(hand2)
