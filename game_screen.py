import pygame

class GameScreen(object):
    def __init__(self):
        pass

    def on_loop(self, window):
        self.update()
        self.draw(window)

    def update(self):
        pass

    def draw(self, window):
        pass