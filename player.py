class Player(object):
    def __init__(self):
        self.cards = []

    def get_sum(self):
        total = 0
        for card in self.cards:
            pass

class User (Player):
    def __init__(self):
        self.balance = 500

class Dealer(Player):
    pass