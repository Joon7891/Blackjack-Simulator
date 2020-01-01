from gui import Text, Button
import pygame

class SettingsScreen(object):
    def __init__(self):
        self.back_button = Button(5, 5, 50, 50,
                                  pygame.image.load("Content/Images/Sprites/Buttons/backButton.png"),
                                  Button.set_main_menu)

    def on_loop(self, window):
        self.update()
        self.draw(window)

    def update(self):
        self.back_button.update()

    def draw(self, window):
        self.back_button.draw(window)