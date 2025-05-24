# Exercise 2: Create a deck of cards class

import random

class Deck:
    def __init__(self):
        self.suit = {"Hearts", "Diamonds", "Clubs", "Spades"}
        self.value = {"A",'2','3','4','5','6','7','8','9','10','J','Q','K'}
        self.deck = []

    def shuffle(self):
        self.deck = []
        for suit in self.suit:
            for value in self.value:
                self.deck.append([value, suit])
        random.shuffle(self.deck)

    def deal(self):
        card_index = random.randint(0, len(self.deck) -1)
        card = self.deck[card_index]
        self.deck.pop(card_index)
        return card


# deck_1 = Deck()
# print(deck_1.suit)
# print(deck_1.value)
# print()
# print(deck_1.deck)
# print()
# deck_1.shuffle()
# print(deck_1.deck)

# print()
# print(deck_1.deal())
# print()
# print(deck_1.deck)