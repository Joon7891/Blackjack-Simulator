import pygame

class Button(object):
    def __init__(self, x, y, width, height, image, func):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.image = image
        self.func = func

    def update(self):
        pass

    def draw(self):
        pass