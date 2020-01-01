from colour import Colour
from gui import Text
import font

class Player(object):
    def __init__(self):
        self.cards = []

    def get_sum(self):
        total = 0
        for card in self.cards:
            pass

class User (Player):
    def __init__(self, balance=1000):
        self.balance = balance
        self.balance_text = Text(f"${balance}", font.get_font('Content/Fonts/SF-Atarian-System-Bold.ttf', 40),
                                 Colour.White, 300, 370)

    def set_balance(self, new_balance):
        self.balance = new_balance
        self.balance_text = Text(f"${balance}", font.get_font('Content/Fonts/SF-Atarian-System-Bold.ttf', 40),
                                 Colour.White, 300, 370)

    def draw(self, window):
        self.balance_text.draw(window)

class Dealer(Player):
    pass