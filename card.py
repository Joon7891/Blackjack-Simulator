from enum import Enum
import random

class Suit(Enum):
    Clubs = 0
    Spades = 1
    Hearts = 2
    Diamonds = 3

class Rank(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image =

    def draw(self):
        pass

class Deck(object):
    def __init__(self):
        self.deck = []

        for i in range(4):
            for j in range(1, 14):
                self.deck.append(Card(Suit(i), Rank(j)))

        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()