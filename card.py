from enum import Enum
from pygame import *
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
    cards = {}
    width = 25
    height = 35

    @staticmethod
    def load():
        file_path = 'Content/Images/Sprites/Cards/'

        # Loading card images into a static class dictionary
        Card.back_image = transform.scale(image.load(f"{file_path}cardBack.png"),
                                                    (Card.width, Card.height))
        for suit in Suit:
            suit_cards = {}
            for i in range(1, 14):
                suit_cards[Rank(i)] = transform.scale(image.load(f"{file_path}{suit.name}{i}.png"),
                                                      (Card.width, Card.height))
            Card.cards[suit] = suit_cards

    def __init__(self, suit, rank, x, y, reveal=False):
        self.suit = suit
        self.rank = rank
        self.x, self.y = x, y
        self.image = Card.cards[suit][rank]
        self.reveal = reveal

    def draw(self, window):
        window.blit(self.image if self.reveal else Card.back_image, (self.x, self.y))

class Deck(object):
    def __init__(self, x, y):
        self.deck = []

        for i in range(4):
            for j in range(1, 14):
                self.deck.append(Card(Suit(i), Rank(j), x, y))

        random.shuffle(self.deck)

    def get_card(self):
        return self.deck.pop()