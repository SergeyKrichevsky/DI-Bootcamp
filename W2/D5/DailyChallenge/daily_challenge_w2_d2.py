# Exercise 1: Quizz

# Answer the following questions:

# What is a class?
# - Class is a blueprint for creating objects, with custom defined properties and methods, the jbject will posess

# What is an instance?
# - Instance is an object, created based on perticular class

# What is encapsulation?
# - Encapsulation is: Hiding an attribute form direct access ("self.__attribute").
# It restrict direct access like to self.__attribute.
# and can be accessed (called) only within predefined methods
# It`s used to protect data from unauthorized or careless access

# What is abstraction?
# - Abstraction is hiding a "under the hood" details of processes. And showing user friendly information only

# What is inheritance?
# - Automaticly defining properties and methods for a new class (child) from anoter (perrent) class

# What is multiple inheritance?
# - Inhereting from multiple "perrent" classes

# What is polymorphism?
# - Having method or with the same name as in other class or classes, but with different functionality

# What is method resolution order or MRO?
# - MRO is order, in wich methods and attributes defined inside a class



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


deck_1 = Deck()
# print(deck_1.suit)
# print(deck_1.value)
print()
print(deck_1.deck)
print()
deck_1.shuffle()
print(deck_1.deck)

print()
print(deck_1.deal())
print()
print(deck_1.deck)